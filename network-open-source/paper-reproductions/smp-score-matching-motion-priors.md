# SMP：可复用分数匹配运动先验复现

> 类型：运动先验 / 模仿学习 / 强化学习 / 人形机器人

## 项目简介

SMP（Score-Matching Motion Priors）是从对抗模仿学习走向生成式运动先验的一种方法。它先用运动数据训练扩散模型，再将冻结的模型作为与具体任务无关的奖励模型，通过 Score Distillation Sampling（SDS）引导 PPO 策略产生自然运动。

论文主页将这种先验概括为：一次训练、跨任务复用。一个运动先验可以用于行走、转向、目标点导航、躲避球、起身等任务，也可以通过风格条件和风格组合生成训练数据中没有直接出现的新风格。

## 本次开源复现

原始方法和参考实现来自 [SMP 论文](https://arxiv.org/abs/2512.03028)、[项目主页](https://yxmu.foo/smp-page/) 和 [MimicKit](https://github.com/xbpeng/MimicKit)。投稿者提供的 [SUZ-tsinghua/smp](https://github.com/SUZ-tsinghua/smp) 则将方法完整移植到 Unitree G1：包括运动特征、扩散先验、任务环境和奖励设计。

仓库基于 [mjlab](https://github.com/mujocolab/mjlab)，而不是直接依赖原始 MimicKit 的 G1 配置。项目提供了行走/慢跑/奔跑、LAFAN 奔跑和起身三类预训练先验，可以直接跳过扩散模型预训练进入 RL。

## 方法流程

1. 将 LAFAN1 等动作 CSV 转换为运动窗口和归一化统计；
2. 在运动窗口上训练 DDPM 扩散模型；
3. 冻结扩散模型，在 PPO 训练期间计算 SDS 风格的运动自然度奖励；
4. 将任务奖励与 SMP 奖励结合，学习面向下游任务的控制策略。

与原始方法的一个重要差异是，该复现仓库采用 `task × SMP` 的乘法奖励，而不是任务奖励与先验奖励的加法。这样只有同时完成任务并保持在合理运动分布附近时，策略才能获得较高奖励。

## 任务与运行入口

仓库当前列出了以下 G1 任务：

- `Smp-Forward-G1`：跟踪前向速度，覆盖行走、慢跑和奔跑；
- `Smp-Steering-G1`：跟踪速度与朝向；
- `Smp-Location-G1`：移动到世界坐标系目标点；
- `Smp-Getup-G1`：从倒地姿态起身。

安装方面，仓库使用 `uv` 管理依赖，并锁定 `mjlab` 版本。使用已提供先验时，基本流程是 `uv sync --frozen`，然后运行 `uv run scripts/train.py Smp-Forward-G1 --env.scene.num-envs=4096`。

## 数据与复现提示

G1 动作输入采用 LAFAN1 重定向格式：每帧 36 列，包括根位置、四元数和 29 个关节角。仓库会将 30 FPS 数据转换到 50 FPS，并生成包含根状态、关节、末端位置和速度的 59 维运动特征。

投稿视频展示了该思路在高速度四足运动中的尝试，标题为“最快 5 m/s，浅尝 SMP”。视频中的具体速度和训练配置属于投稿者实验结果，实际复现应以仓库当前代码、数据和配置为准。

## 相关链接

- [论文 PDF](https://arxiv.org/pdf/2512.03028)
- [SMP 项目主页](https://yxmu.foo/smp-page/)
- [复现代码](https://github.com/SUZ-tsinghua/smp)
- [完善环境安装代码：mimic](https://github.com/senlanke/mimic)
- [投稿视频](https://www.bilibili.com/video/BV1CEh36mE3W/)
