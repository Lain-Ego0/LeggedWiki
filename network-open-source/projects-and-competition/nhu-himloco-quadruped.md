# 南华大学衡山Π：HIMLOCO 串联四足机器人项目

> 类型：串联四足机器人 / 强化学习 / Sim2Real

## 项目简介

这是南华大学衡山Π战队串联四足机器人的代码整理，包含强化学习训练框架、MuJoCo Sim2Sim 验证和实机部署代码。作者说明训练完成后因临近比赛没有继续部署，赛后机器人又出现故障，因此目前没有可展示的真机效果。

## 项目仓库

- [uw-himloco：RL 训练框架](https://github.com/uwvwko-zzz/uw-himloco)
- [himdog：Sim2Real 部署](https://github.com/uwvwko-zzz/himdog)

其中：

- `uw-himloco` 基于 HIMLOCO 修改；
- `himdog` 中主要使用 `dog_policy_test` 和 `dog_control` 部分；
- `hip` 分支用于倾倒恢复；
- `high` 分支用于上高台。

## 训练框架

`uw-himloco` 基于 Isaac Gym，支持从仿真训练到 MuJoCo Sim2Sim 验证、ONNX 模型导出的流程。仓库以分支组织不同任务：`main` 为正常 locomotion，任务名为 `dog`；`hip` 为从倒地姿态恢复站立的 `dog_recovery`；`high` 为上高墙或登上平台的 `dog_high`。项目还提供 A1、Go1、Go2 和 Aliengo 等机器人配置。

策略支持 45 维基础观测和 46 维高度指令观测，动作空间为 12 维关节位置增量，采用 PD 位置控制。训练中包含平地、复杂地形、台阶、踏脚石和斜坡等场景，并提供 45/46 维 ONNX 导出脚本与 MuJoCo 推理示例。

## 硬件信息

- 电机：灵足 02；
- IMU：达妙 IMU。

`himdog` 是 ROS 2 部署工程：`dog_control` 负责电机通信和底层 PD 控制，`dog_policy_test` 负责 ONNX 策略推理，仓库还包含导航与视觉相关的 `dog_nav` 包。策略推理节点提供键盘、手柄和导航等控制模式，并包含模型切换、传感器滤波、倾倒检测和系统监控等工程实现。

## 实车效果说明

由于比赛临近，训练完成后没有继续部署到实物上，比赛结束后机器人又出现故障，因此目前没有可展示的实车效果。项目主要适合用于学习训练框架、策略分支和 Sim2Real 部署代码。

作者认为项目仍有部分功能可以改进，欢迎基于仓库进行交流和完善。训练框架中的论文背景可参考 [HIMLoco](https://arxiv.org/abs/2312.11460) 与 [H-Infinity Locomotion Control](https://arxiv.org/abs/2404.14405)。
