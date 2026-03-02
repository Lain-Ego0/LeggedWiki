# KAIST (Raibo / Unitree, etc.)

[中文（默认）](KAIST.md) | English

## Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion (RAL 2022)
- PDF: [推荐论文/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf](<../推荐论文/KAIST/2022 - Concurrent Training of a Control Policy and a State Estimator for Dynamic and Robust Legged Locomotion.pdf>)
- Notes: A one-stage asymmetric training setup (not teacher–student). The policy jointly trains a key-state estimator (linear velocity, foot height, contact probability) from history of observable signals, while the critic in simulation uses privileged ground-truth key states. Uses dynamics randomization + PPO and transfers to real robots for robust traversal over continuous rough terrains.

## DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning (ICRA 2023)
- PDF: [推荐论文/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf](<../推荐论文/KAIST/2023 - DreamWaQ- Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning.pdf>)
- Notes: An asymmetric RL structure where a state estimator infers velocity and implicit terrain latent variables `z` from observable signals (with a VAE-style formulation). Demonstrates robust long-range outdoor locomotion on Unitree A1 and highlights the power of asymmetric actor–critic training in complex environments.

## Learning quadrupedal locomotion on deformable terrain (Science Robotics 2023)
- PDF: No open-access PDF was fetched automatically (likely paywalled; try author preprint / arXiv version if available).
- Notes: Modifies RaiSim’s contact dynamics to model granular media / deformable terrain, enabling agile and robust locomotion on soft terrains (e.g., sand, foam pads). Uses an asymmetric training framework, further supporting its effectiveness.

## A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards (ICRA 2025)
- PDF: [推荐论文/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf](<../推荐论文/KAIST/2025 - A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards.pdf>)
- Notes: Introduces relaxed logarithmic barrier functions to design soft-constraint style rewards that guide the robot toward preset motion characteristics (periodicity, joint-range constraints, etc.). Notably, it generates diverse bio-inspired gaits without explicit motion priors; the “human-like walking while standing” and gallop gaits are impressive.

