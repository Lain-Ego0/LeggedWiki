# LeggedGym-Ex：多仿真器腿足机器人训练框架

> 类型：强化学习框架 / Isaac Gym / Genesis / Isaac Sim

## 项目简介

[LeggedGym-Ex](https://github.com/lupinjia/LeggedGym-Ex) 以 `legged_gym` 的 API 和代码习惯为基础，将训练流程扩展到 Isaac Gym、Genesis 和 Isaac Sim 三种仿真器。

它的目标不是重新发明一套完全不同的接口，而是尽量保留 legged_gym 的可读性和使用方式，让同一个机器人任务能够在不同仿真器中进行训练和比较。

## 主要功能

- 支持 Isaac Gym、Genesis 和 Isaac Sim；
- 使用 NVIDIA Warp 加速深度图渲染；
- 集成 Walk These Ways、系统辨识、Teacher-Student、显式状态估计和 Constraints as Terminations 等方法示例；
- 目录结构和环境配置延续 legged_gym 风格，便于迁移已有任务。

仓库对仿真器的定位是：Isaac Gym 训练速度较快，Genesis 兼顾速度和软体/流体扩展，Isaac Sim 渲染更真实但训练速度相对较慢。实际选择仍取决于任务、显卡和所需传感器。

## 使用建议

项目 README 提供了安装、训练、深度图和示例任务说明。新增机器人时应先阅读仓库随附文档，再按照对应仿真器的环境目录添加资产、观测、奖励和训练配置。框架仍在持续更新，人形机器人及更多仿真器支持处于计划中。

## 相关链接

- [项目仓库](https://github.com/lupinjia/LeggedGym-Ex)
- [legged_gym](https://github.com/leggedrobotics/legged_gym)
- [投稿视频](https://www.bilibili.com/video/BV1S1ZNBgEcB/)
