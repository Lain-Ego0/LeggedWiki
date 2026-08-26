# TWIST：全身遥操作模仿系统

> 类型：人形机器人 / 遥操作 / 模仿学习 / G1

## 项目简介

[TWIST](https://github.com/YanjieZe/TWIST)（Teleoperated Whole-Body Imitation System，CoRL 2025）面向 Unitree G1，提供从人体动作遥操作、教师/学生策略训练到 sim-to-sim 和 sim-to-real 的完整开源流程。

仓库公开训练数据、教师与学生策略代码、预训练通用运动跟踪器，以及高低层控制分离的部署脚本。教师策略通过 RL 学习，学生策略通过 RL+BC 蒸馏，最终可导出 JIT 模型部署。实时动作重定向由配套项目 [GMR](https://github.com/YanjieZe/GMR) 提供。

## 相关链接

- [GitHub 仓库](https://github.com/YanjieZe/TWIST)
- [项目主页](https://humanoid-teleop.github.io/)
- [论文](https://arxiv.org/abs/2505.02833)
- [GMR 实时重定向](https://github.com/YanjieZe/GMR)
