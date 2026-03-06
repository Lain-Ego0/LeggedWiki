# Reading List (RL Locomotion / Legged / Humanoids)

> English | [中文](README.md)

This folder collects key papers in legged / humanoid locomotion and related topics, and (when possible) keeps **open-access PDFs** under `recommended-papers/` (preferably arXiv preprints). For works without an open-access PDF, we keep the citation and a note on where to find it.

## Quick Navigation
- [Update / Fetch PDFs](#update-fetch)
- [Technical Direction Index (Quick Lookup)](#tech-index)
- [Notes by Lab/Source (Detailed)](#source-notes)
  - [ETH RSL](#eth-rsl)
  - [KAIST](#kaist)
  - [Other Works](#other-works)
  - [Humanoids](#humanoids)
  - [Surveys](#surveys)
  - [Misc (no notes yet)](#misc)

<a id="update-fetch" name="update-fetch"></a>
## Update / Fetch PDFs
1. Add or edit entries in `reading-list/papers.json`.
2. Run:

```bash
python3 scripts/fetch_open_access_pdfs.py --download
```

Note: the script mainly fetches from arXiv/open-access sources. For items hosted on OpenReview or author pages, you may need to add a more specific query in `papers.json` or download manually into `recommended-papers/` and link it from the corresponding reading-list page.

<a id="tech-index" name="tech-index"></a>
## Technical Direction Index (Quick Lookup)
Note: this is a quick index; for short notes/introductions, see “Notes by Lab/Source (Detailed)” below (when available).

### Surveys / Lectures
- Learning-based legged locomotion: State of the art and future perspectives (IJRR 2025) — [PDF](<../recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf>)
- Robot Dynamics Lecture Notes (2017) — [PDF](<../recommended-papers/ETH-RSL/2017 - Robot Dynamics Lecture Notes.pdf>)

### Model-based Control / Trajectory Optimization
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [PDF](<../recommended-papers/MIT/Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control.pdf>)
- DTC: Deep Tracking Control (Science Robotics 2024) — [PDF](<../recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- [CN] 基于虚拟模型的四足机器人对角小跑步态控制方法 — [PDF](<../recommended-papers/chinese/基于虚拟模型的四足机器人对角小跑步态控制方法.pdf>)
- [CN] 仿生四足机器人多步态规划与控制 — [PDF](<../recommended-papers/chinese/仿生四足机器人多步态规划与控制.pdf>)
- [CN] 基于稳定性的仿生四足机器人控制系统设计（于宪元）— [PDF](<../recommended-papers/chinese/SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计.pdf>)

### Learning-based Locomotion (mostly proprioceptive)
#### Quadrupeds
- Learning agile and dynamic motor skills for legged robots (Science Robotics 2019) — [PDF](<../recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- Learning Quadrupedal Locomotion over Challenging Terrain (Science Robotics 2020) — [PDF](<../recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning (CoRL 2021) — [PDF](<../recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion (RAL 2022) — [PDF](<../recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning (ICRA 2023) — [PDF](<../recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- Learning Quadrupedal Locomotion on Deformable Terrain (Science Robotics 2023) — PDF: not available (try author preprint / public version)
- Rapid Locomotion via Reinforcement Learning (RSS 2022) — [PDF](<../recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf>)

#### Bipeds
- Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (ICRA 2021) — [PDF](<../recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf>)

### Sim-to-Real / Adaptation
- Sim-to-Real: Learning Agile Locomotion for Quadruped Robots (2018) — [PDF](<../recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf>)
- RMA: Rapid Motor Adaptation for Legged Robots (RSS 2021) — [PDF](<../recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf>)

### Perception / Mapping
- Learning robust perceptive locomotion for quadrupedal robots in the wild (Science Robotics 2022) — [PDF](<../recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- Elevation Mapping for Locomotion and Navigation using GPU (IROS 2022) — [PDF](<../recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)

### Motion Priors / Imitation / Style / Foundation Models
- Learning Agile Robotic Locomotion Skills by Imitating Animals (RSS 2020) — [PDF](<../recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf>)
- Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations — [PDF](<../recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf>)
- AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (SIGGRAPH 2021) — [PDF](<../recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf>)
- Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions (ICRA 2022) — [PDF](<../recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf>)
- Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning (ICRA 2023) — [PDF](<../recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (CoRL 2022) — [PDF](<../recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf>)
- A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards (ICRA 2025) — [PDF](<../recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild (RAL 2023) — [PDF](<../recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf>)
- Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models (Nature Machine Intelligence 2023) — [PDF](<../recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf>)

### Parkour / Discrete Terrain / Highly Dynamic Skills
- Learning Agile Locomotion on Risky Terrains (IROS 2024) — [PDF](<../recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (Science Robotics 2024) — [PDF](<../recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- Extreme Parkour with Legged Robots (ICRA 2024) — [PDF](<../recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf>)
- Robot Parkour Learning (CoRL 2024) — [PDF](<../recommended-papers/other/2024 - Robot Parkour Learning.pdf>)
- PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots (RAL 2024) — [PDF](<../recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf>)
- [CN] 四足机器人跳跃步态主动柔顺控制研究 — [PDF](<../recommended-papers/chinese/四足机器人跳跃步态主动柔顺控制研究.pdf>)

### Loco-manipulation / Whole-body
- Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion (CoRL 2022) — [PDF](<../recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf>)
- Visual Whole-Body Control for Legged Loco-Manipulation (CoRL 2024) — [PDF](<../recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf>)
- Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks (CoRL 2023) — PDF: not available (try OpenReview / authors' page)

### Humanoids (Whole-body / Teleop / Getting-up / Generative)
- Expressive Whole-Body Control for Humanoid Robots (RSS 2024) — [PDF](<../recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf>)
- ExBody2: Advanced Expressive Humanoid Whole-Body Control (2024) — [PDF](<../recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf>)
- Open-TeleVision: Teleoperation with Immersive Active Visual Feedback (CoRL 2024) — [PDF](<../recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf>)
- Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control (2024) — [PDF](<../recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf>)
- HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots (ICRA 2025) — [PDF](<../recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf>)
- HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion (2025) — [PDF](<../recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf>)
- Learning Humanoid Standing-up Control across Diverse Postures (RSS 2025) — [PDF](<../recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf>)
- Learning Getting-Up Policies for Real-World Humanoid Robots (RSS 2025) — [PDF](<../recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf>)
- BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (2025) — [PDF](<../recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf>)

### Hardware
- A Low Cost Modular Actuator for Dynamic Robots — [PDF](<../recommended-papers/MIT/MIT - A Low Cost Modular Actuator for Dynamic Robots.pdf>)
- [CN] 新型电驱式四足机器人研制与测试（王兴兴）— [PDF](<../recommended-papers/chinese/新型电驱式四足机器人研制与测试-王兴兴.pdf>)

### Others
- [CN] 四足机器人随笔 — [PDF](<../recommended-papers/chinese/四足机器人随笔.pdf>)

<a id="source-notes" name="source-notes"></a>
## Notes by Lab/Source (Detailed)

<a id="eth-rsl" name="eth-rsl"></a>
### ETH Robotics Systems Lab (RSL)

#### Learning Agile and Dynamic Motor Skills for Legged Robots (Science Robotics 2019)
- PDF: [recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf](<../recommended-papers/ETH-RSL/2019 - Learning agile and dynamic motor skills for legged robots.pdf>)
- Notes: A foundational work for RL-based quadruped locomotion. It trains a motor network model from real data and uses it for sim compensation while training the policy with RL + dynamics randomization. The policy was deployed on ANYmal, demonstrating robust locomotion behaviors (speed tracking, recovery after falls, etc.).

#### Learning Quadrupedal Locomotion over Challenging Terrain (Science Robotics 2020)
- PDF: [recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf](<../recommended-papers/ETH-RSL/2020 - Learning Quadrupedal Locomotion over Challenging Terrain.pdf>)
- Notes: Introduces a two-stage teacher–student framework. The teacher learns with privileged (“cheating”) simulator information; the student (deployable with only history of observable signals) is distilled via online imitation learning (DAgger), using an encoder to infer the implicit privileged information. Also proposes terrain curriculum learning for robust traversal of continuous rough terrains. At this time, the overall control stack is still relatively complex: the network assists with foot trajectory generation and still relies on IK to obtain target joints (vs. many later works that directly output target joint commands).

#### Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning (CoRL 2021)
- PDF: [recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf](<../recommended-papers/ETH-RSL/2021 - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.pdf>)
- Notes: A milestone that accelerated RL-for-robots research. It demonstrates massively parallel training (Isaac Gym) + domain randomization for locomotion, and open-sources the `legged_gym` project.

#### Learning robust perceptive locomotion for quadrupedal robots in the wild (Science Robotics 2022)
- PDF: [recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf](<../recommended-papers/ETH-RSL/2022 - Learning robust perceptive locomotion for quadrupedal robots in the wild.pdf>)
- Notes: Integrates proprioception with exteroceptive vision for robust locomotion, enabling large-scale outdoor walking in challenging conditions (stairs, tunnels, snow, fog, forests, loose rocks, etc.). A good example of learning a locomotion policy that estimates terrain elevation information.

#### Elevation Mapping for Locomotion and Navigation using GPU (IROS 2022)
- PDF: [recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf](<../recommended-papers/ETH-RSL/2022 - Elevation Mapping for Locomotion and Navigation using GPU.pdf>)
- Notes: Proposes an efficient GPU pipeline for building local elevation maps from point clouds and robot pose. In complex environments, odometry drift remains one of the biggest challenges for real-time mapping. Code is open-sourced.

#### Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning (ICRA 2023)
- PDF: [recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf](<../recommended-papers/ETH-RSL/2023 - Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning.pdf>)
- Notes: An enhanced AMP setup that supports multiple discrete styles with switching, demonstrated on a wheeled-legged robot (avoidance, walking, and style switching between quadruped and biped/standing modes). The “learn to get down to quadruped from a reverse-standing (biped) sequence” case is particularly interesting.

#### Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks (CoRL 2023)
- PDF: No open-access PDF was fetched automatically (likely on OpenReview and/or the authors’ website).
- Notes: Key highlight: learns loco-manipulation behaviors on a wheeled-legged robot, using legs as manipulators.

#### Learning Agile Locomotion on Risky Terrains (IROS 2024)
- PDF: [recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf](<../recommended-papers/ETH-RSL/2024 - Learning Agile Locomotion on Risky Terrains.pdf>)
- Notes: An interesting RL locomotion work on discrete “risky” terrains (not omnidirectional walking), with strong demos.

#### ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (Science Robotics 2024)
- PDF: [recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf](<../recommended-papers/ETH-RSL/2024 - ANYmal Parkour- Learning Agile Navigation for Quadrupedal Robots.pdf>)
- Notes: A hierarchical framework with perception (environment reconstruction), navigation (driving skill selection), and motion modules (parkour primitives). One of the first works demonstrating dynamic quadruped parkour-style navigation.

#### DTC: Deep Tracking Control (Science Robotics 2024)
- PDF: [recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf](<../recommended-papers/ETH-RSL/2024 - DTC- Deep Tracking Control.pdf>)
- Notes: Combines model-based and learning-based methods. The upper-level trajectory optimization (TO) layer optimizes body and foot trajectories in real time; a lower-level RL policy tightly tracks those trajectories, enabling precise motion over extreme terrains (stepping stones, trenches, rubble/ruins, etc.). Compared to setups that only do base-velocity tracking, this hierarchical design better leverages legged robots’ ability to choose footholds.

<a id="kaist" name="kaist"></a>
### KAIST (Raibo / Unitree, etc.)

#### Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion (RAL 2022)
- PDF: [recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf](<../recommended-papers/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- Notes: A one-stage asymmetric training setup (not teacher–student). The policy jointly trains a key-state estimator (linear velocity, foot height, contact probability) from history of observable signals, while the critic in simulation uses privileged ground-truth key states. Uses dynamics randomization + PPO and transfers to real robots for robust traversal over continuous rough terrains.

#### DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning (ICRA 2023)
- PDF: [recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf](<../recommended-papers/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- Notes: An asymmetric RL structure where a state estimator infers velocity and implicit terrain latent variables `z` from observable signals (with a VAE-style formulation). Demonstrates robust long-range outdoor locomotion on Unitree A1 and highlights the power of asymmetric actor–critic training in complex environments.

#### Learning Quadrupedal Locomotion on Deformable Terrain (Science Robotics 2023)
- PDF: No open-access PDF was fetched automatically (likely paywalled; try author preprint / arXiv version if available).
- Notes: Modifies RaiSim’s contact dynamics to model granular media / deformable terrain, enabling agile and robust locomotion on soft terrains (e.g., sand, foam pads). Uses an asymmetric training framework, further supporting its effectiveness.

#### A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards (ICRA 2025)
- PDF: [recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf](<../recommended-papers/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- Notes: Introduces relaxed logarithmic barrier functions to design soft-constraint style rewards that guide the robot toward preset motion characteristics (periodicity, joint-range constraints, etc.). Notably, it generates diverse bio-inspired gaits without explicit motion priors; the “human-like walking while standing” and gallop gaits are impressive.

<a id="other-works" name="other-works"></a>
### Other Key Works (Quadrupeds / Bipeds / General)

#### Quadrupeds / Legged Locomotion

##### Sim-to-Real: Learning Agile Locomotion for Quadruped Robots (Minitaur)
- PDF: [recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf](<../recommended-papers/other/2018 - Sim-to-Real- Learning Agile Locomotion For Quadruped Robots.pdf>)
- Notes: An early sim-to-real quadruped RL work (Ghost Robotics Minitaur). Uses RL + an analytical motor model + dynamics randomization to address the transfer gap, inspiring later ANYmal-style pipelines.

##### Learning Agile Robotic Locomotion Skills by Imitating Animals (RSS 2020)
- PDF: [recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf](<../recommended-papers/other/2020 - Learning Agile Robotic Locomotion Skills by Imitating Animals.pdf>)
- Notes: Learns natural animal-style locomotion via motion retargeting + DeepMimic-style motion tracking, demonstrated on early Unitree platforms (e.g., Laikago). Code is open-sourced (UCB).

##### RMA: Rapid Motor Adaptation for Legged Robots (RSS 2021)
- PDF: [recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf](<../recommended-papers/other/2021 - RMA- Rapid Motor Adaptation for Legged Robots.pdf>)
- Notes: Teacher–student with an adaptation module (similar in spirit to ETH’s encoder). Uses random terrain sampling + domain randomization + parallel training in RaiSim, achieving robust continuous-terrain traversal on Unitree A1 without exteroception. Code is open-sourced (CMU).

##### Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (CoRL 2022)
- PDF: [recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf](<../recommended-papers/other/2022 - Walk These Ways- Tuning Robot Control for Generalization with Multiplicity of Behavior.pdf>)
- Notes: A highly tunable and robust locomotion policy on Unitree Go1 with fine-grained controllable parameters: speed, gait (pronking/trotting/bounding/pacing/galloping), step frequency, base height, pitch, contact timing, foot clearance, etc. Code is open-sourced (MIT).

##### Rapid Locomotion via Reinforcement Learning (RSS 2022)
- PDF: [recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf](<../recommended-papers/other/2022 - Rapid Locomotion via Reinforcement Learning.pdf>)
- Notes: Proposes a self-adaptive speed-grid curriculum that pushes the robot’s speed limits based on learned capability, minimizing hand-tuned curricula and expert intervention. Code is open-sourced (MIT).

##### Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions (ICRA 2022)
- PDF: [recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf](<../recommended-papers/other/2022 - Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions.pdf>)
- Notes: One of the first works applying AMP to quadrupeds: combining task reward with style reward can produce natural-looking behaviors without highly engineered reward terms. Code is open-sourced (UCB).

##### Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion (CoRL 2022)
- PDF: [recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf](<../recommended-papers/other/2022 - Deep Whole-Body Control- Learning a Unified Policy for Manipulation and Locomotion.pdf>)
- Notes: Demonstrates arm–leg coordination on Unitree Go1 + a WidowX arm using RL for whole-body loco-manipulation (teleoperation data). Also proposes ROA to estimate environment latent variables online. Built on Isaac Gym + `rsl_rl`, and open-sourced (CMU).

##### Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild (RAL 2023)
- PDF: [recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf](<../recommended-papers/other/2023 - Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild.pdf>)
- Notes: Teacher–student + AMP enables robust continuous-terrain traversal on Unitree Go1 using only proprioception. Natural gait data is generated via trajectory optimization on flat ground. Note: the journal title is “Learning Robust and Agile Legged Locomotion Using Adversarial Motion Priors” (SJTU).

##### Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models (Nature Machine Intelligence 2023)
- PDF: [recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf](<../recommended-papers/other/2023 - Lifelike Agility and Play in Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models.pdf>)
- Notes: Uses generative models to pretrain on large-scale animal motion data, then reuses those skills during environment-level learning. A representative Robotics X (Tencent) work.

##### Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations
- PDF: [recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf](<../recommended-papers/other/Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations.pdf>)
- Notes: Learns dynamic skills from rough/incomplete demonstrations collected via manual operation, including backflip-like behaviors on low-cost platforms.

##### Extreme Parkour with Legged Robots (ICRA 2024)
- PDF: [recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf](<../recommended-papers/other/2024 - Extreme Parkour with Legged Robots.pdf>)
- Notes: Pushes Unitree A1’s rough-terrain capabilities with domain randomization + exteroception; demonstrates box jumping, vaulting, squeezing through gaps, etc. (CMU/Stanford+ collaborators).

##### Robot Parkour Learning (CoRL 2024)
- PDF: [recommended-papers/other/2024 - Robot Parkour Learning.pdf](<../recommended-papers/other/2024 - Robot Parkour Learning.pdf>)
- Notes: A concurrent line of work with similar goals: parkour-style locomotion with domain randomization + exteroception (CoRL 2024).

##### Visual Whole-Body Control for Legged Loco-Manipulation (CoRL 2024)
- PDF: [recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf](<../recommended-papers/other/2024 - Visual Whole-Body Control for Legged Loco-Manipulation.pdf>)
- Notes: Demonstrates vision-driven hierarchical policies (imitation learning + RL) for mobile manipulation on Unitree B1 + Z1 arm via sim-to-real. Built on Isaac Gym + `rsl_rl`, and open-sourced (UCSD).

##### PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots (RAL 2024)
- PDF: [recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf](<../recommended-papers/other/2024 - PIE- Parkour with Implicit-Explicit Learning Framework for Legged Robots.pdf>)
- Notes: A “plus” version that further improves dynamic parkour performance and transfers to outdoor settings (ZJU).

#### Bipeds / General

##### Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (ICRA 2021)
- PDF: [recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf](<../recommended-papers/other/2021 - Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.pdf>)
- Notes: Defines common gaits (standing, walking, jumping, running, hopping) via probabilistic periodic reward composition and demonstrates on Cassie. Includes both single-gait policies and a gait-switching policy.

##### AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (SIGGRAPH 2021)
- PDF: [recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf](<../recommended-papers/other/2021 - AMP- Adversarial Motion Priors for Stylized Physics-Based Character Control.pdf>)
- Notes: Not a legged-robot paper, but highly transferable: uses a GAN-based implicit metric to provide style rewards for learning control policies (UCB).

<a id="humanoids" name="humanoids"></a>
### Humanoids (Whole-Body Control / Teleop / Getting-Up, etc.)

#### Expressive Whole-Body Control for Humanoid Robots (RSS 2024)
- PDF: [recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf](<../recommended-papers/humanoid/2024 - Expressive Whole-Body Control for Humanoid Robots.pdf>)
- Notes: Learns humanoid motion sequences via motion retargeting (UCSD).

#### ExBody2: Advanced Expressive Humanoid Whole-Body Control (2024)
- PDF: [recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf](<../recommended-papers/humanoid/2024 - ExBody2- Advanced Expressive Humanoid Whole-Body Control.pdf>)
- Notes: A follow-up work to Expressive Whole-Body Control (2024).

#### Open-TeleVision: Teleoperation with Immersive Active Visual Feedback (CoRL 2024)
- PDF: [recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf](<../recommended-papers/humanoid/2024 - Open-TeleVision- Teleoperation with Immersive Active Visual Feedback.pdf>)
- Notes: An open-source VR teleoperation framework for humanoids (upper body only).

#### Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control (2024)
- PDF: [recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf](<../recommended-papers/humanoid/2024 - Mobile-TeleVision- Predictive Motion Priors for Humanoid Whole-Body Control.pdf>)
- Notes: Demonstrates a whole-body control approach that extends Open-TeleVision, with a locomotion controller that leverages ideas related to ExBody (2024).

#### HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots (ICRA 2025)
- PDF: [recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf](<../recommended-papers/humanoid/2025 - HOVER- Versatile Neural Whole-Body Controller for Humanoid Robots.pdf>)
- Notes: Unifies several whole-body control target types (root velocity tracking, joint-angle tracking, key-point tracking, etc.) (CMU).

#### HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion (2025)
- PDF: [recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf](<../recommended-papers/humanoid/2025 - HugWBC- A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion.pdf>)
- Notes: A “humanoid version” of Walk These Ways: fine-grained gait tuning over continuous terrains (gait type, step frequency, base height, pitch, contact timing, foot clearance, etc.). Notable for natural gaits induced by polynomial foot-trajectory rewards and extensibility via curricula that bring in upper-body freedom (SJTU / Shanghai AI Lab).

#### Learning Humanoid Standing-up Control across Diverse Postures (RSS 2025)
- PDF: [recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf](<../recommended-papers/humanoid/2025 - Learning Humanoid Standing-up Control across Diverse Postures.pdf>)
- Notes: Strong getting-up behaviors across diverse postures (Shanghai AI Lab).

#### Learning Getting-Up Policies for Real-World Humanoid Robots (RSS 2025)
- PDF: [recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf](<../recommended-papers/humanoid/2025 - Learning Getting-Up Policies for Real-World Humanoid Robots.pdf>)
- Notes: A concurrent getting-up policy work (UIUC).

#### BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (2025)
- PDF: [recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf](<../recommended-papers/humanoid/2025 - BeyondMimic- From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.pdf>)
- Notes: High-quality motion tracking plus guided diffusion; supports test-time task-specific control using simple cost functions (Berkeley/Stanford).

<a id="surveys" name="surveys"></a>
### Surveys

#### Learning-based legged locomotion: State of the art and future perspectives (IJRR 2025)
- PDF: [recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf](<../recommended-papers/surveys/2025 - Learning-based legged locomotion- State of the art and future perspectives.pdf>)
- Notes: A survey of learning-based legged locomotion control, summarizing recent academic and industrial progress and outlining future directions (Georgia Tech).

<a id="misc" name="misc"></a>
### Misc (no notes yet)
- Robot Dynamics Lecture Notes (2017) — [PDF](<../recommended-papers/ETH-RSL/2017 - Robot Dynamics Lecture Notes.pdf>)
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [PDF](<../recommended-papers/MIT/Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control.pdf>)
- A Low Cost Modular Actuator for Dynamic Robots — [PDF](<../recommended-papers/MIT/MIT - A Low Cost Modular Actuator for Dynamic Robots.pdf>)
- [CN] 四足机器人随笔 — [PDF](<../recommended-papers/chinese/四足机器人随笔.pdf>)
- [CN] 新型电驱式四足机器人研制与测试-王兴兴 — [PDF](<../recommended-papers/chinese/新型电驱式四足机器人研制与测试-王兴兴.pdf>)
- [CN] 四足机器人跳跃步态主动柔顺控制研究 — [PDF](<../recommended-papers/chinese/四足机器人跳跃步态主动柔顺控制研究.pdf>)
- [CN] 仿生四足机器人多步态规划与控制 — [PDF](<../recommended-papers/chinese/仿生四足机器人多步态规划与控制.pdf>)
- [CN] 基于虚拟模型的四足机器人对角小跑步态控制方法 — [PDF](<../recommended-papers/chinese/基于虚拟模型的四足机器人对角小跑步态控制方法.pdf>)
- [CN] SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计 — [PDF](<../recommended-papers/chinese/SY1807103-于宪元-基于稳定性的仿生四足机器人控制系统设计.pdf>)
