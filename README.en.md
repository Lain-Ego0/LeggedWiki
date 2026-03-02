# ROBOCON-Legged-Robot Resource Collection

[中文（默认）](README.md) | English

This repository curates ROBOCON-related resources (e.g., Robot Equestrian / Bio-inspired Legged Robot Challenge): rulebooks, tech-sharing slides, a paper library, and links to commonly referenced open-source projects/components/knowledge bases.

## Contents
- [Directory Layout](#directory-layout)
- [Local Resources](#local-resources)
  - [Competition Rules](#competition-rules)
  - [Tech Sharing](#tech-sharing)
  - [Papers](#papers)
  - [Reading List](#reading-list)
- [External Links](#external-links)
  - [Full Projects](#full-projects)
  - [Components](#components)
  - [Challenge-Specific Repos](#challenge-specific-repos)
  - [Knowledge Bases](#knowledge-bases)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## Directory Layout

```
.
├── README.md          # Chinese (default)
├── README.en.md       # English
├── 阅读清单/           # Reading list + notes (Chinese)
├── scripts/            # Fetch/organize scripts
├── 比赛规则/           # Rulebooks (PDF)
├── 技术分享/           # Slides (PPTX, etc.)
└── 推荐论文/           # Paper PDFs + index
```

## Local Resources

### Competition Rules
- Folder: [比赛规则/](<比赛规则/>)
- PDFs:
  - [第二十一届全国大学生机器人大赛ROBOCON机器马术赛规则（20211220修订）](<比赛规则/第二十一届全国大学生机器人大赛ROBOCON机器马术赛规则（20211220修订）.pdf>)
  - [第二十二届全国大学生机器人大赛-机器马术赛规则（拟发布稿V2）](<比赛规则/第二十二届全国大学生机器人大赛-机器马术赛规则（拟发布稿V2）.pdf>)
  - [第二十三届全国大学生机器人大赛 ROBOCON仿生足式机器人挑战赛比赛规则手册](<比赛规则/第二十三届全国大学生机器人大赛 ROBOCON仿生足式机器人挑战赛比赛规则手册.pdf>)
  - [第二十四届全国大学生机器人大赛“仿生足式机器人挑战赛”规则-V1.0](<比赛规则/第二十四届全国大学生机器人大赛“仿生足式机器人挑战赛”规则-V1.0.pdf>)
  - [第二十四届全国大学生机器人大赛“仿生足式机器人挑战赛”规则-V2.0](<比赛规则/第二十四届全国大学生机器人大赛“仿生足式机器人挑战赛”规则-V2.0.pdf>)

### Tech Sharing
- Folder: [技术分享/](<技术分享/>)
- Slides:
  - [2023大连工业大学马术分享](<技术分享/2023大连工业大学马术分享.pptx>)
  - [2026年会 福建理工 从赛事到“具身”？足式机器人杂谈](<技术分享/2026年会 福建理工 从赛事到“具身”？足式机器人杂谈.pptx>)

### Papers
- Paper library index: [推荐论文/README.md](<推荐论文/README.md>)
- Local PDFs are organized under:
  - `推荐论文/ETH-RSL/`, `推荐论文/KAIST/`, `推荐论文/其他/`, `推荐论文/人形/`, `推荐论文/综述/`

### Reading List
- Reading list (with notes, mainly Chinese): [阅读清单/README.md](<阅读清单/README.md>)

## External Links

### Full Projects
- HCRT-DOG (HUT 2019): https://github.com/yltzdhbc/HCRT-DOG
- orthrus-1 (DJTU 2023): https://github.com/evencewu/orthrus-1
- Corgi_for_ROBOCON (HIT 2024, control framework): https://github.com/Prcheems/Corgi_for_ROBOCON
- VMC-based-QMR (HFUT): https://github.com/HFUT-YYH/VMC-based-QMR
- ROBOCON2024-3508DOG (FJUT 2024): https://github.com/Lain-Ego0/ROBOCON2024-3508DOG
- ROBOCON2025-8-DOF-serial (FJUT 2025, mech, 8 DoF serial): https://github.com/Lain-Ego0/ROBOCON2025-8-DOF-serial
- ROBOCON2025-12-DOF-serial (FJUT 2025, mech, 12 DoF serial): https://github.com/Lain-Ego0/ROBOCON2025-12-DOF-serial
- VMC_Quadruped_Controller (NBU 2025, control framework): https://github.com/Leader-txt/VMC_Quadruped_Controller
- ROBOCON-BRS_robot (FJUT 2025): https://github.com/Lain-Ego0/ROBOCON-BRS_robot

### Components
- DM_RS (USB-to-CAN + RobStride/MC02 related): https://github.com/zeitvex/DM_RS
- MC02_for_Unitree (MC02 Unitree driver): https://github.com/Lain-Ego0/MC02_for_Unitree
- RobStride-motorDrive: https://github.com/heartpain-kong/RobStride-motorDrive

### Challenge-Specific Repos
- 26RC_Field: https://github.com/Ruixi-Cheng/26RC_Field

### Knowledge Bases
- FJUT 2025 legged robotics wiki: https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home
- DAMIAO legged robotics control wiki: https://my.feishu.cn/wiki/D88NwctmXieODakf3f1cPWCinfe
- DAMIAO deep RL notes: https://my.feishu.cn/wiki/Sn4iwqtREio1llkzJ6Vc9wIwnmf
- RL intro wiki (DJTU): https://za8k8pe2ezm.feishu.cn/wiki/N5hFwIrC3isrVckQRRPcx6cHnPs?from=from_parent_docx

## Contributing
- Add files into `比赛规则/`, `技术分享/`, `推荐论文/` with informative filenames (year/edition/topic/version).
- For the reading list: update `阅读清单/papers.json`, then run:

```bash
python3 scripts/fetch_open_access_pdfs.py --download
```

- Large files: consider Git LFS or external links to avoid bloating the repo.

## Disclaimer
- This repository is for learning and indexing only. Copyright belongs to the original authors/publishers.
- If any material should not be publicly shared, please open an issue or contact the maintainer for removal.

