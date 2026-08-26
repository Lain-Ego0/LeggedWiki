# Go2：可控跳跃与 Sim2Sim 差异实验

> 类型：四足机器人 / 跳跃控制 / Isaac Gym / MuJoCo

## 项目简介

这是基于 [My_unitree_go2_gym](https://github.com/yusongmin1/My_unitree_go2_gym) 的 Go2 跳跃实验。项目将多个运动控制任务放在同一个 legged_gym 风格框架中，包含普通 PPO、DreamWaQ、AMP 和 CTS 等方法。

## 实验观察

投稿者关注到：在加速度较大的任务中，Isaac Gym 训练出的策略迁移到 MuJoCo 往往比较困难。本次实验中，策略在 MuJoCo 中如果不做力矩限制会翻倒，但部署到实物时不加力矩限制反而可以正常跳出。

这个结果说明仿真器之间的差异不能只靠“能否运行”判断。接触模型、执行器、关节阻尼、控制频率、力矩裁剪和碰撞处理都可能影响高动态动作；MuJoCo 中的失败也不必然意味着实物一定失败，反之亦然。

## 仓库任务

仓库的标准 PPO 任务包括 `go2_jump`、`go2_spring_jump`、`go2_backflip`、`go2_handstand` 和 `go2_leggedstand`，同时包含 `go2_stairs_dreamwaq`、AMP、CTS 和 teacher-student 任务。项目流程覆盖 Train、Play、Sim2Sim 和 Sim2Real。

## 复现建议

进行跳跃任务时，应同时记录 Isaac Gym 和 MuJoCo 的动作输出、关节力矩、接触力、基座姿态和控制周期，并检查两边的模型参数是否一致。不要把某个仿真器中的力矩限制直接当作真实机器人的安全边界，真机测试仍需单独进行保护和限幅验证。

## 相关链接

- [项目仓库](https://github.com/yusongmin1/My_unitree_go2_gym)
- [投稿视频](https://www.bilibili.com/video/BV1Q7JkzzEZo/)
