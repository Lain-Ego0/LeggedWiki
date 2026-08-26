# Go2 空翻数据采集与全身轨迹优化

> 类型：动作生成 / 轨迹优化 / 空翻数据 / Go2

## 项目简介

[go2_flip_TO](https://github.com/yusongmin1/go2_flip_TO) 是一个用于 Go2 后空翻脚本生成的项目。仓库实际实现的是基于 SE(3) 切空间的浮动基全身轨迹优化：将机器人动力学、接触约束和地形建模放入非线性优化问题，通过 IPOPT 和 Pinocchio 求解动作轨迹。

## 主要能力

仓库示例包含前后行走、左右侧空翻、前空翻、后空翻和向前跳跃。优化结果可以通过 MeshCat 可视化，也可以导出为 50 Hz 的 Go2 动作数据，用于后续 AMP 或其他模仿学习流程。

每帧数据包含根位置、根姿态、12 个关节角、足端相对位置、根部线速度/角速度和关节速度，共 49 个浮点数。导出的数据位于 `datasets/go2/mocap_motions_go2/`，可以用 MuJoCo 脚本回放。

## 安装与运行

仓库建议使用 Python 3.10 及以上，并通过 Conda 安装 Pinocchio、cyipopt、MeshCat、Matplotlib 和 NumPy。运行示例前需要设置：

```bash
export PYTHONPATH="$(pwd)/src/nltrajopt:$(pwd)/src"
```

例如，`python src/examples/agile_exps/quad_backflip.py --vis` 可生成后空翻轨迹。若 MuJoCo 图形窗口出现 GLX 或段错误，可以使用 EGL 离屏导出视频。

## 与强化学习的关系

该项目本身是轨迹优化和动作数据生成工具，并非完整的 RL 训练框架。它可以为 AMP、动作模仿或高动态策略训练提供结构化参考轨迹，降低直接从随机探索学习空翻动作的难度。

## 相关链接

- [项目仓库](https://github.com/yusongmin1/go2_flip_TO)
- [论文：A Comparative Study of Floating-Base Space Parameterizations](https://arxiv.org/abs/2508.11520)
- [投稿视频](https://www.bilibili.com/video/BV1qCDsBoEMQ/)
