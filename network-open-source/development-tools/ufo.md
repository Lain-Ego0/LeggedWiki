# UFO：人形机器人无监督强化学习框架

> 类型：人形控制 / 无监督强化学习 / MJLab / 远程操作

## 项目简介

[UFO](https://github.com/Roboparty/UFO) 是 Roboparty 开源的人形机器人控制框架，面向无监督强化学习（unsupervised RL）。项目实现 FB/TeCH 训练流程、面向具体机器人的动作导入，以及真实机器人远程操作。

UFO 基于 [MJLab](https://github.com/mujocolab/mjlab) 构建，提供训练配置、动作数据处理、策略推理和部署脚本。其定位是把通用行为学习与人形机器人的运动控制、数据采集连接起来。

## 主要内容

- FB/TeCH 等无监督强化学习训练方法；
- 人形机器人动作导入与机器人适配配置；
- 仿真训练、策略推理和 sim-to-sim/sim-to-real 部署；
- 面向真实机器人的 teleoperation 工具。

仓库的 `configs/`、`humanoidverse/` 和 `scripts/` 分别承载配置、环境与训练/部署入口。BFM-Zero 的分布式 MJLab 训练和遥操作实现也参考了 UFO。

## 相关链接

- [GitHub 仓库](https://github.com/Roboparty/UFO)
- [项目主页](https://roboparty.github.io/UFO/)
- [BFM-Zero](https://github.com/LeCAR-Lab/BFM-Zero)
