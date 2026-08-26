# AMP Go2：楼梯运动复现实验

> 类型：四足机器人 / AMP / 楼梯地形 / Sim2Sim

## 项目简介

这是基于 [ak1raljl/amp_go2](https://github.com/ak1raljl/amp_go2) 的 Unitree Go2 AMP 实验，投稿重点是使用 Trimesh 楼梯地形测试策略的越障能力，楼梯效果约达到 Level 4。

该文章与仓库中的“AMP Go2 基础复现”属于同一代码库，但记录的是楼梯场景实验，不能将 Level 4 直接理解为仓库对所有地形的统一评级。

## 仓库内容

仓库将 AMP 方法移植到 Go2 EDU，参考了 [AMP for Hardware](https://github.com/escontra/AMP_for_hardware)、[rl_amp](https://github.com/fan-ziqi/rl_amp) 和 [go2_rl_gym](https://github.com/wty-yy/go2_rl_gym)。算法通过动作捕捉数据训练运动判别器，帮助策略学习更自然的运动。

仓库提供 Isaac Gym 训练、动作数据可视化、MuJoCo Sim2Sim 和后续 Sim2Real 的基础流程。README 中还包含平地、楼梯、横坡和比赛赛道等 MuJoCo 场景配置。

## 使用流程

环境主要使用 Python 3.8、Isaac Gym 和对应版本的 PyTorch。动作数据来自 `legged_control` 记录的 Go2 运动，可通过脚本生成 AMP 数据，再使用 `python legged_gym/legged_gym/scripts/train.py --task=go2_amp` 训练。

训练后的策略可以通过 `play.py` 导出 TorchScript，再使用 `deploy_mujoco/deploy_go2.py` 在 MuJoCo 中回放。仓库提醒 Isaac Gym 与 MuJoCo 的观测维度、动作缩放、PD 参数、默认姿态和关节顺序必须保持一致。

## 实验信息

投稿者使用 Trimesh 构造楼梯，并报告了接近 Level 4 的效果。这里的楼梯难度、训练步数和视频表现属于该次实验记录；建议结合仓库场景文件与训练配置复核。

## 相关链接

- [AMP Go2 仓库](https://github.com/ak1raljl/amp_go2)
- [AMP 论文](https://arxiv.org/pdf/2203.15103)
- [投稿视频](https://www.bilibili.com/video/BV1bboeBDE3z/)
