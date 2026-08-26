# 福州大学浮舟湿地：12DOF 四足强化学习训练项目

> 类型：四足机器人 / 12DOF / 强化学习训练

## 项目简介

福州大学浮舟湿地战队开源了一套点足 12DOF 四足机器人的强化学习训练代码。仓库称其为“26RC 浮舟湿地马术 RL 训练开源”，目标是训练仅依靠电机位置和 IMU 等本体感知完成运动控制的策略。项目 README 中还整理了作者学习强化学习过程中的一些体会，并配有系统框图和数据流图。

项目仓库：

- [Taojunfeng123/quadruped_robot_lab](https://github.com/Taojunfeng123/quadruped_robot_lab)

## 项目内容

目前项目主要提供：

- 点足 12DOF 四足机器人的 RL 训练代码；
- 强化学习学习过程中的经验和思考；
- README 中的结构说明与示意图。

根据仓库说明，项目基于 `Fan Ziqi/robot_lab` 二次开发，并借鉴了云深处 Lite3 项目中的部分步态奖励和课程学习设计。训练框架采用 Isaac Lab，当前 README 列出的环境包括 Ubuntu 22.04、Python 3.11.15、Isaac Lab 0.54.3、Isaac Sim 5.1.0 和 rsl_rl 5.0.1。

## 已展示能力

仓库展示了平地、斜坡、绕桩、沙石地等场景，并报告了在起伏粗糙地形约 3 m/s 运行、以约 2 m/s 上下楼梯的训练结果；在不使用相机或雷达的情况下，楼梯高度 15 cm 以下可以稳定运行。以上属于仓库作者的实验记录，复现时需要使用相同或相近的机器人模型、参数和训练配置。

## 训练入口

安装到 Isaac Lab 的同一 Conda 环境后，可使用 `python -m pip install -e source/robot_lab` 安装，并通过 `scripts/tools/list_envs.py` 检查环境。README 提供了 `Rough-train` 和 `Stair-train` 的 rsl_rl 训练命令，并区分 rsl_rl 5.0.1 与旧版本脚本。项目还包含 URDF/Mesh 资产、训练日志、检查点和多种 MDP 配置。

作者后续仍可能继续修改或补充 README，因此完整说明以 GitHub 仓库为准。

## 相关讨论

- [Robomaster 论坛原帖](https://bbs.robomaster.com/article/1938225)

项目作者表示，希望该开源内容能帮助更多队伍开展四足机器人强化学习训练，也欢迎通过项目仓库进行交流和反馈。
