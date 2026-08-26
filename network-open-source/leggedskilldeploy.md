# LeggedSkillDeploy：腿足机器人多策略部署框架

> 类型：部署框架 / 模仿学习 / 强化学习 / 多机器人

## 项目简介

[LeggedSkillDeploy](https://github.com/haozhang04/LeggedSkillDeploy) 是一个面向腿足机器人运动控制的 Python 多策略部署框架，以状态机组织不同机器人、不同算法和不同技能的推理与切换。

## 支持范围

仓库支持：

- Go1 / Go2：HIMLOCO、NP3O、MoE、Loco、倒立、跳跃、后空翻、侧空翻和 Bound 等；
- Go2W：行走、倒立和腿立；
- M20：行走和高台；
- Duow 双轮足：行走；
- G1：动作模仿、行走和 AMP。

项目当前主要是部署侧框架，不负责替代各算法的训练仓库。它适合把多个已经训练好的策略统一接入仿真或实机，并通过键盘、Xbox 手柄或手机 Web 页面切换控制模式。

## 运行方式

仓库提供 MuJoCo、MuJoCo GLFW 和 Gazebo 入口。基础环境为 Python 3.10，安装依赖后可以运行 `src/rl_mujoco.py`、`src/rl_mujoco_glfw.py` 或 `src/rl_gazebo.py`。实机入口为 `src/rl_real.py`，但 README 明确提示目前仅在 Go1 Pro 上完成测试，部署时需要充分做好保护。

策略表和代码中还可以看到 Go2 的行走、跳跃、后空翻、侧空翻，以及 M20 高台等模型入口。适配新机器人时，需要修改机器人 IO 接口和对应的策略配置。

## 相关链接

- [项目仓库](https://github.com/haozhang04/LeggedSkillDeploy)
- [投稿视频](https://www.bilibili.com/video/BV1cpGt65EF1/)
