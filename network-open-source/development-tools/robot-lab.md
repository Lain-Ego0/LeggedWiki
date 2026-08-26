# robot_lab：基于 IsaacLab 的机器人强化学习扩展库

> 类型：强化学习训练 / IsaacLab / 多机器人

## 项目简介

[robot_lab](https://github.com/fan-ziqi/robot_lab) 是一个脱离 IsaacLab 核心仓库运行的 RL 扩展库，采用外部扩展方式组织机器人模型、环境和训练脚本。仓库覆盖 Unitree Go2、Go2W、B2、A1、G1，以及 Anymal D、Lite3、ZSL1 等多种足式和人形平台。

项目提供 RSL-RL 训练、策略播放、零动作/随机动作环境检查，以及 BeyondMimic 等动作模仿示例。当前 README 对应 Isaac Sim 5.1.0、IsaacLab 2.3.2 和 Python 3.11。

## 使用方式

安装 IsaacLab 后，在仓库中以 editable 模式安装，再通过如下入口训练或播放：

```bash
python scripts/reinforcement_learning/rsl_rl/train.py --task=<TASK_NAME> --headless
python scripts/reinforcement_learning/rsl_rl/play.py --task=<TASK_NAME>
```

训练得到的策略可交由 [rl_sar](https://github.com/fan-ziqi/rl_sar) 做 Gazebo、MuJoCo 仿真验证和真机部署。使用时需保持 robot_lab 配置中的关节顺序与 rl_sar 配置一致。

## 相关链接

- [GitHub 仓库](https://github.com/fan-ziqi/robot_lab)
- [配套部署框架 rl_sar](https://github.com/fan-ziqi/rl_sar)
