# 推荐论文本地 PDF（存储目录）

> 中文 | [English](README.en.md)

`recommended-papers/` 已与 `reading-list` 功能合并：本目录仅负责存放本地 PDF 文件（**镜像兜底**），不再维护重复的论文索引页面。

> 链接策略：论文索引中的主要下载链接是**原始来源**（arXiv / OpenReview / 作者主页，见 `reading-list/papers.json` 的 `url` 字段）；本目录的本地 PDF 只作为镜像兜底，供无法访问原始链接时使用。中文资料（学位论文/笔记等）无原始公开链接，仍以本地 PDF 为准。

## 统一入口
- 论文索引与笔记：[reading-list/README.md](../reading-list/README.md)
- 更新与抓取说明：[reading-list/README.md#update](../reading-list/README.md#update)
- 解析原始链接并回写索引：`python3 scripts/fetch_open_access_pdfs.py --update-index`
- 下载 PDF 到本目录：`python3 scripts/fetch_open_access_pdfs.py --download`
- 更新索引 README 链接（原文为主）：`python3 scripts/fetch_open_access_pdfs.py --update-readme`

## 目录结构（存储层）
- ETH RSL：`ETH-RSL/`
- KAIST：`KAIST/`
- MIT：`MIT/`
- 人形：`humanoid/`
- 综述：`surveys/`
- 其他（四足/双足/通用）：`other/`
- 中文资料（学位论文/笔记等）：`chinese/`

返回总览：[README.md](../README.md)
