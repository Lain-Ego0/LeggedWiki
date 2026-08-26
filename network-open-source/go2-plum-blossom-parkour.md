# Go2 梅花桩跑酷：Isaac Gym 复杂地形训练

> 类型：四足机器人 / 强化学习 / 复杂地形 / 梅花桩

## 项目简介

[legged_robot_competition](https://github.com/jindadu00/legged_robot_competition) 是一个基于 Isaac Gym 和 legged_gym 的 Go2 复杂地形强化学习项目，目标是让四足机器人在赛道上尽可能行走更远，并重点展示了翻越梅花桩。

项目规则允许使用强化学习或其他算法，不限制传感器类型，也允许自动控制或键盘控制。比赛终止条件主要包括 base 接触地面或到达赛道终点，成绩按行走距离评判。

## 训练内容

仓库提供 Go2 环境、训练与评估脚本，以及奖励函数、观测、课程学习和实验记录方面的说明。作者采用由易到难的课程：先到达梅花桩前，再逐步增加需要跨越的梅花桩数量和难度，最后训练完整赛道。

面对单一策略难以兼顾普通地面和梅花桩的情况，项目还讨论了分层策略：分别训练不同地形的策略，在识别地形后切换控制器。目标点追踪奖励、梅花桩边缘惩罚和前方地形高度观测是其中较有代表性的设计。

## 环境与运行

README 记录的环境包括 Ubuntu 20.04、Python 3.8、PyTorch 2.4.0 + CUDA 12.1，并使用 Isaac Gym。基本训练命令是 `python train.py --task=go2 --num_envs=64 --headless`，显卡性能足够时可以提高并行环境数量。训练后使用 `play.py` 加载 checkpoint 评估。

## 相关代码

- [比赛/训练项目](https://github.com/jindadu00/legged_robot_competition)
- [训练好的复杂地形示例](https://github.com/jindadu00/Training-Quadruped-Robots-to-Traverse-Diverse-Complex-Terrains)
- [投稿视频](https://www.bilibili.com/video/BV1qQ4VefEa6/)
