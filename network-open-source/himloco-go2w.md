# HIMLoco for Go2W：四轮足强化学习训练

> 类型：四轮足机器人 / HIMLoco / Isaac Gym / Sim2Sim

## 项目简介

[HIMLoco-for-Go2W](https://github.com/TrackinBIT/HIMLoco-for-Go2W) 将 HIMLoco 框架适配到 Unitree Go2W，用 Isaac Gym 训练四轮足机器人的运动控制策略。

## 训练与验证

仓库提供 `go2w` 任务，训练入口为：

```bash
cd legged_gym/scripts
python train.py --task=go2w
```

训练完成后可使用 `play.py` 查看并导出策略。MuJoCo 验证代码位于 `mujoco/`，运行前需要将 `config.yaml` 中的路径改为本地绝对路径。

MuJoCo 验证支持键盘控制：W/S 控制前后，A/D 控制左右，Q/E 控制偏航，空格键重置零位。仓库还提醒，站立阶段当前 PD 控制器主要跟踪最终目标状态，尚未完整跟踪插值曲线，必要时需要通过 Reset 获得成功站立效果。

## 参考项目

该项目基于 [HIMLoco](https://github.com/OpenRobotLab/HIMLoco)，同时参考 `legged_gym` 和 [rl_sar](https://github.com/fan-ziqi/rl_sar)。如果要进一步进行真机部署，建议优先核对四轮足的轮关节定义、观测与动作顺序、PD 参数以及仿真和实机的接口差异。

## 相关链接

- [项目仓库](https://github.com/TrackinBIT/HIMLoco-for-Go2W)
- [投稿视频](https://www.bilibili.com/video/BV1AbC3BLEVJ/)
