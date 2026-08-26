# RoboGauge：Go2 高鲁棒运动控制与自动评测方案

> 类型：四足机器人 / 本体感知 / MoE / Sim2Real / 自动评测

## 项目简介

该项目开源了首届腾讯开悟具身智能强化学习运控挑战赛的 Go2 方案。团队基于 Unitree Go2 EDU，训练仅依赖本体感知的鲁棒运动控制策略，并将比赛、高速奔跑和综合场景分别进行优化。

## 三类策略

- **比赛模型**：针对赛道环境和黄色胶带引导线优化；
- **高速模型**：平地最高速度约 4 m/s；
- **综合模型**：面向其他 Demo 场景的通用鲁棒控制。

相关论文是 [Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion](https://arxiv.org/abs/2602.00678)。项目主页展示了 Isaac Gym、MuJoCo 和实机效果，并提供训练、评估和部署三个仓库。

## 代码组成

- [训练代码：go2_rl_gym](https://github.com/wty-yy/go2_rl_gym)：基于 `unitree_rl_gym` 的 Go2 强化学习实现，包含 CTS、MoE 等任务；
- [评估代码：RoboGauge](https://github.com/wty-yy/RoboGauge)：使用 MuJoCo 自动评估鲁棒性、安全性、跟踪精度和控制质量；
- [部署代码：unitree_cpp_deploy](https://github.com/wty-yy/unitree_cpp_deploy)：面向 Go2 EDU 与 Orin NX 的 C++ 部署。

RoboGauge 可以测试波浪、斜坡、楼梯、障碍物等地形，并统计关节限位、速度误差、能耗、姿态稳定性、力矩平滑度、摩擦裕度和 ZMP 裕度等指标。它还支持在训练期间异步评估模型，把结果写入日志和 TensorBoard。

## 训练与部署特点

训练仓库支持从 Isaac Gym 训练到 MuJoCo Sim2Sim，再到 Python/C++ Sim2Real。公开评测表中，`go2_moe_cts` 在 150k 训练步后的综合分数为 0.6713，具体成绩应以仓库当前版本和对应 checkpoint 为准。

C++ 部署支持通过网络连接或 Orin NX 机载电脑运行，并可在运行时切换多个速度策略。仓库还公开了模型和相关 Hugging Face 资源入口。

## 相关链接

- [Project Page](https://robogauge.github.io/complete/)
- [论文](https://arxiv.org/abs/2602.00678)
- [训练代码](https://github.com/wty-yy/go2_rl_gym)
- [评估代码](https://github.com/wty-yy/RoboGauge)
- [C++ 部署代码](https://github.com/wty-yy/unitree_cpp_deploy)
- [投稿视频](https://www.bilibili.com/video/BV1mwFLzTEWV/)
