# BFM-Zero：可提示的人形行为基础模型

> 类型：人形机器人 / 行为基础模型 / 无监督强化学习 / sim-to-real

## 项目简介

[BFM-Zero](https://github.com/LeCAR-Lab/BFM-Zero) 提出一种使用无监督强化学习训练的、可通过提示控制的人形机器人行为基础模型。模型从运动跟踪和任务奖励中提取潜变量 `z`，再用不同目标或奖励推断出可执行行为。

项目支持 Isaac Sim 与 MuJoCo，并逐步公开预训练模型、最小推理代码、完整训练评测流程，以及基于 [UFO](https://github.com/Roboparty/UFO) 的 MJLab 分布式训练和遥操作实现。

## 使用流程

仓库通过 Git LFS 提供 LaFan 运动数据和模型文件，使用 `uv sync` 安装依赖后，可运行 `humanoidverse.train` 训练。训练完成后，`tracking_inference`、`goal_inference` 和 `reward_inference` 分别用于运动跟踪、目标到达和奖励任务推理，并将策略导出为 ONNX。

BFM-Zero 需要 CUDA GPU；推理阶段可以选择 Isaac Sim 或 MuJoCo。使用真实机器人前，应先在仿真中验证策略、观测和动作接口。

## 相关链接

- [GitHub 仓库](https://github.com/LeCAR-Lab/BFM-Zero)
- [项目主页](https://lecar-lab.github.io/BFM-Zero/)
- [论文（arXiv）](https://arxiv.org/abs/2511.04131)
