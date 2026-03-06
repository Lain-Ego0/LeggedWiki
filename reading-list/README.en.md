# Reading List (RL Locomotion / Legged / Humanoids)

> English | [中文](README.md)

This folder organizes papers by lab/source and topic, and (when possible) keeps **open-access PDFs** under `recommended-papers/` (preferably arXiv preprints). For works without an open-access PDF, we keep the citation and a note on where to find it.

## Index
- ETH Robotics Systems Lab (RSL): [ETH-RSL.en.md](<ETH-RSL.en.md>)
- KAIST (Raibo / Unitree, etc.): [KAIST.en.md](<KAIST.en.md>)
- Others (quadrupeds/bipeds/general): [其他.en.md](<其他.en.md>)
- Humanoids: [人形.en.md](<人形.en.md>)
- Surveys: [综述.en.md](<综述.en.md>)
- By topic: [按主题.en.md](<按主题.en.md>)

## Update / Fetch PDFs
1. Add or edit entries in `reading-list/papers.json`.
2. Run:

```bash
python3 scripts/fetch_open_access_pdfs.py --download
```

Note: the script mainly fetches from arXiv/open-access sources. For items hosted on OpenReview or author pages, you may need to add a more specific query in `papers.json` or download manually into `recommended-papers/` and link it from the corresponding reading-list page.
