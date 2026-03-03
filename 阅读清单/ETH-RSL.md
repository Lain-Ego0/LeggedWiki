# ETH Robotics Systems Lab（RSL）

> 中文 | [English](ETH-RSL.en.md)

## Learning Agile and Dynamic Motor Skills for Legged Robots（Science Robotics 2019）
- PDF： [推荐论文/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf](<../推荐论文/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- 笔记：强化学习四足运控的奠基之作：用真实数据训练电机网络模型，并在仿真中进行补偿，结合 RL + dynamics randomization 训练策略；成功部署到 ANYmal，实现鲁棒 locomotion（速度跟踪、跌倒恢复等）。

## Learning Quadrupedal Locomotion over Challenging Terrain（Science Robotics 2020）
- PDF： [推荐论文/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf](<../推荐论文/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- 笔记：首次提出两阶段教师-学生框架：教师策略利用模拟器里的“作弊信息”学习到好的运动策略，再通过在线模仿学习（DAgger）蒸馏给可部署（仅使用历史可观测数据）的学生策略（引入 encoder 估计隐式作弊信息）。同时提出地形课程，实现鲁棒的复杂连续地形行走。该阶段控制栈仍较复杂：网络用于辅助足端轨迹生成，还需 IK 求解得到最终 target joints；而后续主流更倾向策略直接输出 target joints。

## Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning（CoRL 2021）
- PDF： [推荐论文/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf](<../推荐论文/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- 笔记：里程碑工作：推动 RL + Robotics 的后续发展。开发并验证 Isaac Gym 大规模并行训练 + domain randomization 的强化学习运控方案，并开源 `legged_gym` 项目。

## Learning robust perceptive locomotion for quadrupedal robots in the wild（Science Robotics 2022）
- PDF： [推荐论文/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf](<../推荐论文/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- 笔记：集成本体感知与外部视觉信号的鲁棒 locomotion 策略，实现大规模户外甚至极端条件行走（楼梯、隧道、雪山、浓雾、森林、碎岩等）。给出了学习“带外感知策略”（估计高程图）的范例。

## Elevation Mapping for Locomotion and Navigation using GPU（IROS 2022）
- PDF： [推荐论文/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf](<../推荐论文/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)
- 笔记：提出利用 GPU 高效构建高程图的方法：接收外部传感器点云与机器人位姿信息，快速构建周围地形高程图；复杂环境中里程计漂移仍是实时建图的最大挑战之一。代码已开源。

## Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning（ICRA 2023）
- PDF： [推荐论文/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf](<../推荐论文/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- 笔记：增强版 AMP：允许多种可离散切换的风格，在轮腿四足机器人上展示躲避、行走，以及四足与双足模式（站立）之间的风格切换；其中从“反向站立（双足）序列”学习“趴下（四足）”的案例较有意思。

## Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks（CoRL 2023）
- PDF：暂未找到可公开抓取的 PDF（可能在 OpenReview/作者主页）。
- 笔记：亮点：用轮腿四足学习把腿当作 manipulator 的 loco-manipulation 策略。

## Learning Agile Locomotion on Risky Terrains（IROS 2024）
- PDF： [推荐论文/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf](<../推荐论文/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- 笔记：（@XueYeiii）有意思的工作之一：可能是较早的基于 RL 运控走离散地形的工作（虽非全向行走），demo 效果不错。

## ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots（Science Robotics 2024）
- PDF： [推荐论文/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf](<../推荐论文/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- 笔记：多层级框架：感知模块重建环境信息，导航模块根据环境信息导航并驱动运动模块选择能力；运动模块具备跑酷基本技能。首篇实现四足动态跑酷的工作之一。

## DTC: Deep Tracking Control（Science Robotics 2024）
- PDF： [推荐论文/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf](<../推荐论文/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- 笔记：结合 Model-based 与 Learning-based：上层 TO 根据环境与动力学实时优化机身轨迹与足端轨迹；底层 RL 严格跟踪优化轨迹，实现极端地形的精确运动（梅花桩、深沟、废墟等）。相较只做机身速度跟踪的方法，该分层框架更有利于落足点选择。
