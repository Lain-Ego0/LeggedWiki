# Recommended Papers Local PDFs (Storage Folder)

> English | [中文](README.md)

`recommended-papers/` is now merged with `reading-list`: this folder is only used to store local PDF files (a **mirror fallback**), and no longer keeps a duplicated paper index page.

> Link policy: the primary download link in the paper index is the **original source** (arXiv / OpenReview / author page — see the `url` field in `reading-list/papers.json`). The local PDFs in this folder are only a mirror fallback for when the original link is unreachable. Chinese materials (theses/notes, etc.) have no public original link and remain local-PDF only.

## Unified Entry
- Paper index and notes: [reading-list/README.en.md](../reading-list/README.en.md)
- Update/fetch workflow: [reading-list/README.en.md#update-fetch](../reading-list/README.en.md#update-fetch)
- Resolve original links and write them back into the index: `python3 scripts/fetch_open_access_pdfs.py --update-index`
- Download PDFs into this folder: `python3 scripts/fetch_open_access_pdfs.py --download`
- Update index README links (original first): `python3 scripts/fetch_open_access_pdfs.py --update-readme`

## Directory Layout (Storage Layer)
- ETH RSL: `ETH-RSL/`
- KAIST: `KAIST/`
- MIT: `MIT/`
- Humanoids: `humanoid/`
- Surveys: `surveys/`
- Other (quadruped/biped/general): `other/`
- Chinese materials (theses/notes, etc.): `chinese/`

Back to overview: [README.en.md](../README.en.md)
