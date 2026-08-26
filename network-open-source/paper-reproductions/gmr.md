# GMR：通用实时动作重定向

> 类型：动作重定向 / 人形机器人 / CPU 实时推理

## 项目简介

[GMR](https://github.com/YanjieZe/GMR)（General Motion Retargeting，ICRA 2026）将人体动作实时重定向到多种人形机器人，定位是 [TWIST](https://github.com/YanjieZe/TWIST) 的动作重定向器。项目支持从 SMPL-X 等人体姿态数据生成机器人关节轨迹，并提供面向不同机器人形态的 IK 配置。

GMR 的特点是可在 CPU 上实时运行，适合与动作捕捉、遥操作和下游模仿学习策略连接。使用时需根据目标机器人的关节、连杆名称和坐标系准备对应配置。

## 相关链接

- [GitHub 仓库](https://github.com/YanjieZe/GMR)
- [TWIST 全身模仿系统](https://github.com/YanjieZe/TWIST)
- [GMR 文档](https://github.com/YanjieZe/GMR/blob/master/DOC.md)
