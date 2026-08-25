# 🛠️ 配套脚本（scripts/）

> 中文 | [English](README.en.md)

本目录包含仓库维护相关的辅助脚本。

## resolve_paper_links.py

根据统一论文清单 `reading-list/papers.json` 中的条目，解析并记录原始论文来源链接（例如 arXiv / OpenReview 等）。脚本不下载、不保存 PDF。

- 查看参数：`python3 scripts/resolve_paper_links.py --help`
- 解析原始链接并回写 `papers.json`（`url` 字段）：`python3 scripts/resolve_paper_links.py --update-index`
- `reading-list/README(.en).md` 只保留原始来源链接，不再生成本地 PDF 镜像链接。

> 链接策略：`url` 字段优先写原始公开来源（arXiv 等），无直接 PDF 时回退到论文落地页（作者主页/OpenReview）。仓库不保存论文 PDF。

返回总览：[README.md](../README.md)
