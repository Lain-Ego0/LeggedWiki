# rl_sar：强化学习策略仿真与真机部署框架

> 类型：部署框架 / Gazebo / MuJoCo / ROS / 多机器人

## 项目简介

[rl_sar](https://github.com/fan-ziqi/rl_sar)（simulation and real）用于强化学习算法的仿真验证和物理机器人部署，支持四足、轮足和人形机器人。框架兼容 Isaac Gym、Isaac Sim、Gazebo 与 MuJoCo，并提供 ROS Noetic、ROS 2 Foxy/Humble、libtorch 和 ONNX Runtime 接口。

支持列表包含 Unitree A1、Go2、Go2W、B2/B2W、G1、Lite3、Agibot D1 等平台，既可运行 locomotion，也可运行部分舞蹈策略。仓库还提供 Docker、移动 Web 控制和多种网络/SDK 接口。

## 使用方式

克隆子模块并运行 `build.sh` 编译；将训练得到的模型放入对应机器人/策略目录，配置 `config.yaml` 后，可通过 Gazebo、MuJoCo 或真机入口运行。与 [robot_lab](https://github.com/fan-ziqi/robot_lab) 配套时，需保证两边的关节顺序一致。

## 相关链接

- [GitHub 仓库](https://github.com/fan-ziqi/rl_sar)
- [配套训练库 robot_lab](https://github.com/fan-ziqi/robot_lab)
