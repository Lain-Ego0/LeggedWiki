# Extreme-RGMT：高动态通用人形控制方案复现

> 类型：论文复现 / 训练经验分享

## 项目简介

本项目复现的论文是 **Extreme-RGMT: Continual Learning of Highly Dynamic Skills for Robust Generalist Humanoid Control**，面向高动态人形机器人全身控制，支持后空翻等高动态动作，也支持跌倒恢复。

从论文项目主页介绍来看，Extreme-RGMT 采用“两阶段持续学习”思路：先使用多来源动作数据训练通用的动作跟踪基础策略，再在学习新技能时约束已经掌握的能力，同时重点采样困难的动态片段。针对高动态动作样本少、失败率高的问题，方法还结合了难度感知采样和基于优势的轨迹重采样。项目主页展示了高动态、低动态以及失败动作等多组视频，适合用来对照复现效果。

论文项目主页：

- [Extreme-RGMT Project Page](https://zeonsunlightyu.github.io/Extreme-RGMT.github.io/)

## 训练配置与效果

本次复现使用 **4 × RTX 2080 Ti**，并行环境数量为 **4096 environments**。

根据实际训练情况：

- 训练约 2 天，可以达到视频中展示的效果；
- 如果不追求后空翻等极高动态动作，训练约 1 天就能看到较好的效果；
- 以该训练规模推测，单张 RTX 4090 应足以完成训练；
- 整体算力门槛相对较低，属于比较亲民的高动态全身控制方案。

这里的训练时长和显卡结论是本次复现者的实测经验，不等同于论文作者给出的统一硬件要求；实际速度仍会受到动作数据规模、环境配置和训练目标影响。

## Motion 数据

基础 Motion 数据主要参考原论文，使用 **LAFAN1** 与 **AMASS**。

针对后空翻等高动态动作，额外加入了：

- SONIC 开源 Bone-Seed 数据中的后空翻动作；
- 青瞳开源数据中的后空翻部分；
- [LAFAN1 Retargeting Dataset](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)；
- [MotionDecode Dataset](https://huggingface.co/datasets/CMRobot/MotionDecode)。

Motion 数据在训练前仍需要筛选和清洗，并不是所有动作都适合直接用于训练。

论文主页强调了多来源动作数据与困难片段重采样的重要性。因此，后空翻数据的补充只是数据准备的一部分，训练前还需要检查动作与目标机器人形态的匹配、重定向质量、姿态连续性以及是否存在不适合当前控制器的片段。

## Motion 可视化工具

为了快速查看、筛选和检查 Motion 数据，可以使用在线可视化工具：

- [Motion 在线可视化工具](https://motion.enkeebot.com/)

该工具可以直接对 Motion 数据进行可视化，有助于检查动作质量和筛选训练数据。

## 相关视频

- [【复现】穷鬼方案-单卡训出可以空翻的通用模型](https://www.bilibili.com/video/BV1jGhG6rEpy/?share_source=copy_web&vd_source=ba8eb7d61bec067d23f755ba4fb55f78)
