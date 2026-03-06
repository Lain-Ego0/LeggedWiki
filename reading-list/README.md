# 阅读清单（RL 运控 / 足式 / 人形）

> 中文 | [English](README.en.md)

本目录按来源与主题整理论文，并尽可能在 `recommended-papers/` 中提供**可公开获取**的 PDF（优先 arXiv 预印本）。若某些期刊/会议论文未找到公开 PDF，会只保留引用与获取建议。

## 索引
- ETH Robotics Systems Lab（RSL）：[ETH-RSL.md](<ETH-RSL.md>)
- KAIST（Raibo / Unitree 等）：[KAIST.md](<KAIST.md>)
- 其他四足/通用（AMP、跑酷、视觉、loco-manipulation 等）：[其他.md](<其他.md>)
- 人形（whole-body control / teleop / getting-up 等）：[人形.md](<人形.md>)
- 综述：[综述.md](<综述.md>)
- 按主题索引：[按主题.md](<按主题.md>)

## 如何更新/抓取
1. 在 `reading-list/papers.json` 新增/更新条目（title / venue / year / notes / group）。
2. 运行：

```bash
python3 scripts/fetch_open_access_pdfs.py --download
```

说明：脚本会尽量从 arXiv 获取 PDF；如需对个别条目补充更精确的抓取（OpenReview/作者主页等），建议在 `papers.json` 中把 `query` 写得更具体，或直接手动下载到 `recommended-papers/` 并在对应阅读清单里补上链接。
