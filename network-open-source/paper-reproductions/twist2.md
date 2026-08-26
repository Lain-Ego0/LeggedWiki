# TWIST2：可扩展的人形机器人数据采集系统

> 类型：人形机器人 / VR 遥操作 / 数据采集 / G1

## 项目简介

[TWIST2](https://github.com/amazon-far/TWIST2) 是 TWIST 的后续数据采集系统，目标是以更具可扩展性和可移植性的方式采集全身人形机器人数据。当前开源代码支持通过 PICO VR 头显，经有线连接控制 Unitree G1，并覆盖仿真、真机和遥操作数据采集流程。

项目将控制器训练/部署与在线动作重定向拆分为 `twist2` 和 `gmr` 两个 Conda 环境，使用 Redis 进行高低层服务通信，并提供示例动作、预训练 ONNX 控制器和 TWIST2 数据集。高层策略学习代码计划在独立仓库发布。

## 注意事项

README 说明当前仍在完善机载流式传输和推理代码，完整遥操作流程需要 PICO SDK、GMR、Redis 及 Unitree SDK 配置。真机运行前必须先完成仿真测试和急停保护。

## 相关链接

- [GitHub 仓库](https://github.com/amazon-far/TWIST2)
- [项目主页](https://yanjieze.com/TWIST2)
- [论文](https://arxiv.org/abs/2511.02832)
- [GMR 动作重定向](https://github.com/YanjieZe/GMR)
