# AMP Go2：Unitree Go2 AMP 基础复现

> 类型：四足机器人 / AMP / 动作模仿 / Sim2Sim

## 项目简介

[amp_go2](https://github.com/ak1raljl/amp_go2) 是面向 Unitree Go2 EDU 的 AMP（Adversarial Motion Priors）实现。AMP 通过动作判别器约束策略，使机器人在完成速度控制任务的同时保持更接近参考动作的运动风格。

该仓库与本站的“AMP Go2：楼梯运动复现实验”使用同一代码入口，但本篇聚焦基础 AMP 流程和后续 Sim2Real 计划。

## 仓库流程

仓库提供从动作数据记录、数据可视化、Isaac Gym 训练、MuJoCo Sim2Sim 到实机部署准备的完整示例。动作数据可以从 `legged_control` 运行环境中记录，再转换为 AMP 使用的格式。

训练入口为：

```bash
python legged_gym/legged_gym/scripts/train.py --task=go2_amp
```

训练后的策略通过 `play.py` 导出 TorchScript，再由 `deploy_mujoco/deploy_go2.py` 在 MuJoCo 中回放。仓库还支持键盘控制和视频保存。

## 投稿实验

投稿者记录了训练约 4000 步后的效果，并表示后续计划公开实机 Sim2Real 代码，逐步分享相关强化学习内容。4000 步属于该次投稿时的训练记录，不应与完整收敛训练时长混同。

## 相关链接

- [AMP Go2 仓库](https://github.com/ak1raljl/amp_go2)
- [AMP 论文](https://arxiv.org/pdf/2203.15103)
- [投稿视频](https://www.bilibili.com/video/BV1bCdmB9EhK/)
