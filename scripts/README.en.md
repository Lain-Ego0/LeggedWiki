# 🛠️ Supporting Scripts (scripts/)

> [中文](README.md) | English

This folder contains helper scripts for maintaining this repository.

## resolve_paper_links.py

Resolves original paper source links based on the unified paper list in `reading-list/papers.json` (e.g., arXiv / OpenReview when available). The script does not download or store PDFs.

- Show help: `python3 scripts/resolve_paper_links.py --help`
- Resolve original links and write them back into `papers.json` (`url` field): `python3 scripts/resolve_paper_links.py --update-index`
- `reading-list/README(.en).md` keeps original-source links only; no local PDF mirror links are generated.

> Link policy: the `url` field prefers the original public source (e.g., arXiv); falls back to a landing page (author page / OpenReview) when no direct PDF exists. The repository does not store paper PDFs.

Back to overview: [README.en.md](../README.en.md)
