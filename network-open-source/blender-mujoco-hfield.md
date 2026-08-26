# blender-mujoco-terrain：MuJoCo 地形导出插件

> 类型：Blender 插件 / MuJoCo / 地形建模

## 项目简介

由于 GitHub 上缺少相对易用的 MuJoCo 地形导出插件，作者制作了一个 Blender 扩展，并配套整理了地形导出教程，帮助不熟悉地形导出的开发者快速上手。仓库实际项目名称为 `blender-mujoco-terrain`，当前版本为 `0.1.0-alpha`，输出格式仍可能调整。

## 项目入口

- [blender-mujoco-terrain](https://github.com/Eterith/blender-mujoco-hfield/tree/main)

项目由广西大学相关开发者开源，具体使用方式、插件代码和教程请以仓库内容为准。

## 适用场景

该插件适合用于：

- 将 Blender 中制作的地形用于 MuJoCo；
- 学习 MuJoCo height field 地形的导出流程；
- 快速检查地形模型和仿真导入结果。

## 主要功能

- 从当前 Blender 场景导出 MuJoCo heightfield、可视化网格、碰撞网格、纹理、元数据和 MJCF 场景；
- 支持高度场碰撞、额外固定碰撞体和带 `freejoint` 的可移动碰撞体；
- 支持 OBJ、PNG，以及通过 Cube 提取悬空结构；
- 悬空结构可以使用三棱柱碰撞体或 CoACD 进行碰撞近似；
- 普通导出在后台 Blender 进程中执行，减少界面阻塞。

## 安装与使用

建议从 GitHub Release 下载扩展 ZIP，不要直接使用 GitHub 自动生成的 source archive。Blender 中通过 `Edit > Preferences > Extensions > Install from Disk` 安装，然后在 3D Viewport 按 `N` 打开 `MuJoCo 地形` 面板。

基本流程是：切换到 Object Mode，选择网格并加入对应碰撞列表，设置输出目录和 HField 分辨率，点击 `生成 MuJoCo 场景`。生成目录通常包含 `.hfield`、可视化 OBJ、碰撞 OBJ、可选 PNG、`terrain.json` 和 `mjcf/scene_*.xml`。

## 使用注意

Heightfield 会将采样面以下区域视为实体，因此洞穴顶部、桥底和悬空岛屿应放入额外碰撞体。使用 Cube 提取悬空结构会改变源网格拓扑，操作前应保存 `.blend` 文件。该扩展面向 Blender 5.2 及以上版本。
