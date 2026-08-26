# Go2 Trot：步态频率与抬脚高度控制

> 类型：四足机器人 / Trot 步态 / 参数化控制

## 项目简介

这是 [My_unitree_go2_gym](https://github.com/yusongmin1/My_unitree_go2_gym) 中的 Trot 步态实验，目标是让 Go2 以小跑步态行走，并能够调节步态频率和抬脚高度。

投稿记录中给出了约 10 cm、20 cm 两档抬脚高度示例。作者在 2025 年 9 月 22 日对代码进行了重构，但当时重构后的版本尚未发布，因此文章只记录已公开仓库和投稿内容，不把未发布代码描述为当前可用接口。

## 仓库背景

该仓库将普通 PPO、DreamWaQ、AMP 和 CTS 等算法统一放在 Go2 强化学习示例中，除 `go2_trot` 外还包括跳跃、空翻、倒立、复杂地形和 teacher-student 任务。

Trot 步态实验适合用来理解步态周期、足端轨迹、摆动相与支撑相之间的关系。若要把频率和抬脚高度用于实机，还需要同步检查速度命令、关节限位、足端碰撞和动作变化率。

## 相关链接

- [项目仓库](https://github.com/yusongmin1/My_unitree_go2_gym)
- [投稿视频](https://www.bilibili.com/video/BV15zufzPEzA/)
