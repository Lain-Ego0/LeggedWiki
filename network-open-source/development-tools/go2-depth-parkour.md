# Go2 深度图跑酷：LeggedGym-Ex 任务示例

> 类型：四足机器人 / 深度图感知 / Teacher-Student / 复杂地形

## 项目简介

这是 [LeggedGym-Ex](https://github.com/lupinjia/LeggedGym-Ex) 中针对 Unitree Go2 的深度图跑酷任务，代码位于 `legged_gym/envs/go2/go2_ts_depth`。

任务重点是将深度图感知纳入腿足机器人强化学习，使策略能够利用前方地形信息完成复杂地形运动。它属于 LeggedGym-Ex 中 Go2 Teacher-Student/深度感知方向的示例，与仅依赖本体观测的速度控制任务不同。

## 框架关系

LeggedGym-Ex 保持 legged_gym 的任务组织方式，并支持 Isaac Gym、Genesis 和 Isaac Sim。该 Go2 任务可以作为深度传感器输入、深度图渲染和策略训练流程的参考；框架还集成 Warp 以加速 NVIDIA GPU 上的深度图渲染。

## 阅读入口

任务目录包含 `go2_ts_depth.py` 和 `go2_ts_depth_config.py`。建议先阅读配置文件，再结合框架 README 了解仿真器选择、传感器输入、训练命令和教师学生结构。仓库当前持续开发，具体参数应以最新分支为准。

## 相关链接

- [Go2 深度图任务目录](https://github.com/lupinjia/LeggedGym-Ex/tree/main/legged_gym/envs/go2/go2_ts_depth)
- [LeggedGym-Ex 仓库](https://github.com/lupinjia/LeggedGym-Ex)
- [投稿视频](https://www.bilibili.com/video/BV1AboDBRE2X/)
