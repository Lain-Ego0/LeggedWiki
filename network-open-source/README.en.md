# Web Open-Source Projects

> [中文](README.md) | English

## Scope

This page is the open-source resource index. Complete competition solutions, core drivers, competition resources, and learning knowledge bases belong to the Open Source collection. General theory, tutorials, and methodology remain under `wiki/`, while paper metadata remains under `reading-list/`. Different experiments from the same repository may have separate articles, but each article should identify the related repository.

## 🏆 Complete Competition Solutions

| Institution | Season/Project | Open-Source Repository |
| :--- | :--- | :--- |
| Hubei University of Technology | 2019 Parallel Quadruped HCRT-DOG | [HCRT-DOG](https://github.com/yltzdhbc/HCRT-DOG) |
| Dalian Jiaotong University | 2023 Quadruped Project orthrus-1 | [orthrus-1](https://github.com/evencewu/orthrus-1) |
| Harbin Engineering University | 2024 Electronic Control Framework Corgi_for_ROBOCON | [Corgi_for_ROBOCON](https://github.com/Prcheems/Corgi_for_ROBOCON) |
| Hefei University of Technology | VMC-based Quadruped Project | [VMC-based-QMR](https://github.com/HFUT-YYH/VMC-based-QMR) |
| Fujian University of Technology | 2024 3508 Motor Quadruped Project | [ROBOCON2024-3508DOG](https://github.com/Lain-Ego0/ROBOCON2024-3508DOG) |
| Fujian University of Technology | 2025 8-DOF Serial Mechanism | [ROBOCON2025-8-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-8-DOF-serial) |
| Fujian University of Technology | 2025 12-DOF Serial Mechanism | [ROBOCON2025-12-DOF-serial](https://github.com/Lain-Ego0/ROBOCON2025-12-DOF-serial) |
| Ningbo University of Technology | 2025 VMC Electronic Control Framework | [VMC_Quadruped_Controller](https://github.com/Leader-txt/VMC_Quadruped_Controller) |
| Fujian University of Technology | 2025 Full-Stack Legged Robot Project BRS | [ROBOCON-BRS_robot](https://github.com/Lain-Ego0/ROBOCON-BRS_robot) |

## 🧩 Core Component Drivers

- ZeitVex: Damiao USB-to-CAN, Lingzu motor, and MC02 driver [DM_RS](https://github.com/zeitvex/DM_RS)
- Jinzhong College of Information: MC02 Unitree motor driver [MC02_for_Unitree](https://github.com/Lain-Ego0/MC02_for_Unitree)
- Guilin University of Aerospace Technology: common Damiao H7 motor, remote-control, and chassis libraries [DM02_control](https://github.com/heartpain-kong/DM02_control)

## 🎯 Competition Resources

- Hefei University of Technology: 2026 season competition-field 3D model [26RC_Field](https://github.com/Ruixi-Cheng/26RC_Field)

## 📚 Learning Knowledge Bases

- Fujian University of Technology 2025 full-stack quadruped knowledge base: [Main Knowledge Base](https://wcn9j5638vrr.feishu.cn/wiki/space/7570988375279517715?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)
- Damiao Technology fundamentals of legged robot control: [Legged Robot Control](https://my.feishu.cn/wiki/D88NwctmXieODakf3f1cPWCinfe)
- Damiao Technology deep-RL notes for legged robots: [In-depth Reinforcement Learning Notes](https://my.feishu.cn/wiki/Sn4iwqtREio1llkzJ6Vc9wIwnmf)
- Dalian Jiaotong University reinforcement-learning primer: [A Deep Dive into Reinforcement Learning](https://za8k8pe2ezm.feishu.cn/wiki/N5hFwIrC3isrVckQRRPcx6cHnPs?from=from_parent_docx)

## Project Articles

The project articles are grouped by their primary purpose.

### Paper and Algorithm Reproductions

| Project | Entry | Summary |
| :--- | :--- | :--- |
| [Extreme-RGMT Reproduction](paper-reproductions/extreme-rgmt-reproduction.md) | [Project Page](https://zeonsunlightyu.github.io/Extreme-RGMT.github.io/) | Humanoid whole-body control for highly dynamic skills, including backflips and recovery |
| [SMP Score-Matching Motion Priors](paper-reproductions/smp-score-matching-motion-priors.md) | [GitHub](https://github.com/SUZ-tsinghua/smp) | Uses a frozen diffusion model as a reusable motion reward for Unitree G1 |
| [AMP Go2 Basics](paper-reproductions/amp-go2.md) | [GitHub](https://github.com/ak1raljl/amp_go2) | Go2 AMP training, motion data, Sim2Sim, and Sim2Real workflow |
| [AMP Go2 Stairs Experiment](paper-reproductions/go2-amp-stairs.md) | [GitHub](https://github.com/ak1raljl/amp_go2) | AMP-based Go2 stair-terrain reproduction experiment |
| [M20 DreamWaQ High Platform](paper-reproductions/m20-dreamwaq-highplatform.md) | [GitHub](https://github.com/yusongmin1/Dreamwaq/tree/highplatform) | Curriculum-trained vision-free high-platform climbing for M20 |
| [Go2 Controllable Jump](paper-reproductions/go2-controllable-jump.md) | [GitHub](https://github.com/yusongmin1/My_unitree_go2_gym) | Compares high-acceleration jumping across Isaac Gym, MuJoCo, and hardware |
| [Go2 Flip Data Collection](paper-reproductions/go2-flip-data-collection.md) | [GitHub](https://github.com/yusongmin1/go2_flip_TO) | Generates Go2 flip motions with SE(3) whole-body trajectory optimization |
| [Go2 Trot Gait Control](paper-reproductions/go2-trot-gait-control.md) | [GitHub](https://github.com/yusongmin1/My_unitree_go2_gym) | Controls trot frequency and 10/20 cm foot-clearance settings |
| [Go2 Plum-Blossom Parkour](paper-reproductions/go2-plum-blossom-parkour.md) | [GitHub](https://github.com/jindadu00/legged_robot_competition) | Isaac Gym curriculum-learning experiment for complex terrain |

### Development Tools and Frameworks

| Project | Entry | Summary |
| :--- | :--- | :--- |
| [blender-mujoco-terrain](development-tools/blender-mujoco-hfield.md) | [GitHub](https://github.com/Eterith/blender-mujoco-hfield/tree/main) | Blender exporter for MuJoCo heightfields, meshes, and collision bodies |
| [LeggedGym-Ex](development-tools/leggedgym-ex.md) | [GitHub](https://github.com/lupinjia/LeggedGym-Ex) | Extends legged_gym across Isaac Gym, Genesis, and Isaac Sim |
| [Go2 Depth-Image Parkour](development-tools/go2-depth-parkour.md) | [GitHub](https://github.com/lupinjia/LeggedGym-Ex/tree/main/legged_gym/envs/go2/go2_ts_depth) | Go2 depth-image task example from LeggedGym-Ex |
| [LeggedSkillDeploy](development-tools/leggedskilldeploy.md) | [GitHub](https://github.com/haozhang04/LeggedSkillDeploy) | Deployment framework for multiple legged robots and policy switching |

### Projects and Competition Solutions

| Project | Entry | Summary |
| :--- | :--- | :--- |
| [Engineering Robot and Seven-Axis Dual-Arm Development](projects-and-competition/humanoid-seven-axis-arm-control.md) | [专题入口](https://bbs.robomaster.com/article/1942648?source=1) | Mechanical design, custom controllers, seven-axis control, engineering vision, and the RM2026 vehicle report |
| [RC_WheelLeg](projects-and-competition/rc-wheelleg.md) | [GitHub](https://github.com/zeitvex/RC_WheelLeg) | HYNova wheel-legged robot project with ROS 2 and reinforcement learning |
| [Fuzhou University 12-DOF Quadruped](projects-and-competition/fuzhou-quadruped-robot-lab.md) | [GitHub](https://github.com/Taojunfeng123/quadruped_robot_lab) | RL training code for a 12-DOF point-foot quadruped |
| [Nanhua University HIMLOCO Quadruped](projects-and-competition/nhu-himloco-quadruped.md) | [GitHub](https://github.com/uwvwko-zzz/uw-himloco) | HIMLOCO training framework and himdog deployment code |
| [HIMLoco for Go2W](projects-and-competition/himloco-go2w.md) | [GitHub](https://github.com/TrackinBIT/HIMLoco-for-Go2W) | Go2W Isaac Gym training and MuJoCo verification based on HIMLoco |
| [RoboGauge Go2 Champion Solution](projects-and-competition/robogauge-go2-champion.md) | [Project Page](https://robogauge.github.io/complete/) | Robust locomotion, automated evaluation, and multi-policy deployment for Go2 |

## Supplementary: Robot Hardware Open Source
| Platform | Author/Uploader | Project | Link | One-line Description |
| :--- | :--- | :--- | :--- | :--- |
| Github | michaelkubina | SpotMicroESP32 | [SpotMicroESP32](https://github.com/michaelkubina/SpotMicroESP32) | A classic Spot-like direct-drive servo dog; relatively easy to replicate |
| Github | Huabei Dog King / golaced | MocoMoco_Software | [MocoMoco_Software](https://github.com/golaced/MocoMoco_Software) | Early MocoMoco quadruped open-source software, modified from a flight controller stack |
| Github | Huabei Dog King / golaced | Moco-Minitaur-LTS- | [Moco-Minitaur-LTS-](https://github.com/golaced/Moco-Minitaur-LTS-) | A Minitaur reproduction using Odrive drivers and parallel force control |
| Github | ToanTech | py-apple-bldc-quadruped-robot | [py-apple-bldc-quadruped-robot](https://github.com/ToanTech/py-apple-bldc-quadruped-robot) | A coaxial four-link parallel BLDC quadruped ("Pineapple Dog") |
| Github | ToanTech | py-apple-structure | [py-apple-structure](https://github.com/ToanTech/py-apple-structure) | Mechanical structure for Pineapple Dog |
| Github | ToanTech | py-apple-controller | [py-apple-controller](https://github.com/ToanTech/py-apple-controller) | Control software for Pineapple Dog |
| Github | ToanTech | py-apple-dynamics | [py-apple-dynamics](https://github.com/ToanTech/py-apple-dynamics) | Dynamics/control module for Pineapple Dog |
| Github | Nate711 | StanfordDoggoProject | [StanfordDoggoProject](https://github.com/Nate711/StanfordDoggoProject) | Stanford-style 8-DOF dog with Odrive + belts + shaft sleeves |
| Github | mangdangroboticsclub | QuadrupedRobot | [QuadrupedRobot](https://github.com/mangdangroboticsclub/QuadrupedRobot) | A toy-level quadruped; low replication priority |
| Github | lshil00 | Quadruped_robot | [Quadruped_robot](https://github.com/lshil00/Quadruped_robot) | Well-designed 12-DOF servo quadruped; high completion as a student project |
| Github | XRobots | openDogV3 | [openDogV3](https://github.com/XRobots/openDogV3) | Small BLDC inward-knee-elbow quadruped with interesting design |
| Github | fgrimminger | open_robot_actuator_hardware | [open_robot_actuator_hardware](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware) | Core hardware repository from Open Dynamic Robot Initiative; widely reproduced |
| OSHWHub | 有大饼的魔法少女 | 旺财-仿生四足机器狗 | [旺财-仿生四足机器狗](https://oshwhub.com/gulu666/detector-disaster-scene-3d-reconstruction-robot-dog) | High completion and reasonable design; Xiaomi motors used here are discontinued |
| OSHWHub | hua | 并联臂四足机器狗 | [并联臂四足机器狗](https://oshwhub.com/cdm0302/parallel-arm-quadruped-robot-dog) | Basic five-link servo quadruped; useful when budget is very limited |
| OSHWHub | Forairaaaaa | 基于 ESP-32 的四足机器狗~ | [基于 ESP-32 的四足机器狗~](https://oshwhub.com/eedadada/bakery-zhu-kong-long-gu-zhai-jia) | An integrated simple five-link servo dog, good for practice |
| Gitee | Huabei Dog King / OmniBotLab | Tinymal-Pholcus | [Tinymal-Pholcus](https://gitee.com/tinymal/tinymal-pholcus-t) | 8-DOF parallel layout, typical coaxial five-link; clamp fixation is not ideal |
| Gitee | Huabei Dog King / OmniBotLab | Tinymal-B 四足机器人 | [Tinymal-B 四足机器人](https://gitee.com/tinymal/tinymal-b-quadruped-robot) | A mini-ANYmal style design, but motor torque is somewhat insufficient |
| Gitee | Huabei Dog King / OmniBotLab | Tinymal-Spirit40 | [Tinymal-Spirit40](https://gitee.com/tinymal/tinymal-spirit40-t) | 12-DOF medium-sized all-elbow quadruped using timing belts |
| Gitee | Huabei Dog King / OmniBotLab | OmniBotSeries_Tinker | [OmniBotSeries_Tinker](https://gitee.com/tinymal/omni-bot-series_-tinker) | Ostrich-like biped style, similar to Disney-inspired form |
| Gitee | Huabei Dog King / OmniBotLab | SimpleMan | [SimpleMan](https://gitee.com/tinymal/simple-man-s) | Early rough biped; limited reference value |
| Others | Nathan Kau | Stanford Pupper | [Stanford Pupper](https://pupper.readthedocs.io/en/latest/) | A well-known Stanford servo quadruped |
| Others | 高擎机电 | HTM5046版本四足机器人 | [HTM5046版本四足机器人](https://www.hightorque.cn/category/service) | A commercial quadruped product based on HTM5046 motors |

## Supplementary: Algorithms and Training Frameworks
| Platform | Author/Uploader | Project | Link | One-line Description |
| :--- | :--- | :--- | :--- | :--- |
| Github | fan-ziqi | rl_sar | [rl_sar](https://github.com/fan-ziqi/rl_sar) | A Chinese-built RL framework supporting both simulation and real robot deployment |
| Github | chvmp | champ | [champ](https://github.com/chvmp/champ) | A development framework with a long history |
| Github | real-stanford | umi-on-legs | [umi-on-legs](https://umi-on-legs.github.io/) | A new framework combining real-world and simulated data for quadruped manipulation |
| Github | silvery107 | rl-mpc-locomotion | [rl-mpc-locomotion](https://github.com/silvery107/rl-mpc-locomotion/tree/main) | Training framework combining high-level policy networks and low-level MPC controllers |
| Github | qiayuanl | legged_control | [legged_control](https://github.com/qiayuanl/legged_control) | One of the most portable and high-performing open-source MPC frameworks |
| Github | mit-biomimetics | Cheetah-Software | [Cheetah-Software](https://github.com/mit-biomimetics/Cheetah-Software) | Classic MIT software and algorithm framework |
| Github | robomechanics | quad-sdk | [quad-sdk](https://github.com/robomechanics/quad-sdk) | Extends MIT-style control stack with global trajectory and local foothold planning |
| Github | erwincoumans | motion_imitation | [motion_imitation](https://github.com/erwincoumans/motion_imitation) | Highly readable imitation-learning and MPC controller project |
| Github | ShuoYangRobotics | A1-QP-MPC-Controller | [A1-QP-MPC-Controller](https://github.com/ShuoYangRobotics/A1-QP-MPC-Controller) | MIT-style algorithm implementation on Unitree A1 |
