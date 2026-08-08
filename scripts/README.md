# 🛠️ 配套脚本（scripts/）

> 中文 | [English](README.en.md)

本目录包含仓库维护相关的辅助脚本。

## fetch_open_access_pdfs.py

根据统一论文清单 `reading-list/papers.json` 中的条目，尝试解析并抓取可公开获取的论文 PDF（例如 arXiv / OpenReview 等）。

- 查看参数：`python3 scripts/fetch_open_access_pdfs.py --help`
- 下载 PDF 到本地镜像目录：`python3 scripts/fetch_open_access_pdfs.py --download`
- 解析原始链接并回写 `papers.json`（`url` 字段）：`python3 scripts/fetch_open_access_pdfs.py --update-index`
- 根据解析结果更新 `reading-list/README(.en).md` 链接（原文为主、本地镜像为辅）：`python3 scripts/fetch_open_access_pdfs.py --update-readme`

> 链接策略：`url` 字段优先写开放获取 PDF 的**原始下载链接**（arXiv 等），无 PDF 时回退到论文落地页（作者主页/OpenReview）。本地 PDF 仅作为镜像兜底，不是主要下载途径。

返回总览：[README.md](../README.md)
