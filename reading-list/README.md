# 阅读清单（RL 运控 / 足式 / 人形）

> 中文 | [English](README.en.md)

本目录整理足式 / 人形等方向的代表论文，并尽可能在 `recommended-papers/` 中提供 **可公开获取** 的 PDF（优先 arXiv 预印本）。若某些期刊/会议论文未找到公开 PDF，会保留引用与获取建议。

## 快速跳转
- [如何更新/抓取](#update)
- [按技术方向索引（快速查找）](#tech-index)
- [按来源/团队笔记（详细介绍）](#source-notes)
  - [ETH RSL](#eth-rsl)
  - [KAIST](#kaist)
  - [其他代表作](#other-works)
  - [人形](#humanoids)
  - [综述](#surveys)
  - [其他资料（暂无笔记）](#misc)

<a id="update" name="update"></a>
## 如何更新/抓取
1. 在 `reading-list/papers.json` 新增/更新条目（title / venue / year / notes / group）。
2. 运行：

```bash
python3 scripts/fetch_open_access_pdfs.py --download
```

说明：脚本会尽量从 arXiv 获取 PDF；如需对个别条目补充更精确的抓取（OpenReview/作者主页等），建议在 `papers.json` 中把 `query` 写得更具体，或直接手动下载到 `recommended-papers/` 并在对应阅读清单里补上链接。

<a id="tech-index" name="tech-index"></a>
## 按技术方向索引（快速查找）
注：下方为快速索引；若某条目有笔记/简介，详见同文件后半部分「按来源/团队笔记（详细介绍）」。

### 综述 / 教材
- Learning-based legged locomotion: State of the art and future perspectives（IJRR 2025）— [PDF](<../recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf>)
- Robot Dynamics Lecture Notes（2017）— [PDF](<../recommended-papers/ETH-RSL/2017 - Robot Dynamics Lecture Notes.pdf>)

### 模型驱动控制 / 轨迹优化
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [PDF](<../recommended-papers/MIT/Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control.pdf>)
- DTC: Deep Tracking Control（Science Robotics 2024）— [PDF](<../recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- [中文] 基于虚拟模型的四足机器人对角小跑步态控制方法 — [PDF](<../recommended-papers/chinese/基于虚拟模型的四足机器人对角小跑步态控制方法.pdf>)
- [中文] 仿生四足机器人多步态规划与控制 — [PDF](<../recommended-papers/chinese/仿生四足机器人多步态规划与控制.pdf>)
- [中文] 基于稳定性的仿生四足机器人控制系统设计（于宪元）— [PDF](<../recommended-papers/chinese/SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计.pdf>)

### 学习运控（本体感知为主）
#### 四足
- Learning agile and dynamic motor skills for legged robots（Science Robotics 2019）— [PDF](<../recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- Learning Quadrupedal Locomotion over Challenging Terrain（Science Robotics 2020）— [PDF](<../recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning（CoRL 2021）— [PDF](<../recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion（RAL 2022）— [PDF](<../recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning（ICRA 2023）— [PDF](<../recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- Learning Quadrupedal Locomotion on Deformable Terrain（Science Robotics 2023）— 暂无公开 PDF（可优先尝试作者预印本/公开版）
- Rapid Locomotion via Reinforcement Learning（RSS 2022）— [PDF](<../recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf>)

#### 双足
- Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition（ICRA 2021）— [PDF](<../recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf>)

### Sim-to-Real / 适应
- Sim-to-Real: Learning Agile Locomotion for Quadruped Robots（2018）— [PDF](<../recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf>)
- RMA: Rapid Motor Adaptation for Legged Robots（RSS 2021）— [PDF](<../recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf>)

### 感知 / 建图
- Learning robust perceptive locomotion for quadrupedal robots in the wild（Science Robotics 2022）— [PDF](<../recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- Elevation Mapping for Locomotion and Navigation using GPU（IROS 2022）— [PDF](<../recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)

### 运动先验 / 模仿学习 / 风格奖励 / 生成模型
- Learning Agile Robotic Locomotion Skills by Imitating Animals（RSS 2020）— [PDF](<../recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf>)
- Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations — [PDF](<../recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf>)
- AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control（SIGGRAPH 2021）— [PDF](<../recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf>)
- Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions（ICRA 2022）— [PDF](<../recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf>)
- Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning（ICRA 2023）— [PDF](<../recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior（CoRL 2022）— [PDF](<../recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf>)
- A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards（ICRA 2025）— [PDF](<../recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild（RAL 2023）— [PDF](<../recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf>)
- Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models（Nature Machine Intelligence 2023）— [PDF](<../recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf>)

### 跑酷 / 离散地形 / 高动态
- Learning Agile Locomotion on Risky Terrains（IROS 2024）— [PDF](<../recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots（Science Robotics 2024）— [PDF](<../recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- Extreme Parkour with Legged Robots（ICRA 2024）— [PDF](<../recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf>)
- Robot Parkour Learning（CoRL 2024）— [PDF](<../recommended-papers/other/2024 - Robot Parkour Learning.pdf>)
- PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots（RAL 2024）— [PDF](<../recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf>)
- [中文] 四足机器人跳跃步态主动柔顺控制研究 — [PDF](<../recommended-papers/chinese/四足机器人跳跃步态主动柔顺控制研究.pdf>)

### Loco-manipulation / Whole-body
- Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion（CoRL 2022）— [PDF](<../recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf>)
- Visual Whole-Body Control for Legged Loco-Manipulation（CoRL 2024）— [PDF](<../recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf>)
- Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks（CoRL 2023）— 暂无公开 PDF（可优先尝试 OpenReview/作者主页）

### 人形（Whole-Body / Teleop / Getting-Up / 生成）
- Expressive Whole-Body Control for Humanoid Robots（RSS 2024）— [PDF](<../recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf>)
- ExBody2: Advanced Expressive Humanoid Whole-Body Control（2024）— [PDF](<../recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf>)
- Open-TeleVision: Teleoperation with Immersive Active Visual Feedback（CoRL 2024）— [PDF](<../recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf>)
- Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control（2024）— [PDF](<../recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf>)
- HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots（ICRA 2025）— [PDF](<../recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf>)
- HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion（2025）— [PDF](<../recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf>)
- Learning Humanoid Standing-up Control across Diverse Postures（RSS 2025）— [PDF](<../recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf>)
- Learning Getting-Up Policies for Real-World Humanoid Robots（RSS 2025）— [PDF](<../recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf>)
- BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion（2025）— [PDF](<../recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf>)

### 硬件 / 机构
- A Low Cost Modular Actuator for Dynamic Robots — [PDF](<../recommended-papers/MIT/MIT - A Low Cost Modular Actuator for Dynamic Robots.pdf>)
- [中文] 新型电驱式四足机器人研制与测试（王兴兴）— [PDF](<../recommended-papers/chinese/新型电驱式四足机器人研制与测试-王兴兴.pdf>)

### Others
- [中文] 四足机器人随笔 — [PDF](<../recommended-papers/chinese/四足机器人随笔.pdf>)

<a id="source-notes" name="source-notes"></a>
## 按来源/团队笔记（详细介绍）

<a id="eth-rsl" name="eth-rsl"></a>
### ETH Robotics Systems Lab（RSL）

#### Learning Agile and Dynamic Motor Skills for Legged Robots（Science Robotics 2019）
- PDF： [recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf](<../recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- 笔记：强化学习四足运控的奠基之作：用真实数据训练电机网络模型，并在仿真中进行补偿，结合 RL + dynamics randomization 训练策略；成功部署到 ANYmal，实现鲁棒 locomotion（速度跟踪、跌倒恢复等）。

#### Learning Quadrupedal Locomotion over Challenging Terrain（Science Robotics 2020）
- PDF： [recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf](<../recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- 笔记：首次提出两阶段教师-学生框架：教师策略利用模拟器里的“作弊信息”学习到好的运动策略，再通过在线模仿学习（DAgger）蒸馏给可部署（仅使用历史可观测数据）的学生策略（引入 encoder 估计隐式作弊信息）。同时提出地形课程，实现鲁棒的复杂连续地形行走。该阶段控制栈仍较复杂：网络用于辅助足端轨迹生成，还需 IK 求解得到最终 target joints；而后续主流更倾向策略直接输出 target joints。

#### Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning（CoRL 2021）
- PDF： [recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf](<../recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- 笔记：里程碑工作：推动 RL + Robotics 的后续发展。开发并验证 Isaac Gym 大规模并行训练 + domain randomization 的强化学习运控方案，并开源 `legged_gym` 项目。

#### Learning robust perceptive locomotion for quadrupedal robots in the wild（Science Robotics 2022）
- PDF： [recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf](<../recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- 笔记：集成本体感知与外部视觉信号的鲁棒 locomotion 策略，实现大规模户外甚至极端条件行走（楼梯、隧道、雪山、浓雾、森林、碎岩等）。给出了学习“带外感知策略”（估计高程图）的范例。

#### Elevation Mapping for Locomotion and Navigation using GPU（IROS 2022）
- PDF： [recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf](<../recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)
- 笔记：提出利用 GPU 高效构建高程图的方法：接收外部传感器点云与机器人位姿信息，快速构建周围地形高程图；复杂环境中里程计漂移仍是实时建图的最大挑战之一。代码已开源。

#### Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning（ICRA 2023）
- PDF： [recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf](<../recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- 笔记：增强版 AMP：允许多种可离散切换的风格，在轮腿四足机器人上展示躲避、行走，以及四足与双足模式（站立）之间的风格切换；其中从“反向站立（双足）序列”学习“趴下（四足）”的案例较有意思。

#### Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks（CoRL 2023）
- PDF：暂未找到可公开抓取的 PDF（可能在 OpenReview/作者主页）。
- 笔记：亮点：用轮腿四足学习把腿当作 manipulator 的 loco-manipulation 策略。

#### Learning Agile Locomotion on Risky Terrains（IROS 2024）
- PDF： [recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf](<../recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- 笔记：（@XueYeiii）有意思的工作之一：可能是较早的基于 RL 运控走离散地形的工作（虽非全向行走），demo 效果不错。

#### ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots（Science Robotics 2024）
- PDF： [recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf](<../recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- 笔记：多层级框架：感知模块重建环境信息，导航模块根据环境信息导航并驱动运动模块选择能力；运动模块具备跑酷基本技能。首篇实现四足动态跑酷的工作之一。

#### DTC: Deep Tracking Control（Science Robotics 2024）
- PDF： [recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf](<../recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- 笔记：结合 Model-based 与 Learning-based：上层 TO 根据环境与动力学实时优化机身轨迹与足端轨迹；底层 RL 严格跟踪优化轨迹，实现极端地形的精确运动（梅花桩、深沟、废墟等）。相较只做机身速度跟踪的方法，该分层框架更有利于落足点选择。

<a id="kaist" name="kaist"></a>
### KAIST（Raibo / Unitree 等）

#### Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion（RAL 2022）
- PDF： [recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf](<../recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- 笔记：一阶段非对称学习（非教师-学生）：策略网络联合训练关键状态估计器（线速度、足端高度、触地概率，输入为历史可观测数据）；仿真中 critic 直接使用关键状态真值，并引入 dynamics randomization，使用 PPO 训练后可部署并穿越多样连续复杂地形。

#### DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning（ICRA 2023）
- PDF： [recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf](<../recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- 笔记：非对称强化学习结构：状态估计器从可观测信息中估计速度与隐式地形信息 z，z 通过 VAE 学习。在宇树 A1 上实现鲁棒的长距离多样户外地形行走，说明非对称 actor-critic 训练框架可在复杂环境获得很强的运动能力。

#### Learning Quadrupedal Locomotion on Deformable Terrain（Science Robotics 2023）
- PDF：暂未找到可公开抓取的 PDF（可能为期刊付费版；可优先找作者公开版/预印本）。
- 笔记：针对模拟器多为刚性接触动力学，修改 RaiSim 底层接触模型，建模颗粒介质（granular media）接触动力学，实现 Raibo 在沙滩/海绵垫等松软地形的敏捷与鲁棒运动；采用非对称训练框架，进一步验证其有效性。

#### A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards（ICRA 2025）
- PDF： [recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf](<../recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- 笔记：引入松弛对数障碍函数，设计基于运动模式特征的软约束奖励机制，引导机器人趋向预设运动形态参数（周期步态、关节范围限制等）。未使用运动先验也生成多种仿生四足步态，其中四足站立的“仿人行走”与 gallop 奔跑步态令人印象深刻。

<a id="other-works" name="other-works"></a>
### 其他代表作（四足/双足/通用）

#### 四足 / 足式

##### Sim-to-Real: Learning Agile Locomotion for Quadruped Robots（Minitaur）
- PDF： [recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf](<../recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf>)
- 笔记：较早的四足 sim2real 工作：RL + analytical 解析式电机模型 + dynamics randomization，基于 Ghost Robotics 的 Minitaur，启发了 ETH ANYmal 系列。

##### Learning Agile Robotic Locomotion Skills by Imitating Animals（RSS 2020）
- PDF： [recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf](<../recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf>)
- 笔记：在宇树早期的 Laikago 平台上，基于 motion retargeting + DeepMimic 的 motion tracking 方案，学习动物自然风格运动行为。代码已开源（UCB）。

##### RMA: Rapid Motor Adaptation for Legged Robots（RSS 2021）
- PDF： [recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf](<../recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf>)
- 笔记：Teacher-student + adaptation module（类似 ETH 的 encoder），随机采样地形 + domain randomization + RaiSim 并行训练，在宇树 A1 上实现无外感知的复杂连续地形穿越。代码已开源（CMU）。

##### Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior（CoRL 2022）
- PDF： [recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf](<../recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf>)
- 笔记：在宇树 Go1 上实现可细粒度调参的鲁棒 locomotion：速度、步态（pronking/trotting/bounding/pacing/galloping）、步频、机身高度、俯仰角、触地时间、抬腿高度等。代码已开源（MIT）。

##### Rapid Locomotion via Reinforcement Learning（RSS 2022）
- PDF： [recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf](<../recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf>)
- 笔记：提出速度网格自适应采样课程，自动挖掘速度上限，减少手工速度课程与专家知识干预。代码已开源（MIT）。

##### Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions（ICRA 2022）
- PDF： [recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf](<../recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf>)
- 笔记：首次将 AMP 应用于四足：仅任务奖励 + 风格奖励学习自然运动行为，推动后续四足模仿学习运控研究。代码已开源（UCB）。

##### Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion（CoRL 2022）
- PDF： [recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf](<../recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf>)
- 笔记：在宇树 Go1 + WidowX 机械臂上验证 RL 运控实现臂-腿协同（基于遥操作），并提出 ROA 将环境隐变量 z 的两阶段估计改为一阶段在线估计；基于 Isaac Gym + rsl_rl 开发，代码已开源（CMU）。

##### Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild（RAL 2023）
- PDF： [recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf](<../recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf>)
- 笔记：教师-学生框架 + AMP：仅本体感知即可在宇树 Go1 上实现鲁棒复杂连续地形行走；自然步态数据用轨迹优化在平地生成。注：期刊标题为 “Learning robust and Agile Legged Locomotion Using Adversarial Motion Priors”（SJTU）。

##### Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models（Nature Machine Intelligence 2023）
- PDF： [recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf](<../recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf>)
- 笔记：利用生成模型：先在预训练阶段学习动物大规模运动数据，再在环境交互学习阶段复用技能；腾讯 Robotics X 代表作。

##### Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations
- PDF： [recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf](<../recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf>)
- 笔记：从不完整动作演示中学习四足动态运动：数据来自人为手工操作机器人收集，在低成本机器人上实现后空翻动作。

##### Extreme Parkour with Legged Robots（ICRA 2024）
- PDF： [recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf](<../recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf>)
- 笔记：domain randomization + 外感知将宇树 A1 连续地形 locomotion 能力推向极致，可跳箱、翻越、夹缝行走等（CMU/Stanford 等）。

##### Robot Parkour Learning（CoRL 2024）
- PDF： [recommended-papers/other/2024 - Robot Parkour Learning.pdf](<../recommended-papers/other/2024 - Robot Parkour Learning.pdf>)
- 笔记：与 Extreme Parkour 同期：通过 domain randomization + 外感知提升跑酷能力（CoRL 2024）。

##### Visual Whole-Body Control for Legged Loco-Manipulation（CoRL 2024）
- PDF： [recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf](<../recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf>)
- 笔记：在宇树 B1 + Z1 机械臂上验证视觉输入的双层策略（模仿学习 + 强化学习），通过 sim2real 实现自动移动抓取；基于 Isaac Gym + rsl_rl，代码已开源（UCSD）。

##### PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots（RAL 2024）
- PDF： [recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf](<../recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf>)
- 笔记：跑酷能力的增强版本：进一步提高动态能力，实现挑战环境高速运动并迁移到野外（ZJU）。

#### 双足 / 通用

##### Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition（ICRA 2021）
- PDF： [recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf](<../recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf>)
- 笔记：较早提出用概率周期函数定义足式步态（站立、行走、跳跃、跑步、单脚跳），在 Cassie 上测试；包含单步态策略与多步态切换策略，被后续工作参考。

##### AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control（SIGGRAPH 2021）
- PDF： [recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf](<../recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf>)
- 笔记：非足式机器人论文，但框架迁移价值高：用 GAN 作为隐式 metric 获得风格引导奖励学习控制策略（UCB）。

<a id="humanoids" name="humanoids"></a>
### 人形（Whole-Body Control / Teleop / Getting-Up 等）

#### Expressive Whole-Body Control for Humanoid Robots（RSS 2024）
- PDF： [recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf](<../recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf>)
- 笔记：基于 motion sequence retargeting 学习人形运动序列（UCSD）。

#### ExBody2: Advanced Expressive Humanoid Whole-Body Control（2024）
- PDF： [recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf](<../recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf>)
- 笔记：Expressive Whole-Body Control 的后续工作（2024）。

#### Open-TeleVision: Teleoperation with Immersive Active Visual Feedback（CoRL 2024）
- PDF： [recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf](<../recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf>)
- 笔记：开源 VR 人形机器人遥操作框架（仅上半身）。

#### Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control（2024）
- PDF： [recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf](<../recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf>)
- 笔记：在 Mobile-TeleVision 工作中展示全身控制方式，其中 locomotion 控制器结合 ExBody 思路（2024）。

#### HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots（ICRA 2025）
- PDF： [recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf](<../recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf>)
- 笔记：总结并统一多种人形全身控制方式（root velocity tracking、joint angle tracking、key-point tracking 等）（CMU）。

#### HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion（2025）
- PDF： [recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf](<../recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf>)
- 笔记：人形版 Walk These Ways：可细粒度调参的鲁棒连续地形 locomotion（步态、步频、机身高度、俯仰角、触地时间、抬腿高度等）；自然步态来自多项式足端轨迹引导奖励，并通过上肢介入课程实现上肢自由控制（SJTU/上海 AI Lab）。

#### Learning Humanoid Standing-up Control across Diverse Postures（RSS 2025）
- PDF： [recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf](<../recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf>)
- 笔记：效果很好的倒地起身控制（上海 AI Lab）。

#### Learning Getting-Up Policies for Real-World Humanoid Robots（RSS 2025）
- PDF： [recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf](<../recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf>)
- 笔记：同期起身策略工作（UIUC）。

#### BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion（2025）
- PDF： [recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf](<../recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf>)
- 笔记：高质量 motion tracking + guided diffusion：测试时可用简单 cost functions 做 task-specific control（Berkeley/Stanford）。

<a id="surveys" name="surveys"></a>
### 综述

#### Learning-based legged locomotion: State of the art and future perspectives（IJRR 2025）
- PDF： [recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf](<../recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf>)
- 笔记：学习方法腿足式机器人运动控制综述：系统概括过去几年学术界与工业界相关成果并展望未来方向（佐治亚理工，Georgia Tech）。

<a id="misc" name="misc"></a>
### 其他资料（暂无笔记）
- Robot Dynamics Lecture Notes（2017）— [PDF](<../recommended-papers/ETH-RSL/2017 - Robot Dynamics Lecture Notes.pdf>)
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [PDF](<../recommended-papers/MIT/Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control.pdf>)
- A Low Cost Modular Actuator for Dynamic Robots — [PDF](<../recommended-papers/MIT/MIT - A Low Cost Modular Actuator for Dynamic Robots.pdf>)
- [中文] 四足机器人随笔 — [PDF](<../recommended-papers/chinese/四足机器人随笔.pdf>)
- [中文] 新型电驱式四足机器人研制与测试-王兴兴 — [PDF](<../recommended-papers/chinese/新型电驱式四足机器人研制与测试-王兴兴.pdf>)
- [中文] 四足机器人跳跃步态主动柔顺控制研究 — [PDF](<../recommended-papers/chinese/四足机器人跳跃步态主动柔顺控制研究.pdf>)
- [中文] 仿生四足机器人多步态规划与控制 — [PDF](<../recommended-papers/chinese/仿生四足机器人多步态规划与控制.pdf>)
- [中文] 基于虚拟模型的四足机器人对角小跑步态控制方法 — [PDF](<../recommended-papers/chinese/基于虚拟模型的四足机器人对角小跑步态控制方法.pdf>)
- [中文] SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计 — [PDF](<../recommended-papers/chinese/SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计.pdf>)

返回总览：[README.md](../README.md)
