# 🦿 LocoWiki 机器人运控资料库

<img src="assets/LOGO-LocoWiki1-cut.jpg" alt="足式机器人运控开发入门" width="820" />

项目网站：https://locowiki.github.io/

> 中文 | [English](README.en.md)

LocoWiki 原名 ROBOCON_Legged_Robot，是面向机器人运动控制学习与实践的开放资料索引，服务于比赛备赛、科研学习和工程开发检索。仓库按主题整理足式机器人领域的公开资源：

- 📋 历届赛事官方规则文档
- 📢 高校参赛队伍技术分享
- 📄 论文学习清单（论文元数据、笔记与原始来源链接；不保存论文 PDF）
- 🔗 主流开源项目、核心组件与学习知识库汇总

仓库以 Markdown 为主要内容格式，资料尽量链接到官方页面、作者主页、开放获取平台或原始开源仓库，方便溯源和持续维护。

**配套系统讲解**：[机器人运控开发飞书知识库](<https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home>)

<p align="center">
  <a href="https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home">
    <img src="assets/image.png" alt="机器人运控开发入门" width="820" />
  </a>
</p>

---

### 🚀 快速导航
| 模块 | 直达入口 |
| :--- | :--- |
| 赛事规则 | [比赛规则](competition-rules/README.md)|
| 网络开源 | [网络开源](network-open-source/README.md)|
| 技术分享 | [技术分享](technical-sharing/README.md) |
| 论文学习清单 | [阅读清单（论文索引与原文链接）](reading-list/README.md) |
| 系统化教程 | [Wiki 教程](wiki/) |
| 配套工具脚本 | [scripts](scripts/README.md)|

---

### 🏆 完整参赛方案开源
| 所属高校 | 赛季/项目 | 开源仓库地址 |
| :--- | :--- | :--- |
| 湖北工业大学 | 2019 并联四足 HCRT-DOG | [HCRT-DOG](https://github.com/yltzdhbc/HCRT-DOG) |
| 大连交通大学 | 2023 四足项目 orthrus-1 | [orthrus-1](https://github.com/evencewu/orthrus-1) |
| 哈尔滨工程大学 | 2024 电控框架 Corgi_for_ROBOCON | [Corgi_for_ROBOCON](https://github.com/Prcheems/Corgi_for_ROBOCON) |
| 合肥工业大学 | 基于VMC的四足项目 | [VMC-based-QMR](https://github.com/HFUT-YYH/VMC-based-QMR) |
| 福建理工大学 | 2024 3508电机四足项目 | [ROBOCON2024-3508DOG](https://github.com/Lain-Ego0/ROBOCON2024-3508DOG) |
| 福建理工大学 | 2025 8自由度串联机械开源 | [ROBOCON2025-8-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-8-DOF-serial) |
| 福建理工大学 | 2025 12自由度串联机械开源 | [ROBOCON2025-12-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-12-DOF-serial) |
| 宁波工程学院 | 2025 VMC电控框架 | [VMC_Quadruped_Controller](https://github.com/Leader-txt/VMC_Quadruped_Controller) |
| 福建理工大学 | 2025 全栈足式机器人项目 BRS | [ROBOCON-BRS_robot](https://github.com/Lain-Ego0/ROBOCON-BRS_robot) |

### 🧩 核心组件驱动开源
- 时维科技：达妙USB转CAN/灵足电机+MC02驱动 [DM_RS](https://github.com/zeitvex/DM_RS)
- 晋中信息学院：MC02 宇树电机驱动 [MC02_for_Unitree](https://github.com/Lain-Ego0/MC02_for_Unitree)
- 桂林航天工业学院：基于达妙H7中常用开源,包括宇树+DMA、灵足、达妙、大疆的电机驱动库、大疆遥控器和底盘控制 [DM02_control](https://github.com/heartpain-kong/DM02_control)

### 🎯 赛题功能性开源
- 合肥工业大学：2026赛季赛事场地三维模型 [26RC_Field](https://github.com/Ruixi-Cheng/26RC_Field)

### 📚 学习知识库
- 福建理工大学 2025 四足机器人全栈开源知识库：[总知识库](https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)
- 达妙科技 足式机器人控制基础知识库：[足式机器人控制](https://my.feishu.cn/wiki/D88NwctmXieODakf3f1cPWCinfe)
- 达妙科技 足式机器人强化学习深度笔记：[足式深度强化学习笔记](https://my.feishu.cn/wiki/Sn4iwqtREio1llkzJ6Vc9wIwnmf)
- 大连交通大学 强化学习快速入门知识库：[深入浅出强化学习](https://za8k8pe2ezm.feishu.cn/wiki/N5hFwIrC3isrVckQRRPcx6cHnPs?from=from_parent_docx)

---

## 🤝 贡献指南
欢迎各位开发者、参赛队伍一起完善本仓库，贡献方式如下：
1. **新增资料**：按内容分类放入 `competition-rules/`、`technical-sharing/` 或 `wiki/` 对应目录；提交前确认资料可以公开分享。
2. **新增外链**：优先使用官方页面、原作者页面、开放获取平台和原始开源仓库，并标注项目用途与所属单位，保证信息可溯源。
3. **更新论文清单**：在 `reading-list/papers.json` 中维护论文元数据和来源链接，再执行 `python3 scripts/resolve_paper_links.py --update-index` 更新索引。仓库不上传论文 PDF 镜像。
4. **保护隐私与安全**：不要提交访问令牌、密码、私钥、个人联系方式、未公开数据或本地绝对路径；示例配置应使用占位符。
5. **大文件处理**：单个文件较大时，优先使用合规外链或 Git LFS，并确认其版权和分发许可。

### 内容与网站

本仓库是资料内容源，配套网站负责展示和检索。资料目录与网站栏目的对应关系见 [内容目录与站点边界](CONTENT_STRUCTURE.md)。Markdown 内容更新后，网站会收到更新通知并刷新文档索引；网站运行时仍从本仓库读取对应文档。索引只记录网站栏目允许展示的公开 Markdown 路径，不包含访问凭据。

---

## ⚠️ 免责声明
1. 本仓库仅用于非商业的学习交流与资料索引，所有资料的版权、署名权均归原作者、原发布方所有。
2. 若仓库内任何内容存在侵权、不当公开或其他问题，请通过 Issue 或直接联系仓库维护者，我们将第一时间核实并处理。
