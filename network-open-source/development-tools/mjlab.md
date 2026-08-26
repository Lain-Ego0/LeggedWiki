# mjlab：MuJoCo Warp GPU 机器人学习框架

> 类型：机器人学习 / MuJoCo Warp / GPU 仿真 / IsaacLab API

## 项目简介

[mjlab](https://github.com/mujocolab/mjlab) 将 IsaacLab 的 manager-based API 与 MuJoCo Warp 的 GPU 加速仿真结合，提供可组合的环境设计组件，并允许直接访问 MuJoCo 原生数据结构。项目适用于强化学习、运动模仿和机器人研究。

仓库内置 Unitree G1 速度跟踪、运动模仿等示例，支持多 GPU 训练、Weights & Biases 评估和 MuJoCo 原生评测。无需本地安装即可用 `uvx` 启动 demo，也可从源码或 PyPI 安装。

## 快速开始

```bash
uvx --from mjlab --refresh demo
uv run train Mjlab-Velocity-Flat-Unitree-G1 --env.scene.num-envs 4096
uv run train Mjlab-Tracking-Flat-Unitree-G1 --registry-name your-org/motions/motion-name
```

项目需要 NVIDIA GPU 进行训练，macOS 主要用于评估。UFO 和 BFM-Zero 的部分训练流程建立在 mjlab 之上。

## 相关链接

- [GitHub 仓库](https://github.com/mujocolab/mjlab)
- [项目文档](https://mujocolab.github.io/mjlab/)
- [论文](https://arxiv.org/abs/2601.22074)
