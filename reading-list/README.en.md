# Paper Study Hub (Reading List + Recommended Papers)

> English | [中文](README.md)

This folder is the unified entry for the paper module: technical-direction index, key paper notes, and maintenance workflow. Paper PDFs are not stored in this repository; entries point to original sources.

## Quick Navigation
- [Update original links](#update-fetch)
- [Technical Direction Index (Quick Lookup)](#tech-index)
- [Notes by Lab/Source (Detailed)](#source-notes)
  - [ETH RSL](#eth-rsl)
  - [KAIST](#kaist)
  - [Other Works](#other-works)
  - [Humanoids](#humanoids)
  - [Surveys](#surveys)
  - [Misc (no notes yet)](#misc)

<a id="update-fetch" name="update-fetch"></a>
## Update original links
1. Add or edit entries in `reading-list/papers.json`.
2. Resolve original links and write them back into the index (`url` field; prefers public sources and falls back to a landing page):

```bash
python3 scripts/resolve_paper_links.py --update-index
```
3. Keep README entries linked to the original source; do not add local PDF mirrors.

Note: the script resolves original links from arXiv/open-access sources. For items it cannot resolve (e.g., Chinese theses, paywalled journal papers), add a `url` field manually in `papers.json`.

<a id="tech-index" name="tech-index"></a>
## Technical Direction Index (Quick Lookup)
Note: this is a quick index; for short notes/introductions, see “Notes by Lab/Source (Detailed)” below (when available).

### Surveys / Lectures
- Learning-based legged locomotion: State of the art and future perspectives (IJRR 2025) — [Original PDF](https://arxiv.org/pdf/2406.01152.pdf)
- Robot Dynamics Lecture Notes (2017) — [Original PDF](https://rsl.ethz.ch/education-students/lectures/robotdynamics.html)

### Model-based Control / Trajectory Optimization
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [Original PDF](https://dspace.mit.edu/handle/1721.1/138000.2)
- DTC: Deep Tracking Control (Science Robotics 2024) — [Original PDF](https://arxiv.org/pdf/2309.15462.pdf)

### Learning-based Locomotion (mostly proprioceptive)
#### Quadrupeds
- Learning agile and dynamic motor skills for legged robots (Science Robotics 2019) — [Original PDF](https://arxiv.org/pdf/1901.08652.pdf)
- Learning Quadrupedal Locomotion over Challenging Terrain (Science Robotics 2020) — [Original PDF](https://arxiv.org/pdf/2010.11251.pdf)
- Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning (CoRL 2021) — [Original PDF](https://arxiv.org/pdf/2109.11978)
- Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion (RAL 2022) — [Original PDF](https://arxiv.org/pdf/2202.05481.pdf)
- DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning (ICRA 2023) — [Original PDF](https://arxiv.org/pdf/2301.10602.pdf)
- Learning Quadrupedal Locomotion on Deformable Terrain (Science Robotics 2023) — [Original (journal page)](https://doi.org/10.1126/scirobotics.ade2256) (no public PDF; try author preprint)
- Rapid Locomotion via Reinforcement Learning (RSS 2022) — [Original PDF](https://arxiv.org/pdf/2205.02824.pdf)

#### Bipeds
- Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (ICRA 2021) — [Original PDF](https://arxiv.org/pdf/2011.01387.pdf)

### Sim-to-Real / Adaptation
- Sim-to-Real: Learning Agile Locomotion for Quadruped Robots (2018) — [Original PDF](https://arxiv.org/pdf/1804.10332.pdf)
- RMA: Rapid Motor Adaptation for Legged Robots (RSS 2021) — [Original PDF](https://arxiv.org/pdf/2107.04034.pdf)

### Perception / Mapping
- Learning robust perceptive locomotion for quadrupedal robots in the wild (Science Robotics 2022) — [Original PDF](https://arxiv.org/pdf/2201.08117)
- Elevation Mapping for Locomotion and Navigation using GPU (IROS 2022) — [Original PDF](https://arxiv.org/pdf/2204.12876)

### Motion Priors / Imitation / Style / Foundation Models
- Learning Agile Robotic Locomotion Skills by Imitating Animals (RSS 2020) — [Original PDF](https://arxiv.org/pdf/2004.00784.pdf)
- Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations — [Original PDF](https://arxiv.org/pdf/2206.11693.pdf)
- AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (SIGGRAPH 2021) — [Original PDF](https://arxiv.org/pdf/2104.02180.pdf)
- Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions (ICRA 2022) — [Original PDF](https://arxiv.org/pdf/2203.15103.pdf)
- Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning (ICRA 2023) — [Original PDF](https://arxiv.org/pdf/2203.14912)
- Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (CoRL 2022) — [Original PDF](https://arxiv.org/pdf/2212.03238.pdf)
- A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards (ICRA 2025) — [Original PDF](https://arxiv.org/pdf/2409.15780.pdf)
- Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild (RAL 2023) — [Original PDF](https://arxiv.org/pdf/2304.10888.pdf)
- Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models (Nature Machine Intelligence 2023) — [Original PDF](https://arxiv.org/pdf/2308.15143.pdf)

### Parkour / Discrete Terrain / Highly Dynamic Skills
- Learning Agile Locomotion on Risky Terrains (IROS 2024) — [Original PDF](https://arxiv.org/pdf/2311.10484.pdf)
- ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (Science Robotics 2024) — [Original PDF](https://arxiv.org/pdf/2306.14874.pdf)
- Extreme Parkour with Legged Robots (ICRA 2024) — [Original PDF](https://arxiv.org/pdf/2309.14341.pdf)
- Robot Parkour Learning (CoRL 2024) — [Original PDF](https://arxiv.org/pdf/2309.05665.pdf)
- PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots (RAL 2024) — [Original PDF](https://arxiv.org/pdf/2408.13740.pdf)

### Loco-manipulation / Whole-body
- Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion (CoRL 2022) — [Original PDF](https://arxiv.org/pdf/2210.10044.pdf)
- Visual Whole-Body Control for Legged Loco-Manipulation (CoRL 2024) — [Original PDF](https://arxiv.org/pdf/2403.16967.pdf)
- Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks (CoRL 2023) — [Original PDF](https://proceedings.mlr.press/v229/schwarke23a/schwarke23a.pdf) (open access via PMLR)

### Humanoids (Whole-body / Teleop / Getting-up / Generative)
- Expressive Whole-Body Control for Humanoid Robots (RSS 2024) — [Original PDF](https://arxiv.org/pdf/2402.16796.pdf)
- ExBody2: Advanced Expressive Humanoid Whole-Body Control (2024) — [Original PDF](https://arxiv.org/pdf/2412.13196.pdf)
- Open-TeleVision: Teleoperation with Immersive Active Visual Feedback (CoRL 2024) — [Original PDF](https://arxiv.org/pdf/2407.01512.pdf)
- Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control (2024) — [Original PDF](https://arxiv.org/pdf/2412.07773.pdf)
- HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots (ICRA 2025) — [Original PDF](https://arxiv.org/pdf/2410.21229.pdf)
- HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion (2025) — [Original PDF](https://arxiv.org/pdf/2502.03206)
- Learning Humanoid Standing-up Control across Diverse Postures (RSS 2025) — [Original PDF](https://arxiv.org/pdf/2502.08378)
- Learning Getting-Up Policies for Real-World Humanoid Robots (RSS 2025) — [Original PDF](https://arxiv.org/pdf/2502.12152)
- BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (2025) — [Original PDF](https://arxiv.org/pdf/2508.08241)

### Hardware
- A Low Cost Modular Actuator for Dynamic Robots — [Original PDF](https://dspace.mit.edu/handle/1721.1/118671)

### Others

<a id="source-notes" name="source-notes"></a>
## Notes by Lab/Source (Detailed)

<a id="eth-rsl" name="eth-rsl"></a>
### ETH Robotics Systems Lab (RSL)

#### Learning Agile and Dynamic Motor Skills for Legged Robots (Science Robotics 2019)
- Original PDF: https://arxiv.org/pdf/1901.08652.pdf- Notes: A foundational work for RL-based quadruped locomotion. It trains a motor network model from real data and uses it for sim compensation while training the policy with RL + dynamics randomization. The policy was deployed on ANYmal, demonstrating robust locomotion behaviors (speed tracking, recovery after falls, etc.).

#### Learning Quadrupedal Locomotion over Challenging Terrain (Science Robotics 2020)
- Original PDF: https://arxiv.org/pdf/2010.11251.pdf- Notes: Introduces a two-stage teacher–student framework. The teacher learns with privileged (“cheating”) simulator information; the student (deployable with only history of observable signals) is distilled via online imitation learning (DAgger), using an encoder to infer the implicit privileged information. Also proposes terrain curriculum learning for robust traversal of continuous rough terrains. At this time, the overall control stack is still relatively complex: the network assists with foot trajectory generation and still relies on IK to obtain target joints (vs. many later works that directly output target joint commands).

#### Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning (CoRL 2021)
- Original PDF: https://arxiv.org/pdf/2109.11978- Notes: A milestone that accelerated RL-for-robots research. It demonstrates massively parallel training (Isaac Gym) + domain randomization for locomotion, and open-sources the `legged_gym` project.

#### Learning robust perceptive locomotion for quadrupedal robots in the wild (Science Robotics 2022)
- Original PDF: https://arxiv.org/pdf/2201.08117- Notes: Integrates proprioception with exteroceptive vision for robust locomotion, enabling large-scale outdoor walking in challenging conditions (stairs, tunnels, snow, fog, forests, loose rocks, etc.). A good example of learning a locomotion policy that estimates terrain elevation information.

#### Elevation Mapping for Locomotion and Navigation using GPU (IROS 2022)
- Original PDF: https://arxiv.org/pdf/2204.12876- Notes: Proposes an efficient GPU pipeline for building local elevation maps from point clouds and robot pose. In complex environments, odometry drift remains one of the biggest challenges for real-time mapping. Code is open-sourced.

#### Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning (ICRA 2023)
- Original PDF: https://arxiv.org/pdf/2203.14912- Notes: An enhanced AMP setup that supports multiple discrete styles with switching, demonstrated on a wheeled-legged robot (avoidance, walking, and style switching between quadruped and biped/standing modes). The “learn to get down to quadruped from a reverse-standing (biped) sequence” case is particularly interesting.

#### Curiosity-Driven Learning of Joint Locomotion and Manipulation Tasks (CoRL 2023)
- PDF: No open-access PDF was fetched automatically (likely on OpenReview and/or the authors’ website).
- Notes: Key highlight: learns loco-manipulation behaviors on a wheeled-legged robot, using legs as manipulators.

#### Learning Agile Locomotion on Risky Terrains (IROS 2024)
- Original PDF: https://arxiv.org/pdf/2311.10484.pdf- Notes: An interesting RL locomotion work on discrete “risky” terrains (not omnidirectional walking), with strong demos.

#### ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (Science Robotics 2024)
- Original PDF: https://arxiv.org/pdf/2306.14874.pdf- Notes: A hierarchical framework with perception (environment reconstruction), navigation (driving skill selection), and motion modules (parkour primitives). One of the first works demonstrating dynamic quadruped parkour-style navigation.

#### DTC: Deep Tracking Control (Science Robotics 2024)
- Original PDF: https://arxiv.org/pdf/2309.15462.pdf- Notes: Combines model-based and learning-based methods. The upper-level trajectory optimization (TO) layer optimizes body and foot trajectories in real time; a lower-level RL policy tightly tracks those trajectories, enabling precise motion over extreme terrains (stepping stones, trenches, rubble/ruins, etc.). Compared to setups that only do base-velocity tracking, this hierarchical design better leverages legged robots’ ability to choose footholds.

<a id="kaist" name="kaist"></a>
### KAIST (Raibo / Unitree, etc.)

#### Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion (RAL 2022)
- Original PDF: https://arxiv.org/pdf/2202.05481.pdf- Notes: A one-stage asymmetric training setup (not teacher–student). The policy jointly trains a key-state estimator (linear velocity, foot height, contact probability) from history of observable signals, while the critic in simulation uses privileged ground-truth key states. Uses dynamics randomization + PPO and transfers to real robots for robust traversal over continuous rough terrains.

#### DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning (ICRA 2023)
- Original PDF: https://arxiv.org/pdf/2301.10602.pdf- Notes: An asymmetric RL structure where a state estimator infers velocity and implicit terrain latent variables `z` from observable signals (with a VAE-style formulation). Demonstrates robust long-range outdoor locomotion on Unitree A1 and highlights the power of asymmetric actor–critic training in complex environments.

#### Learning Quadrupedal Locomotion on Deformable Terrain (Science Robotics 2023)
- PDF: No open-access PDF was fetched automatically (likely paywalled; try author preprint / arXiv version if available).
- Notes: Modifies RaiSim’s contact dynamics to model granular media / deformable terrain, enabling agile and robust locomotion on soft terrains (e.g., sand, foam pads). Uses an asymmetric training framework, further supporting its effectiveness.

#### A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards (ICRA 2025)
- Original PDF: https://arxiv.org/pdf/2409.15780.pdf- Notes: Introduces relaxed logarithmic barrier functions to design soft-constraint style rewards that guide the robot toward preset motion characteristics (periodicity, joint-range constraints, etc.). Notably, it generates diverse bio-inspired gaits without explicit motion priors; the “human-like walking while standing” and gallop gaits are impressive.

<a id="other-works" name="other-works"></a>
### Other Key Works (Quadrupeds / Bipeds / General)

#### Quadrupeds / Legged Locomotion

##### Sim-to-Real: Learning Agile Locomotion for Quadruped Robots (Minitaur)
- Original PDF: https://arxiv.org/pdf/1804.10332.pdf- Notes: An early sim-to-real quadruped RL work (Ghost Robotics Minitaur). Uses RL + an analytical motor model + dynamics randomization to address the transfer gap, inspiring later ANYmal-style pipelines.

##### Learning Agile Robotic Locomotion Skills by Imitating Animals (RSS 2020)
- Original PDF: https://arxiv.org/pdf/2004.00784.pdf- Notes: Learns natural animal-style locomotion via motion retargeting + DeepMimic-style motion tracking, demonstrated on early Unitree platforms (e.g., Laikago). Code is open-sourced (UCB).

##### RMA: Rapid Motor Adaptation for Legged Robots (RSS 2021)
- Original PDF: https://arxiv.org/pdf/2107.04034.pdf- Notes: Teacher–student with an adaptation module (similar in spirit to ETH’s encoder). Uses random terrain sampling + domain randomization + parallel training in RaiSim, achieving robust continuous-terrain traversal on Unitree A1 without exteroception. Code is open-sourced (CMU).

##### Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (CoRL 2022)
- Original PDF: https://arxiv.org/pdf/2212.03238.pdf- Notes: A highly tunable and robust locomotion policy on Unitree Go1 with fine-grained controllable parameters: speed, gait (pronking/trotting/bounding/pacing/galloping), step frequency, base height, pitch, contact timing, foot clearance, etc. Code is open-sourced (MIT).

##### Rapid Locomotion via Reinforcement Learning (RSS 2022)
- Original PDF: https://arxiv.org/pdf/2205.02824.pdf- Notes: Proposes a self-adaptive speed-grid curriculum that pushes the robot’s speed limits based on learned capability, minimizing hand-tuned curricula and expert intervention. Code is open-sourced (MIT).

##### Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions (ICRA 2022)
- Original PDF: https://arxiv.org/pdf/2203.15103.pdf- Notes: One of the first works applying AMP to quadrupeds: combining task reward with style reward can produce natural-looking behaviors without highly engineered reward terms. Code is open-sourced (UCB).

##### Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion (CoRL 2022)
- Original PDF: https://arxiv.org/pdf/2210.10044.pdf- Notes: Demonstrates arm–leg coordination on Unitree Go1 + a WidowX arm using RL for whole-body loco-manipulation (teleoperation data). Also proposes ROA to estimate environment latent variables online. Built on Isaac Gym + `rsl_rl`, and open-sourced (CMU).

##### Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild (RAL 2023)
- Original PDF: https://arxiv.org/pdf/2304.10888.pdf- Notes: Teacher–student + AMP enables robust continuous-terrain traversal on Unitree Go1 using only proprioception. Natural gait data is generated via trajectory optimization on flat ground. Note: the journal title is “Learning Robust and Agile Legged Locomotion Using Adversarial Motion Priors” (SJTU).

##### Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Generative Pre-trained Models (Nature Machine Intelligence 2023)
- Original PDF: https://arxiv.org/pdf/2308.15143.pdf- Notes: Uses generative models to pretrain on large-scale animal motion data, then reuses those skills during environment-level learning. A representative Robotics X (Tencent) work.

##### Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations
- Original PDF: https://arxiv.org/pdf/2206.11693.pdf- Notes: Learns dynamic skills from rough/incomplete demonstrations collected via manual operation, including backflip-like behaviors on low-cost platforms.

##### Extreme Parkour with Legged Robots (ICRA 2024)
- Original PDF: https://arxiv.org/pdf/2309.14341.pdf- Notes: Pushes Unitree A1’s rough-terrain capabilities with domain randomization + exteroception; demonstrates box jumping, vaulting, squeezing through gaps, etc. (CMU/Stanford+ collaborators).

##### Robot Parkour Learning (CoRL 2024)
- Original PDF: https://arxiv.org/pdf/2309.05665.pdf- Notes: A concurrent line of work with similar goals: parkour-style locomotion with domain randomization + exteroception (CoRL 2024).

##### Visual Whole-Body Control for Legged Loco-Manipulation (CoRL 2024)
- Original PDF: https://arxiv.org/pdf/2403.16967.pdf- Notes: Demonstrates vision-driven hierarchical policies (imitation learning + RL) for mobile manipulation on Unitree B1 + Z1 arm via sim-to-real. Built on Isaac Gym + `rsl_rl`, and open-sourced (UCSD).

##### PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots (RAL 2024)
- Original PDF: https://arxiv.org/pdf/2408.13740.pdf- Notes: A “plus” version that further improves dynamic parkour performance and transfers to outdoor settings (ZJU).

#### Bipeds / General

##### Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (ICRA 2021)
- Original PDF: https://arxiv.org/pdf/2011.01387.pdf- Notes: Defines common gaits (standing, walking, jumping, running, hopping) via probabilistic periodic reward composition and demonstrates on Cassie. Includes both single-gait policies and a gait-switching policy.

##### AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (SIGGRAPH 2021)
- Original PDF: https://arxiv.org/pdf/2104.02180.pdf- Notes: Not a legged-robot paper, but highly transferable: uses a GAN-based implicit metric to provide style rewards for learning control policies (UCB).

<a id="humanoids" name="humanoids"></a>
### Humanoids (Whole-Body Control / Teleop / Getting-Up, etc.)

#### Expressive Whole-Body Control for Humanoid Robots (RSS 2024)
- Original PDF: https://arxiv.org/pdf/2402.16796.pdf- Notes: Learns humanoid motion sequences via motion retargeting (UCSD).

#### ExBody2: Advanced Expressive Humanoid Whole-Body Control (2024)
- Original PDF: https://arxiv.org/pdf/2412.13196.pdf- Notes: A follow-up work to Expressive Whole-Body Control (2024).

#### Open-TeleVision: Teleoperation with Immersive Active Visual Feedback (CoRL 2024)
- Original PDF: https://arxiv.org/pdf/2407.01512.pdf- Notes: An open-source VR teleoperation framework for humanoids (upper body only).

#### Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control (2024)
- Original PDF: https://arxiv.org/pdf/2412.07773.pdf- Notes: Demonstrates a whole-body control approach that extends Open-TeleVision, with a locomotion controller that leverages ideas related to ExBody (2024).

#### HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots (ICRA 2025)
- Original PDF: https://arxiv.org/pdf/2410.21229.pdf- Notes: Unifies several whole-body control target types (root velocity tracking, joint-angle tracking, key-point tracking, etc.) (CMU).

#### HugWBC: A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion (2025)
- Original PDF: https://arxiv.org/pdf/2502.03206- Notes: A “humanoid version” of Walk These Ways: fine-grained gait tuning over continuous terrains (gait type, step frequency, base height, pitch, contact timing, foot clearance, etc.). Notable for natural gaits induced by polynomial foot-trajectory rewards and extensibility via curricula that bring in upper-body freedom (SJTU / Shanghai AI Lab).

#### Learning Humanoid Standing-up Control across Diverse Postures (RSS 2025)
- Original PDF: https://arxiv.org/pdf/2502.08378- Notes: Strong getting-up behaviors across diverse postures (Shanghai AI Lab).

#### Learning Getting-Up Policies for Real-World Humanoid Robots (RSS 2025)
- Original PDF: https://arxiv.org/pdf/2502.12152- Notes: A concurrent getting-up policy work (UIUC).

#### BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (2025)
- Original PDF: https://arxiv.org/pdf/2508.08241- Notes: High-quality motion tracking plus guided diffusion; supports test-time task-specific control using simple cost functions (Berkeley/Stanford).

<a id="surveys" name="surveys"></a>
### Surveys

#### Learning-based legged locomotion: State of the art and future perspectives (IJRR 2025)
- Original PDF: https://arxiv.org/pdf/2406.01152.pdf- Notes: A survey of learning-based legged locomotion control, summarizing recent academic and industrial progress and outlining future directions (Georgia Tech).

<a id="misc" name="misc"></a>
### Misc (no notes yet)
- Robot Dynamics Lecture Notes (2017) — [Original PDF](https://rsl.ethz.ch/education-students/lectures/robotdynamics.html)
- Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control — [Original PDF](https://dspace.mit.edu/handle/1721.1/138000.2)
- A Low Cost Modular Actuator for Dynamic Robots — [Original PDF](https://dspace.mit.edu/handle/1721.1/118671)

Back to overview: [README.en.md](../README.en.md)
