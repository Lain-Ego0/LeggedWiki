# Unitree Qmini 与 RoboTamer：可 3D 打印的低成本双足机器人

> 类型：双足机器人 / 开源硬件 / Isaac Gym / sim-to-real

## 项目简介

山东大学 VSISLab 与宇树联合开源了 [Unitree Qmini](https://github.com/unitreerobotics/Qmini)：面向个人玩家、教育和研究的低成本双足机器人。硬件模型由宇树提供，软件和部署算法由山大提供，整机机械结构支持个人 3D 打印。

Qmini 仓库包含 BOM、电气系统框图、DIY 指南、STEP 机械文件、装配 SOP 和 URDF。机器人使用 11 个 Unitree 8010 电机，其中 10 个用于运动，颈部电机可用于扩展；参考控制板为 Raspberry Pi 4B。

## 软件与训练

[RoboTamer4Qmini](https://github.com/vsislab/RoboTamer4Qmini) 基于 Isaac Gym 和 PPO，提供 Qmini 的粗糙地形训练、域随机化、随机推搡、策略播放、PID 调参及 PT 到 ONNX 导出。项目需要 Ubuntu 18.04/20.04、Isaac Gym、CUDA 和至少约 8 GB 显存；README 提醒部分路径写死且仓库目前不再维护。

## 相关链接

- [宇树 Qmini 硬件仓库](https://github.com/unitreerobotics/Qmini)
- [山东大学 RoboTamer 项目页](https://vsislab.github.io/RoboTamer/)
- [RoboTamer4Qmini 软件仓库](https://github.com/vsislab/RoboTamer4Qmini)
