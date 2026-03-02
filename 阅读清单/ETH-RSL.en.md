# ETH Robotics Systems Lab (RSL)

[中文（默认）](ETH-RSL.md) | English

## Learning Agile and Dynamic Motor Skills for Legged Robots (Science Robotics 2019)
- PDF: [推荐论文/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf](<../推荐论文/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- Notes: A foundational work for RL-based quadruped locomotion. It trains a motor network model from real data and uses it for sim compensation while training the policy with RL + dynamics randomization. The policy was deployed on ANYmal, demonstrating robust locomotion behaviors (speed tracking, recovery after falls, etc.).

## Learning Quadrupedal Locomotion over Challenging Terrain (Science Robotics 2020)
- PDF: [推荐论文/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf](<../推荐论文/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- Notes: Introduces a two-stage teacher–student framework. The teacher learns with privileged (“cheating”) simulator information; the student (deployable with only history of observable signals) is distilled via online imitation learning (DAgger), using an encoder to infer the implicit privileged information. Also proposes terrain curriculum learning for robust traversal of continuous rough terrains. At this time, the overall control stack is still relatively complex: the network assists with foot trajectory generation and still relies on IK to obtain target joints (vs. many later works that directly output target joint commands).

## Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning (CoRL 2021)
- PDF: [推荐论文/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf](<../推荐论文/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- Notes: A milestone that accelerated RL-for-robots research. It demonstrates massively parallel training (Isaac Gym) + domain randomization for locomotion, and open-sources the `legged_gym` project.

## Learning robust perceptive locomotion for quadrupedal robots in the wild (Science Robotics 2022)
- PDF: [推荐论文/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf](<../推荐论文/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- Notes: Integrates proprioception with exteroceptive vision for robust locomotion, enabling large-scale outdoor walking in challenging conditions (stairs, tunnels, snow, fog, forests, loose rocks, etc.). A good example of learning a locomotion policy that estimates terrain elevation information.

## Elevation Mapping for Locomotion and Navigation using GPU (IROS 2022)
- PDF: [推荐论文/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf](<../推荐论文/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)
- Notes: Proposes an efficient GPU pipeline for building local elevation maps from point clouds and robot pose. In complex environments, odometry drift remains one of the biggest challenges for real-time mapping. Code is open-sourced.

## Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning (ICRA 2023)
- PDF: [推荐论文/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf](<../推荐论文/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- Notes: An enhanced AMP setup that supports multiple discrete styles with switching, demonstrated on a wheeled-legged robot (avoidance, walking, and style switching between quadruped and biped/standing modes). The “learn to get down to quadruped from a reverse-standing (biped) sequence” case is particularly interesting.

## Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks (CoRL 2023)
- PDF: No open-access PDF was fetched automatically (likely on OpenReview and/or the authors’ website).
- Notes: Key highlight: learns loco-manipulation behaviors on a wheeled-legged robot, using legs as manipulators.

## Learning Agile Locomotion on Risky Terrains (IROS 2024)
- PDF: [推荐论文/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf](<../推荐论文/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- Notes: An interesting RL locomotion work on discrete “risky” terrains (not omnidirectional walking), with strong demos.

## ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (Science Robotics 2024)
- PDF: [推荐论文/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf](<../推荐论文/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- Notes: A hierarchical framework with perception (environment reconstruction), navigation (driving skill selection), and motion modules (parkour primitives). One of the first works demonstrating dynamic quadruped parkour-style navigation.

## DTC: Deep Tracking Control (Science Robotics 2024)
- PDF: [推荐论文/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf](<../推荐论文/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- Notes: Combines model-based and learning-based methods. The upper-level trajectory optimization (TO) layer optimizes body and foot trajectories in real time; a lower-level RL policy tightly tracks those trajectories, enabling precise motion over extreme terrains (stepping stones, trenches, rubble/ruins, etc.). Compared to setups that only do base-velocity tracking, this hierarchical design better leverages legged robots’ ability to choose footholds.

