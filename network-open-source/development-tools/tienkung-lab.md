# TienKung-Lab：全尺寸人形机器人 IsaacLab 工作流

> 类型：人形机器人 / IsaacLab / AMP / sim-to-sim / sim-to-real

## 项目简介

[TienKung-Lab](https://github.com/Open-X-Humanoid/TienKung-Lab) 是面向全尺寸 Tien Kung 人形机器人的 IsaacLab 直接工作流。项目将 AMP 风格奖励、周期步态奖励和射线传感器结合，用于训练自然、稳定的行走与跑步策略。

框架基于 Isaac Sim 4.5.0、IsaacLab 2.1.0 和 RSL-RL，提供 MuJoCo sim-to-sim 验证，并已在真实 Tien Kung 机器人上完成验证。

## 主要流程

项目使用 [GMR](https://github.com/YanjieZe/GMR) 将 SMPL-X/AMASS 等人体动作重定向到 Tien Kung，再将数据转换为可视化轨迹和 AMP 专家数据。训练入口支持 `walk`、`run` 等任务，策略可导出后通过 `sim2sim.py` 在 MuJoCo 中验证。

真机部署代码位于独立仓库 [Deploy_Tienkung](https://github.com/Open-X-Humanoid/Deploy_Tienkung)。真实机器人测试具有风险，应准备急停并先完成仿真验证。

## 相关链接

- [GitHub 仓库](https://github.com/Open-X-Humanoid/TienKung-Lab)
- [部署仓库](https://github.com/Open-X-Humanoid/Deploy_Tienkung)
- [GMR 动作重定向](https://github.com/YanjieZe/GMR)
