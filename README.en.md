# 🦿 LocoWiki Legged Robot Motion Control Wiki Repository

<img src="assets/LOGO-LocoWiki1-cut.jpg" alt="Introduction to Legged Robot Motion Control Development" width="820" />

Project website: https://locowiki.github.io/

> [中文](README.md) | English

LocoWiki, formerly known as ROBOCON_Legged_Robot, is a one-stop resource repository built for robot motion control learning. It serves competition preparation, research study, and development lookup scenarios, and covers core full-pipeline resources for legged robot development:

- 📋 Official rule documents from past competitions
- 📢 Technical sharing from university competition teams
- 📄 Paper study list (reading list + recommended paper PDFs)
- 🔗 Curated mainstream open-source projects, core components, and learning knowledge bases

**Supporting System Tutorial**: [Knowledge Base for Robot Motion Control Development](<https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home>)

<p align="center">
  <a href="https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home">
    <img src="assets/image.png" alt="Introduction to Legged Robot Motion Control Development" width="820" />
  </a>
</p>

---

### 🚀 Quick Navigation
| Module | Direct Entry |
| :--- | :--- |
| Competition Rules | [Competition Rules](competition-rules/README.en.md) |
| Network Open Source | [Network Open Source](network-open-source/README.en.md) |
| Technical Sharing | [Technical Sharing](technical-sharing/README.en.md) |
| Paper Study List | [Reading list (with recommended papers and local PDFs)](reading-list/README.en.md) |
| Supporting Tool Scripts | [scripts](scripts/README.en.md) |

---

### 🏆 Complete Competition Solution Open Source
| Institution | Season/Project | Open-Source Repository |
| :--- | :--- | :--- |
| Hubei University of Technology | 2019 Parallel Quadruped HCRT-DOG | [HCRT-DOG](https://github.com/yltzdhbc/HCRT-DOG) |
| Dalian Jiaotong University | 2023 Quadruped Project orthrus-1 | [orthrus-1](https://github.com/evencewu/orthrus-1) |
| Harbin Engineering University | 2024 Electronic Control Framework Corgi_for_ROBOCON | [Corgi_for_ROBOCON](https://github.com/Prcheems/Corgi_for_ROBOCON) |
| Hefei University of Technology | VMC-based Quadruped Project | [VMC-based-QMR](https://github.com/HFUT-YYH/VMC-based-QMR) |
| Fujian University of Technology | 2024 3508 Motor Quadruped Project | [ROBOCON2024-3508DOG](https://github.com/Lain-Ego0/ROBOCON2024-3508DOG) |
| Fujian University of Technology | 2025 8-DOF Serial Mechanism Open Source | [ROBOCON2025-8-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-8-DOF-serial) |
| Fujian University of Technology | 2025 12-DOF Serial Mechanism Open Source | [ROBOCON2025-12-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-12-DOF-serial) |
| Ningbo University of Technology | 2025 VMC Electronic Control Framework | [VMC_Quadruped_Controller](https://github.com/Leader-txt/VMC_Quadruped_Controller) |
| Fujian University of Technology | 2025 Full-Stack Legged Robot Project BRS | [ROBOCON-BRS_robot](https://github.com/Lain-Ego0/ROBOCON-BRS_robot) |

### 🧩 Core Component Driver Open Source
- ZeitVex: Damiao USB-to-CAN / Lingzu Motor + MC02 Driver [DM_RS](https://github.com/zeitvex/DM_RS)
- Jinzhong College of Information: MC02 Unitree Motor Driver [MC02_for_Unitree](https://github.com/Lain-Ego0/MC02_for_Unitree)
- Guilin University of Aerospace Technology: Damiao 02 motor driver with support for Unitree (DMA), Lingzu, DJI, Damiao motors,and DJI Remote Controller Routine[DM02-motorDrive](https://github.com/heartpain-kong/DM02_motorDrive)

### 🎯 Competition Task Functionality Open Source
- Hefei University of Technology: 2026 season competition field 3D model [26RC_Field](https://github.com/Ruixi-Cheng/26RC_Field)

### 📚 Learning Knowledge Bases
- Fujian University of Technology 2025 full-stack quadruped robot open-source knowledge base: [Main Knowledge Base](https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)
- Damiao Technology fundamental knowledge base for legged robot control: [Legged Robot Control](https://my.feishu.cn/wiki/D88NwctmXieODakf3f1cPWCinfe)
- Damiao Technology in-depth notes on reinforcement learning for legged robots: [In-depth Reinforcement Learning Notes](https://my.feishu.cn/wiki/Sn4iwqtREio1llkzJ6Vc9wIwnmf)
- Dalian Jiaotong University quick-start knowledge base for reinforcement learning: [A Deep Dive into Reinforcement Learning](https://za8k8pe2ezm.feishu.cn/wiki/N5hFwIrC3isrVckQRRPcx6cHnPs?from=from_parent_docx)

---

## 🤝 Contribution Guidelines
We welcome developers and competition teams to improve this repository together. Contribution methods are:
1. **Add New Materials**: Place files by content type in `competition-rules/`, `technical-sharing/`, and `recommended-papers/`. For new paper entries, also update index information in `reading-list/README.en.md` or `reading-list/papers.json` for easier search.
2. **Add New External Links**: Prioritize official or original-author open-source repository links. Clearly label the project purpose and institution affiliation to keep information traceable.
3. **Update the Paper List**: Maintain paper entries in `reading-list/papers.json`, then run `python3 scripts/fetch_open_access_pdfs.py --download` to fetch open-access PDF files.
4. **Large File Handling**: For single files larger than ~100MB, use Git LFS, or replace them with compliant external links.

---

## ⚠️ Disclaimer
1. This repository is for non-commercial learning exchange and resource indexing only. Copyright and attribution rights for all materials belong to the original authors and publishers.
2. If any content in this repository involves infringement, improper disclosure, or other issues, please contact the repository maintainers via Issues or direct message. We will verify and handle it as soon as possible.
