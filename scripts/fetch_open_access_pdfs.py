#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


SEMANTIC_SCHOLAR_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
ARXIV_API_URL = "https://export.arxiv.org/api/query"
DEFAULT_FIELDS = [
    "title",
    "year",
    "venue",
    "authors",
    "url",
    "externalIds",
    "openAccessPdf",
    "isOpenAccess",
]


def _norm_title(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"[\s\-_:]+", " ", title)
    title = re.sub(r"[^\w\s]", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def _similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, _norm_title(a), _norm_title(b)).ratio()


def _sanitize_filename(name: str, max_len: int = 180) -> str:
    name = name.strip()
    name = re.sub(r"[\\/:*?\"<>|]", "-", name)
    name = re.sub(r"\s+", " ", name).strip()
    if len(name) > max_len:
        name = name[: max_len - 1].rstrip() + "…"
    return name


def _http_get_json(url: str, timeout: int = 30) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ROBOCON-Legged-Robot/1.0 (open-access fetcher; +https://github.com/)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))


def _http_get_json_with_retries(
    url: str,
    *,
    timeout: int = 30,
    max_retries: int = 6,
    base_backoff_s: float = 2.0,
) -> dict[str, Any]:
    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            return _http_get_json(url, timeout=timeout)
        except urllib.error.HTTPError as e:
            last_err = e
            retry_after = e.headers.get("Retry-After") if hasattr(e, "headers") else None
            if e.code == 429 and attempt < max_retries:
                sleep_s = float(retry_after) if retry_after else base_backoff_s * (2**attempt)
                print(f"  -> rate limited (429), retry in {sleep_s:.1f}s", file=sys.stderr)
                time.sleep(sleep_s)
                continue
            raise
        except Exception as e:
            last_err = e
            if attempt < max_retries:
                sleep_s = base_backoff_s * (2**attempt)
                print(f"  -> transient error, retry in {sleep_s:.1f}s: {e}", file=sys.stderr)
                time.sleep(sleep_s)
                continue
            raise
    assert last_err is not None
    raise last_err


def _download_file(url: str, dest: Path, timeout: int = 60) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ROBOCON-Legged-Robot/1.0 (open-access fetcher; +https://github.com/)",
            "Accept": "*/*",
        },
    )
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp, tmp.open("wb") as f:
            while True:
                chunk = resp.read(1024 * 128)
                if not chunk:
                    break
                f.write(chunk)
        tmp.replace(dest)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except Exception:
                pass


@dataclass
class PaperQuery:
    group: str
    title: str
    venue: Optional[str]
    year: Optional[int]
    notes: str
    query: Optional[str]


def _load_papers(path: Path) -> list[PaperQuery]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    papers: list[PaperQuery] = []
    for item in raw:
        papers.append(
            PaperQuery(
                group=str(item.get("group") or "其他"),
                title=str(item["title"]),
                venue=item.get("venue"),
                year=item.get("year"),
                notes=str(item.get("notes") or ""),
                query=item.get("query"),
            )
        )
    return papers


def _pick_best_match(
    query: PaperQuery, candidates: list[dict[str, Any]]
) -> Optional[dict[str, Any]]:
    expected_year = query.year
    expected_venue = (query.venue or "").lower().strip()

    scored: list[tuple[float, dict[str, Any]]] = []
    for c in candidates:
        title = c.get("title") or ""
        score = _similarity(query.title, title)
        year = c.get("year")
        venue = (c.get("venue") or "").lower().strip()

        if expected_year and year:
            if year == expected_year:
                score += 0.08
            elif abs(int(year) - int(expected_year)) <= 1:
                score += 0.03
            else:
                score -= 0.08

        if expected_venue and venue:
            if expected_venue in venue or venue in expected_venue:
                score += 0.05

        scored.append((score, c))

    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best = scored[0]
    if best_score < 0.72:
        return None
    return best


def _search_semantic_scholar(query_text: str, limit: int = 5) -> list[dict[str, Any]]:
    params = {
        "query": query_text,
        "limit": str(limit),
        "fields": ",".join(DEFAULT_FIELDS),
    }
    url = SEMANTIC_SCHOLAR_SEARCH_URL + "?" + urllib.parse.urlencode(params)
    data = _http_get_json_with_retries(url)
    return list(data.get("data") or [])


def _search_arxiv(query: str, max_results: int = 5) -> list[dict[str, Any]]:
    params = {
        "search_query": query,
        "start": "0",
        "max_results": str(max_results),
    }
    url = ARXIV_API_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ROBOCON-Legged-Robot/1.0 (open-access fetcher; +https://github.com/)",
            "Accept": "application/atom+xml, application/xml;q=0.9, */*;q=0.1",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_bytes = resp.read()

    root = ET.fromstring(xml_bytes)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries: list[dict[str, Any]] = []
    for entry in root.findall("a:entry", ns):
        entry_title = (entry.findtext("a:title", default="", namespaces=ns) or "").strip()
        entry_id_url = (entry.findtext("a:id", default="", namespaces=ns) or "").strip()
        published = (entry.findtext("a:published", default="", namespaces=ns) or "").strip()
        updated = (entry.findtext("a:updated", default="", namespaces=ns) or "").strip()

        arxiv_id = None
        m = re.search(r"/abs/([^/]+)$", entry_id_url)
        if m:
            arxiv_id = m.group(1)
        if arxiv_id:
            arxiv_id = arxiv_id.split("v", 1)[0]

        entries.append(
            {
                "title": entry_title,
                "arxivId": arxiv_id,
                "absUrl": entry_id_url,
                "published": published,
                "updated": updated,
            }
        )
    return entries


def _pick_best_arxiv_match(query: PaperQuery, candidates: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    expected_year = query.year
    scored: list[tuple[float, dict[str, Any]]] = []
    for c in candidates:
        title = c.get("title") or ""
        score = _similarity(query.title, title)

        if expected_year:
            published = c.get("published") or ""
            if len(published) >= 4 and published[:4].isdigit():
                year = int(published[:4])
                if year == expected_year:
                    score += 0.06
                elif abs(year - expected_year) <= 1:
                    score += 0.02
                else:
                    score -= 0.06

        scored.append((score, c))

    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best = scored[0]
    if best_score < 0.74:
        return None
    if not best.get("arxivId"):
        return None
    return best


def _group_to_dir(group: str) -> str:
    group = group.strip()
    mapping = {
        "ETH-RSL": "recommended-papers/ETH-RSL",
        "KAIST": "recommended-papers/KAIST",
        "综述": "recommended-papers/surveys",
        "人形": "recommended-papers/humanoid",
    }
    return mapping.get(group, "recommended-papers/other")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch open-access PDFs for a reading list (via Semantic Scholar)."
    )
    parser.add_argument(
        "--papers",
        default="reading-list/papers.json",
        help="Path to papers.json (default: reading-list/papers.json)",
    )
    parser.add_argument(
        "--report",
        default="reading-list/fetch_report.json",
        help="Where to write JSON report (default: reading-list/fetch_report.json)",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download open-access PDFs when available",
    )
    parser.add_argument(
        "--use-semantic-scholar",
        action="store_true",
        help="Use Semantic Scholar as a fallback when arXiv search misses (may be rate-limited)",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=2.5,
        help="Seconds to sleep between API calls (default: 2.5)",
    )
    args = parser.parse_args()

    papers_path = Path(args.papers)
    report_path = Path(args.report)
    if not papers_path.exists():
        print(f"papers file not found: {papers_path}", file=sys.stderr)
        return 2

    papers = _load_papers(papers_path)
    report: list[dict[str, Any]] = []

    ok = 0
    downloaded = 0
    skipped_no_pdf = 0
    unmatched = 0

    for i, pq in enumerate(papers, start=1):
        print(f"[{i}/{len(papers)}] {pq.group} | {pq.title}")
        arxiv_match = None
        try:
            arxiv_candidates = _search_arxiv(f'ti:"{pq.title}"', max_results=6)
            arxiv_match = _pick_best_arxiv_match(pq, arxiv_candidates)
            if not arxiv_match:
                arxiv_candidates = _search_arxiv(f'all:"{pq.title}"', max_results=6)
                arxiv_match = _pick_best_arxiv_match(pq, arxiv_candidates)
        except Exception as e:
            report.append({"group": pq.group, "title": pq.title, "error": f"arxiv_failed: {e}"})
            time.sleep(args.sleep)
            continue

        match = None
        match_source = None
        if arxiv_match:
            match = arxiv_match
            match_source = "arxiv"
        elif args.use_semantic_scholar:
            query_text = pq.query or pq.title
            try:
                candidates = _search_semantic_scholar(query_text, limit=6)
                match = _pick_best_match(pq, candidates)
                match_source = "semantic_scholar" if match else None
            except Exception as e:
                report.append(
                    {
                        "group": pq.group,
                        "title": pq.title,
                        "error": f"semantic_scholar_failed: {e}",
                    }
                )
                time.sleep(args.sleep)
                continue

        if not match:
            unmatched += 1
            report.append(
                {
                    "group": pq.group,
                    "title": pq.title,
                    "matched": False,
                    "source": "none",
                }
            )
            time.sleep(args.sleep)
            continue

        ok += 1
        paper_url = None
        doi = None
        oa_pdf_url = None
        arxiv_id = None
        is_open_access = True

        if match_source == "arxiv":
            arxiv_id = match.get("arxivId")
            paper_url = match.get("absUrl")
            oa_pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else None
        else:
            open_access_pdf = match.get("openAccessPdf") or {}
            if isinstance(open_access_pdf, dict):
                oa_pdf_url = open_access_pdf.get("url")

            external_ids = match.get("externalIds") or {}
            if isinstance(external_ids, dict):
                arxiv_id = external_ids.get("ArXiv") or external_ids.get("arXiv")
                doi = external_ids.get("DOI")

            is_open_access = bool(match.get("isOpenAccess")) or bool(oa_pdf_url)
            paper_url = match.get("url")

        local_path = None
        pdf_source_url = None

        if is_open_access:
            if oa_pdf_url:
                pdf_source_url = oa_pdf_url
            elif arxiv_id:
                pdf_source_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

        if args.download and pdf_source_url:
            year = match.get("year") or pq.year
            year_prefix = f"{year} - " if year else ""
            filename = _sanitize_filename(f"{year_prefix}{match.get('title') or pq.title}.pdf")
            target_dir = Path(_group_to_dir(pq.group))
            dest = target_dir / filename
            local_path = str(dest)

            if dest.exists() and dest.stat().st_size > 0:
                print(f"  -> exists: {dest}")
            else:
                try:
                    _download_file(pdf_source_url, dest)
                    downloaded += 1
                    print(f"  -> downloaded: {dest}")
                except Exception as e:
                    print(f"  -> download failed: {e}")
                    local_path = None
        else:
            if args.download and not pdf_source_url:
                skipped_no_pdf += 1

        report.append(
            {
                "group": pq.group,
                "title": pq.title,
                "matched": True,
                "source": match_source,
                "matchedTitle": match.get("title"),
                "year": match.get("year") if match_source != "arxiv" else None,
                "venue": match.get("venue") if match_source != "arxiv" else "arXiv",
                "paperUrl": paper_url,
                "doi": doi,
                "isOpenAccess": bool(match.get("isOpenAccess")) if match_source != "arxiv" else True,
                "openAccessPdfUrl": oa_pdf_url,
                "arxivId": arxiv_id,
                "downloadedPath": local_path,
                "pdfSourceUrl": pdf_source_url,
            }
        )

        time.sleep(args.sleep)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("")
    print("Summary:")
    print(f"  matched:      {ok}/{len(papers)}")
    print(f"  unmatched:    {unmatched}")
    if args.download:
        print(f"  downloaded:   {downloaded}")
        print(f"  no OA pdf:    {skipped_no_pdf}")
        print(f"  report:       {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
