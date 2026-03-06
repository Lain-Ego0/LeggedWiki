# 🦿 LeggedWiki Legged Robot Resource Repository

<img src="assets/Logo1.png" alt="Introduction to Legged Robot Motion Control Development" width="820" />

> [中文](README.md) | English

LeggedWiki, formerly known as ROBOCON_Legged_Robot, is a one-stop resource repository built for the ROBOCON Bionic Legged Robot Challenge. It is designed for competition preparation, academic research, and development reference, covering the full-stack core resources for legged robot development:

- 📋 Official rule documents of past competitions
- 📢 Technical sharing from participating university teams
- 📄 Recommended papers in the field of legged robotics
- 🔗 Collection of mainstream open-source projects, core components, and learning knowledge bases

---

### 🚀 Quick Navigation
| Module | Direct Access |
| :--- | :--- |
| Competition Rules | [Competition Rules](competition-rules/README.en.md) |
| Technical Sharing | [Technical Sharing](technical-sharing/README.en.md) |
| Recommended Papers | [Local PDFs & index](recommended-papers/README.en.md) |
| Learning & Reading List | [Reading list (entry)](reading-list/README.en.md) |
| Supporting Tool Scripts | [scripts](scripts/README.en.md) |

**Supporting Systematic Tutorial**: [Introductory Knowledge Base for Legged Robot Motion Control Development](https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)

<p align="center">
  <a href="https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home">
    <img src="assets/image.png" alt="Introduction to Legged Robot Motion Control Development" width="820" />
  </a>
</p>

---

### 🏆 Complete Competition Solution Open-Source
| Institution | Season/Project | Open-Source Repository |
| :--- | :--- | :--- |
| Hubei University of Technology | 2019 Parallel Quadruped HCRT-DOG | [HCRT-DOG](https://github.com/yltzdhbc/HCRT-DOG) |
| Dalian Jiaotong University | 2023 Quadruped Project orthrus-1 | [orthrus-1](https://github.com/evencewu/orthrus-1) |
| Harbin Engineering University | 2024 Electronic Control Framework Corgi_for_ROBOCON | [Corgi_for_ROBOCON](https://github.com/Prcheems/Corgi_for_ROBOCON) |
| Hefei University of Technology | VMC-based Quadruped Project | [VMC-based-QMR](https://github.com/HFUT-YYH/VMC-based-QMR) |
| Fujian University of Technology | 2024 3508 Motor Quadruped Project | [ROBOCON2024-3508DOG](https://github.com/Lain-Ego0/ROBOCON2024-3508DOG) |
| Fujian University of Technology | 2025 8-DOF Serial Mechanism Open-Source | [ROBOCON2025-8-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-8-DOF-serial) |
| Fujian University of Technology | 2025 12-DOF Serial Mechanism Open-Source | [ROBOCON2025-12-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-12-DOF-serial) |
| Ningbo University of Technology | 2025 VMC Electronic Control Framework | [VMC_Quadruped_Controller](https://github.com/Leader-txt/VMC_Quadruped_Controller) |
| Fujian University of Technology | 2025 Full-Stack Legged Robot Project BRS | [ROBOCON-BRS_robot](https://github.com/Lain-Ego0/ROBOCON-BRS_robot) |

### 🧩 Core Component & Driver Open-Source
- Shiwei Technology: Damiao USB to CAN / Lingzu Motor + MC02 Driver [DM_RS](https://github.com/zeitvex/DM_RS)
- Jinzhong College of Information: MC02 Unitree Motor Driver [MC02_for_Unitree](https://github.com/Lain-Ego0/MC02_for_Unitree)
- Guilin University of Aerospace Technology: Lingzu Motor Keil Driver Package [RobStride-motorDrive](https://github.com/heartpain-kong/RobStride-motorDrive)

### 🎯 Competition Task Functional Open-Source
- Hefei University of Technology: 2026 Season Competition Venue 3D Model [26RC_Field](https://github.com/Ruixi-Cheng/26RC_Field)

### 📚 Learning Knowledge Base
- Fujian University of Technology 2025 Full-Stack Quadruped Robot Open-Source Knowledge Base: [Main Knowledge Base](https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)
- Damiao Technology Basic Knowledge Base for Legged Robot Control: [Legged Robot Control](https://my.feishu.cn/wiki/D88NwctmXieODakf3f1cPWCinfe)
- Damiao Technology In-depth Reinforcement Learning Notes for Legged Robots: [In-depth Reinforcement Learning Notes for Legged Robots](https://my.feishu.cn/wiki/Sn4iwqtREio1llkzJ6Vc9wIwnmf)
- Dalian Jiaotong University Quick Start Knowledge Base for Reinforcement Learning: [A Deep Dive into Reinforcement Learning](https://za8k8pe2ezm.feishu.cn/wiki/N5hFwIrC3isrVckQRRPcx6cHnPs?from=from_parent_docx)

---

## 🤝 Contribution Guidelines
We welcome all developers and participating teams to improve this repository. Contribution methods are as follows:
1. **Add New Materials**: Place files in the corresponding directories `competition-rules/`, `technical-sharing/`, `recommended-papers/` by content type. File names should include key information such as "edition/year/theme/version" for easy retrieval.
2. **Add New External Links**: Prioritize official/original author open-source addresses, clearly mark the project purpose and affiliated institution to ensure traceable information.
3. **Update Reading List**: Prioritize maintaining paper entries in `reading-list/papers.json`, then run `python3 scripts/fetch_open_access_pdfs.py --download` to fetch open-source PDF files.
4. **Large File Handling**: For single files exceeding ~100MB, please use Git LFS for management or replace them with compliant external links.

---

## ⚠️ Disclaimer
1. This repository is only for non-commercial learning exchange and resource indexing. The copyright and attribution of all materials belong to the original authors and publishers.
2. If any content in this repository involves infringement, improper disclosure, or other issues, please contact the repository maintainer via Issue or direct message. We will verify and process it as soon as possible.
