# KAIST（Raibo / Unitree 等）

> 中文 | [English](KAIST.en.md)

## Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion（RAL 2022）
- PDF： [recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf](<../recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- 笔记：一阶段非对称学习（非教师-学生）：策略网络联合训练关键状态估计器（线速度、足端高度、触地概率，输入为历史可观测数据）；仿真中 critic 直接使用关键状态真值，并引入 dynamics randomization，使用 PPO 训练后可部署并穿越多样连续复杂地形。

## DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning（ICRA 2023）
- PDF： [recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf](<../recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- 笔记：非对称强化学习结构：状态估计器从可观测信息中估计速度与隐式地形信息 z，z 通过 VAE 学习。在宇树 A1 上实现鲁棒的长距离多样户外地形行走，说明非对称 actor-critic 训练框架可在复杂环境获得很强的运动能力。

## Learning quadrupedal locomotion on deformable terrain（Science Robotics 2023）
- PDF：暂未找到可公开抓取的 PDF（可能为期刊付费版；可优先找作者公开版/预印本）。
- 笔记：针对模拟器多为刚性接触动力学，修改 RaiSim 底层接触模型，建模颗粒介质（granular media）接触动力学，实现 Raibo 在沙滩/海绵垫等松软地形的敏捷与鲁棒运动；采用非对称训练框架，进一步验证其有效性。

## A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards（ICRA 2025）
- PDF： [recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf](<../recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- 笔记：引入松弛对数障碍函数，设计基于运动模式特征的软约束奖励机制，引导机器人趋向预设运动形态参数（周期步态、关节范围限制等）。未使用运动先验也生成多种仿生四足步态，其中四足站立的“仿人行走”与 gallop 奔跑步态令人印象深刻。
