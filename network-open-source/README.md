# 网络开源项目

> 中文 | [English](README.en.md)

## 独立项目文章

以下项目已整理为独立文章，便于记录项目背景、代码入口、训练配置和使用注意事项。

| 项目 | 类型 | 入口 | 简介 |
| :--- | :--- | :--- | :--- |
| [Extreme-RGMT 复现](extreme-rgmt-reproduction.md) | 论文复现 | [Project Page](https://zeonsunlightyu.github.io/Extreme-RGMT.github.io/) | 面向后空翻、跌倒恢复等高动态动作的人形全身控制方案 |
| [七轴双臂机械臂实车控制](humanoid-seven-axis-arm-control.md) | 方案分享 | [论坛原帖](https://bbs.robomaster.com/article/1941628?source=1#head0) | 包含冗余逆解、加权 DLS、重力补偿和分层控制 |
| [RC_WheelLeg](rc-wheelleg.md) | 轮足机器人开源 | [GitHub](https://github.com/zeitvex/RC_WheelLeg) | HYNova 战队的轮足机器人、ROS 2 和强化学习项目 |
| [blender-mujoco-terrain](blender-mujoco-hfield.md) | 工具插件 | [GitHub](https://github.com/Eterith/blender-mujoco-hfield/tree/main) | Blender 到 MuJoCo height field、网格和碰撞体导出工具 |
| [福州大学浮舟湿地点足 12DOF](fuzhou-quadruped-robot-lab.md) | 四足强化学习 | [GitHub](https://github.com/Taojunfeng123/quadruped_robot_lab) | 点足 12DOF 四足机器人的 RL 训练代码 |
| [南华大学衡山Π串联四足](nhu-himloco-quadruped.md) | 四足 Sim2Real | [GitHub](https://github.com/uwvwko-zzz/uw-himloco) | HIMLOCO 训练框架与 himdog 部署代码 |
| [SMP 分数匹配运动先验](smp-score-matching-motion-priors.md) | 运动先验 / RL | [GitHub](https://github.com/SUZ-tsinghua/smp) | 将冻结的扩散模型作为可复用运动奖励，引导 G1 学习自然动作 |
| [AMP Go2 楼梯实验](go2-amp-stairs.md) | AMP / 楼梯越障 | [GitHub](https://github.com/ak1raljl/amp_go2) | 基于 AMP 的 Go2 楼梯地形复现实验 |
| [M20 DreamWaQ 盲爬高台](m20-dreamwaq-highplatform.md) | DreamWaQ / 轮足 | [GitHub](https://github.com/yusongmin1/Dreamwaq/tree/highplatform) | 通过课程学习训练 M20 不依赖视觉爬高台 |
| [HIMLoco for Go2W](himloco-go2w.md) | 四轮足 / RL | [GitHub](https://github.com/TrackinBIT/HIMLoco-for-Go2W) | 基于 HIMLoco 的 Go2W Isaac Gym 训练和 MuJoCo 验证 |
| [Go2 可控跳跃](go2-controllable-jump.md) | 跳跃 / Sim2Sim | [GitHub](https://github.com/yusongmin1/My_unitree_go2_gym) | 对比高加速度任务在 Isaac Gym、MuJoCo 与实物间的差异 |
| [LeggedSkillDeploy](leggedskilldeploy.md) | 部署框架 | [GitHub](https://github.com/haozhang04/LeggedSkillDeploy) | 面向多种腿足机器人和多策略切换的部署框架 |
| [LeggedGym-Ex](leggedgym-ex.md) | 多仿真器 RL 框架 | [GitHub](https://github.com/lupinjia/LeggedGym-Ex) | 将 legged_gym 扩展到 Isaac Gym、Genesis 和 Isaac Sim |
| [Go2 深度图跑酷](go2-depth-parkour.md) | 深度感知 / 跑酷 | [GitHub](https://github.com/lupinjia/LeggedGym-Ex/tree/main/legged_gym/envs/go2/go2_ts_depth) | LeggedGym-Ex 中的 Go2 深度图任务示例 |
| [AMP Go2 基础复现](amp-go2.md) | AMP / 四足模仿 | [GitHub](https://github.com/ak1raljl/amp_go2) | Go2 AMP 训练、动作数据、Sim2Sim 和 Sim2Real 基础流程 |
| [Go2 空翻数据采集](go2-flip-data-collection.md) | 轨迹优化 / 动作数据 | [GitHub](https://github.com/yusongmin1/go2_flip_TO) | 基于 SE(3) 全身轨迹优化生成 Go2 空翻动作数据 |
| [Go2 Trot 步态控制](go2-trot-gait-control.md) | Trot / 步态控制 | [GitHub](https://github.com/yusongmin1/My_unitree_go2_gym) | 控制小跑步态频率与 10/20 cm 抬脚高度 |
| [Go2 梅花桩跑酷](go2-plum-blossom-parkour.md) | 复杂地形 / RL | [GitHub](https://github.com/jindadu00/legged_robot_competition) | 基于 Isaac Gym 的梅花桩课程学习与分层策略实验 |
| [RoboGauge Go2 冠军方案](robogauge-go2-champion.md) | MoE / 评测 / Sim2Real | [Project Page](https://robogauge.github.io/complete/) | Go2 高鲁棒运动控制、自动评测和多策略部署方案 |

## 实物开源
| 平台 | 作者/上传者 | 项目 | 链接 | 一句话简介 |
| :--- | :--- | :--- | :--- | :--- |
| Github | michaelkubina | SpotMicroESP32 | [SpotMicroESP32](https://github.com/michaelkubina/SpotMicroESP32) | 很经典的仿 spot 关节直驱舵狗，复刻难度较低 |
| Github | 华北舵狗王/golaced | MocoMoco_Software | [MocoMoco_Software](https://github.com/golaced/MocoMoco_Software) | 狗王早期 MocoMoco 四足机器人项目的开源程序，修改自飞控 |
| Github | 华北舵狗王/golaced | Moco-Minitaur-LTS- | [Moco-Minitaur-LTS-](https://github.com/golaced/Moco-Minitaur-LTS-) | 狗王对 Minitaur 项目的复刻，驱动器为 Odrive，并联力控 |
| Github | ToanTech | py-apple-bldc-quadruped-robot | [py-apple-bldc-quadruped-robot](https://github.com/ToanTech/py-apple-bldc-quadruped-robot) | 灯哥的同轴四连杆并联无刷狗 |
| Github | ToanTech | py-apple-structure | [py-apple-structure](https://github.com/ToanTech/py-apple-structure) | 灯哥菠萝狗机械结构 |
| Github | ToanTech | py-apple-controller | [py-apple-controller](https://github.com/ToanTech/py-apple-controller) | 灯哥菠萝狗控制软件 |
| Github | ToanTech | py-apple-dynamics | [py-apple-dynamics](https://github.com/ToanTech/py-apple-dynamics) | 灯哥菠萝狗控制器 |
| Github | Nate711 | StanfordDoggoProject | [StanfordDoggoProject](https://github.com/Nate711/StanfordDoggoProject) | Odrive + 同步带 + 轴套轴的斯坦福八自由度小狗 |
| Github | mangdangroboticsclub | QuadrupedRobot | [QuadrupedRobot](https://github.com/mangdangroboticsclub/QuadrupedRobot) | 小贵的玩具小狗，没有复刻必要 |
| Github | lshil00 | Quadruped_robot | [Quadruped_robot](https://github.com/lshil00/Quadruped_robot) | 设计精致的十二自由度舵机狗，国人毕设，完成度高 |
| Github | XRobots | openDogV3 | [openDogV3](https://github.com/XRobots/openDogV3) | 小型无刷内膝肘，设计有趣 |
| Github | fgrimminger | open_robot_actuator_hardware | [open_robot_actuator_hardware](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware) | Open Dynamic Robot Initiative 核心硬件开源仓库，复现较多 |
| 嘉立创开源广场 | 有大饼的魔法少女 | 旺财-仿生四足机器狗 | [旺财-仿生四足机器狗](https://oshwhub.com/gulu666/detector-disaster-scene-3d-reconstruction-robot-dog) | 完成度高，设计合理，只可惜小米电机停产了 |
| 嘉立创开源广场 | hua | 并联臂四足机器狗 | [并联臂四足机器狗](https://oshwhub.com/cdm0302/parallel-arm-quadruped-robot-dog) | 舵机方案，基础五连杆四足，预算有限可参考 |
| 嘉立创开源广场 | Forairaaaaa | 基于 ESP-32 的四足机器狗~ | [基于 ESP-32 的四足机器狗~](https://oshwhub.com/eedadada/bakery-zhu-kong-long-gu-zhai-jia) | 集成度不错的简易五连杆舵机狗，适合练手 |
| Gitee | 华北舵狗王/OmniBotLab机器人实验室 | Tinymal-Pholcus | [Tinymal-Pholcus](https://gitee.com/tinymal/tinymal-pholcus-t) | 八自由度并联，典型同轴五连杆，管夹固定非优解 |
| Gitee | 华北舵狗王/OmniBotLab机器人实验室 | Tinymal-B 四足机器人 | [Tinymal-B 四足机器人](https://gitee.com/tinymal/tinymal-b-quadruped-robot) | Anymal 小型化思路，但使用电机扭矩偏小，结构可参考 |
| Gitee | 华北舵狗王/OmniBotLab机器人实验室 | Tinymal-Spirit40 | [Tinymal-Spirit40](https://gitee.com/tinymal/tinymal-spirit40-t) | 使用同步带的十二自由度中型全肘式四足 |
| Gitee | 华北舵狗王/OmniBotLab机器人实验室 | OmniBotSeries_Tinker | [OmniBotSeries_Tinker](https://gitee.com/tinymal/omni-bot-series_-tinker) | 类迪士尼仿鸵鸟造型双足 |
| Gitee | 华北舵狗王/OmniBotLab机器人实验室 | SimpleMan | [SimpleMan](https://gitee.com/tinymal/simple-man-s) | 较早期粗糙的双足，参考价值不大 |
| Others | Nathan Kau | Stanford Pupper | [Stanford Pupper](https://pupper.readthedocs.io/en/latest/) | 很著名的斯坦福舵机狗 |
| Others | 高擎机电 | HTM5046版本四足机器人 | [HTM5046版本四足机器人](https://www.hightorque.cn/category/service) | 基于 HTM5046 电机，高擎自家产品 |

## 框架开源
| 平台 | 作者/上传者 | 项目 | 链接 | 一句话简介 |
| :--- | :--- | :--- | :--- | :--- |
| Github | fan-ziqi | rl_sar | [rl_sar](https://github.com/fan-ziqi/rl_sar) | 国人制作的强化学习算法框架，同时支持仿真验证与实物部署 |
| Github | chvmp | champ | [champ](https://github.com/chvmp/champ) | 比较有年头的开发框架 |
| Github | real-stanford | umi-on-legs | [umi-on-legs](https://umi-on-legs.github.io/) | 将现实世界和模拟数据相结合的四足机器人操纵系统新框架 |
| Github | silvery107 | rl-mpc-locomotion | [rl-mpc-locomotion](https://github.com/silvery107/rl-mpc-locomotion/tree/main) | 结合高层策略网络和低层模型预测控制器的训练框架 |
| Github | qiayuanl | legged_control | [legged_control](https://github.com/qiayuanl/legged_control) | 目前移植性与性能较好的开源 MPC 框架 |
| Github | mit-biomimetics | Cheetah-Software | [Cheetah-Software](https://github.com/mit-biomimetics/Cheetah-Software) | 经典 MIT 软件算法框架 |
| Github | robomechanics | quad-sdk | [quad-sdk](https://github.com/robomechanics/quad-sdk) | 相较 MIT 框架增加全局轨迹规划与局部足底落点规划 |
| Github | erwincoumans | motion_imitation | [motion_imitation](https://github.com/erwincoumans/motion_imitation) | 高可读性的模仿学习与 MPC 控制器 |
| Github | ShuoYangRobotics | A1-QP-MPC-Controller | [A1-QP-MPC-Controller](https://github.com/ShuoYangRobotics/A1-QP-MPC-Controller) | MIT 算法思路在宇树 A1 上的实现 |
