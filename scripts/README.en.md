# 🛠️ Supporting Scripts (scripts/)

> [中文](README.md) | English

This folder contains helper scripts for maintaining this repository.

## fetch_open_access_pdfs.py

Resolves and fetches publicly available paper PDFs based on the unified paper list in `reading-list/papers.json` (e.g., arXiv / OpenReview when available).

- Show help: `python3 scripts/fetch_open_access_pdfs.py --help`
- Download PDFs to the local mirror folder: `python3 scripts/fetch_open_access_pdfs.py --download`
- Resolve original links and write them back into `papers.json` (`url` field): `python3 scripts/fetch_open_access_pdfs.py --update-index`
- Update `reading-list/README(.en).md` links from the report (original link primary, local mirror as fallback): `python3 scripts/fetch_open_access_pdfs.py --update-readme`

> Link policy: the `url` field prefers the **original download link** of the open-access PDF (e.g., arXiv); falls back to a landing page (author page / OpenReview) when no PDF exists. Local PDFs are only a mirror fallback, not the primary download path.

Back to overview: [README.en.md](../README.en.md)
