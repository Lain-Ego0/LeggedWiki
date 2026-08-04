# RC上位机：从入门到入土（初版）

> 原文链接：[RC上位机：从入门到入土](https://lumivers.feishu.cn/wiki/I0S2wsP9DiUsGdkp1kkc9s48ngb)

# 写在前面

你好，我是lumivers，可以叫我lumi。一位软件工程师，主要方向为上位机开发与游戏开发。目前中北大学大三在读。此文章将持续更新，初版已来到57k\+字符。

在RC这个圈子，机械、结构和电控嵌软占了绝大多数，而负责视觉、感知和决策的上位机方向，资料往往非常碎片化。甚至可以说，目前的上位机教程就像嵌软那边n年不更新的Keil一样，这么多年都没个系统、开箱即用的好版本。因此，我打算将上位机开发的大部分核心知识做个系统性的梳理与统一，并保持持续更新，供大家参考和查阅。
文章部分采用ai编写，文笔与语义错误在所难免，也请读者看到之后联系我：QQ：2423109915
本文欢迎各路大佬加入自己认为上位机中必须的内容，希望可以靠大家的力量将此文章做的越来越好。

# 第一章 如何使用git

> 作者在25赛季见到了很多哥们不喜欢，不懂得，不知道使用git，所以第一节我们先写如何使用git
> 
> 

# 为什么第一节是git？

在机械，电控，上位机开发中，git是非常好用的一个工具，不仅是起到一个备份的作用，更是有强大的版本管理功能。

如果你不用git，可能会碰到以下场景：

- 你改好的最新一版代码，队员上来给你用旧版本的覆盖了

- 你想回滚到最后一版稳定的代码，但是你找不到你的压缩包

- 在自己电脑上好好的，为什么去上位机上面就跑不起来

git就是你的后悔药和时光机，可以让你精准的回溯到每一个文件的编写。

## git最常使用的几个指令

git那么多指令记下来显然不现实，最常用的只有这几个：

### 拉取远程仓库

```Bash
git clone <你的仓库地址>
```

### 日常开发使用

1. 查看自己目前改动了哪些文件

```Bash
git status
```

2. 暂存当前更改

```Bash
git add .
```

3. 提交更改，必须附上这次的更改说明，记录下你改了什么。

```Bash
git commit -m "修改内容"
```

4. 把你的代码推送到云端

```Bash
git push
```

不过令人可喜的是，VScode现在的git插件已经全面把这几个指令图形化了。所以现在也用不着再去cli里面敲指令了。

只需要在侧边栏里面找到源代码管理页面，里面有ai生成提交信息，提交，推送等功能，还能显示提交历史。总之非常好用。

> 重点：学会配置\.gitignore
> 
> 

上位机开发过程中会产生许多编译中间产物，这些往往是出来占你仓库内存的。比如数据集，测试集，build文件夹等。这些都不能上传到仓库里面，要不然拉代码会很折磨

> 在项目根目录下创建一个名为\.gitignore的文件，把不需要上传的文件夹或者文件写进去：
> 
> 

```Plain Text
# 忽略 CMake 编译生成的各种中间件
build/
bin/

# 忽略 VS Code 的本地配置
.vscode/

# 忽略日志文件和测试视频
*.log
*.mp4
*.avi
```

## 经典报错

> fatal: No configured push destination\.
> 
> 

git根本不知道你要推送到哪，去你的仓库里面复制一下链接，然后执行：

```Bash
# 告诉本地 Git，远程仓库的代号叫 origin，地址是后面这串
git remote add origin <你的远程仓库开源地址>
```

验证：运行**git remote \-v**，如果能看到两条带origin的玩意，就跑通了

> error: failed to push some refs to \.\.\. 或者提示找不到分支。
> 
> 

历史遗留问题，现在平台的默认主分支为main，旧版本git init出来的分支叫master。名字对不上推不上去。

执行：

```Plain Text
git branch -M main
```

即可。

> fatal: refusing to merge unrelated histories
> 
> 

你在云端建仓库的时候，手痒勾选了“初始化仓库/生成 README\.md / 添加 \.gitignore”。这就导致云端有了一个“初始提交”，而你本地也有自己的代码提交。Git 认为这是两个完全不相干的独立项目，为了安全，拒绝让你推送和合并。

**方案A**：允许无关历史合并，先把云端的东西拉下来再说：

```Plain Text
git pull origin main --allow-unrelated-histories
```

拉下来之后再提交就行，不过可能会让你写merge说明

**方案B**:不管云端有什么，本地优先（前期可用，后期禁止）

```Plain Text
git push -u origin main -f    # -f 代表 force（强制）
```

注意，这个会强制把云端仓库内容覆盖为上传者的当前仓库，但是前期没东西的话可以用。

\>想少遭这种罪的话，最简单的是先在云端创好仓库，然后再**git clone**下来就行

# 第二章 开发环境搭建与工具链配置

> 既然学会了 git，那接下来我们就从耳熟能详的 Windows 转到上位机开发常用的 Ubuntu 吧。本章会把 C\+\+ / CMake / ROS2 / Python 四件套一次性配齐，并用 Docker 把环境锁死，避免"在我电脑上能跑"的悲剧。
> 
> 

# 为什么是 Ubuntu？

在 RC 上位机开发中，Ubuntu 几乎是事实上的标准系统。原因很简单：

- ROS/ROS2 原生支持 Linux，Windows 上跑起来非常折腾

- OpenCV、PCL 等视觉库在 Linux 下编译和性能都更好

- 大部分开源的上位机项目和算法代码都是在 Ubuntu 下写的

- 嵌入式交叉编译工具链对 Linux 支持更友好

> 当然，不是说 Windows 不能写上位机，但你迟早会碰到各种奇怪的环境问题。与其到时候再折腾，不如一开始就用 Ubuntu。
> 
> 

> 虽然但是如果各位用的是 Jetson 的话，那很享福了，刷机和配环境值得我单开一期，碰到的问题包括但不限于：到头来还得自己编，刷机要求主机版本等等。
> 
> 

# 安装 Ubuntu

目前主流有三种方式，各有优劣：

## 方案一：双系统（推荐）

最正经的方案，性能最好，也最接近真实上位机的使用场景。

**优点：** 性能拉满，GPU 直通，最接近真实部署环境

**缺点：** 需要分区，切换系统要重启

步骤：

1. 去 [Ubuntu 官网](https://ubuntu.com/download/desktop) 下载最新的 LTS 版本（推荐 22\.04 或 24\.04）

2. 用 Rufus 或 Ventoy 制作启动 U 盘

3. 重启电脑，进 BIOS 设置 U 盘启动

4. 安装时选择"与 Windows 共存"，分配至少 100G 空间

> 注意：装双系统之前一定要备份数据，分区操作有风险
> 
> 

## 方案二：WSL2

如果你不想折腾分区，WSL2 是个很好的折中方案。

**优点：** 不用重启切换系统，和 Windows 无缝共存

**缺点：** GPU 支持需要额外配置，GUI 应用需要 WSLg

```PowerShell
# 在 PowerShell（管理员）中执行
wsl --install -d Ubuntu-24.04
```

装完之后在开始菜单找到 Ubuntu，打开设置用户名密码就行了。

> WSL2 默认可以访问 Windows 的文件系统，你的代码放在 `/mnt/c/` 下就能在两个系统间共享
> 
> 

## 方案三：虚拟机

VMware 或 VirtualBox 都行。

**优点：** 不影响现有系统，快照功能方便回滚

**缺点：** 性能损耗大，USB 设备（摄像头等）直通麻烦

> 如果你需要接摄像头调参，虚拟机方案会很痛苦。建议用方案一或方案二。
> 
> 

# 装完系统第一件事：换源

Ubuntu 默认的软件源在国外，下载速度感人。第一步就是换成国内镜像。

```Bash
# 备份原始源
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 换成清华源（以 24.04 为例）
sudo sed -i 's|http://archive.ubuntu.com/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ubuntu|g' /etc/apt/sources.list

# 更新
sudo apt update && sudo apt upgrade -y
```

> 如果你用的是 Ubuntu 24\.04，源配置文件可能在 `/etc/apt/sources.list.d/ubuntu.sources`，格式不一样，具体去清华源官网复制对应版本的配置。
> 
> 

# 基本的终端操作

上位机开发基本都在终端里操作，这几个命令必须会：

```Bash
# 切换目录
cd /path/to/directory

# 查看当前目录下的文件
ls -la

# 创建文件夹
mkdir my_project

# 编辑文件（选一个用）
nano my_file.txt    # 简单好上手
vim my_file.txt     # 学习曲线陡但功能强

# 查看文件内容
cat my_file.txt

# 复制、移动、删除
cp src dst
mv src dst
rm -rf directory    # 慎用，删了就没了

# 查看当前路径
pwd
```

> 记住一个原则：在 Linux 下，`rm -rf` 是不可逆的。没有回收站，删了就是删了。用之前多看一眼路径。
> 
> 

# SSH 配置

上位机一般不会接显示器键盘鼠标，都是通过 SSH 远程连接的

## 在上位机上开启 SSH 服务

```Bash
# 安装 openssh-server
sudo apt install openssh-server -y

# 查看 SSH 状态
sudo systemctl status ssh

# 查看上位机的 IP 地址
ip addr show
```

## 从你的电脑连接

```Bash
# 基本格式
ssh username@ip_address

# 例如
ssh robot@192.168.1.100
```

## 配置免密登录（推荐）

每次输密码太烦了，配置一下密钥：

```Bash
# 在你的电脑上生成密钥（一路回车）
ssh-keygen -t ed25519

# 把公钥传到上位机
ssh-copy-id username@ip_address
```

之后再连就不需要密码了。

# 配置 VSCode Remote SSH

命令行写代码终究不方便，VSCode 的 Remote SSH 插件可以让你在本地 VSCode 里编辑远程上位机的代码。

1. 在 VSCode 里安装插件 `Remote - SSH`

2. 按 `Ctrl+Shift+P`，输入 `Remote-SSH: Connect to Host`

3. 输入 `username@ip_address`，回车

4. 连上之后打开上位机的项目文件夹，和本地开发体验一样

> 甚至终端也是远程的，直接在 VSCode 下面的终端里编译运行，非常方便
> 
> 

# CMake：C\+\+ 工程的构建骨架

上位机工程不是一个 `.cpp` 文件搞定的事。多个源文件、第三方库、编译选项——靠手敲 `g++` 迟早崩溃。CMake 是 C\+\+ 世界事实上的构建标准。

## 最小 CMake 项目

```CMake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(rc_upper VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 把 src/ 下所有 .cpp 编译成一个可执行文件
file(GLOB_RECURSE SOURCES "src/*.cpp")
add_executable(rc_upper ${SOURCES})

# 链接 OpenCV
find_package(OpenCV REQUIRED)
target_link_libraries(rc_upper ${OpenCV_LIBS})
```

```Bash
# 标准三连
mkdir build && cd build
cmake ..
make -j$(nproc)
```

## 为什么用 CMake 而不是直接 g\+\+？

|场景|手敲 g\+\+|CMake|
|---|---|---|
|3 个文件|能凑合|都行|
|30 个文件 \+ 多个库|每次编译敲一屏幕|`cmake .. && make`|
|换电脑/换系统|路径全废，重新来过|改一下路径就行|
|和队友协作|"你编译命令是啥？"|共享 CMakeLists\.txt 即可|

> 一个原则：项目超过 3 个源文件，就该上 CMake。
> 
> 

## 常用 CMake 指令速查

```CMake
# 查找并链接第三方库
find_package(Eigen3 REQUIRED)
target_link_libraries(my_app Eigen3::Eigen)

# 添加头文件搜索路径
target_include_libraries(my_app PRIVATE include/)

# 条件编译（比如 debug 模式加 -g）
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(my_app PRIVATE -g -O0)
endif()

# 生成库（把通用代码编译成 .a 或 .so）
add_library(my_utils STATIC src/utils.cpp)
target_link_libraries(rc_upper my_utils)
```

# Python 环境管理

上位机不全是 C\+\+——快速原型、数据处理、训练脚本经常用 Python。关键是**隔离环境**，避免系统 Python 被污染。

## Miniconda（推荐）

```Bash
# 下载安装
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# 创建项目环境
conda create -n rc python=3.11 -y
conda activate rc

# 常用包
pip install numpy opencv-python pyserial pyyaml
```

> **不要用系统自带的 Python 直接装包。** Ubuntu 的 `apt install python3-xxx` 和 `pip install` 混着用迟早出问题。用 conda 或 venv 隔离。
> 
> 

## 项目级隔离（venv）

如果不想装 conda，Python 自带的 venv 也够用：

```Bash
cd your_project
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

> 把 `.venv/` 加到 `.gitignore` 里，不要提交虚拟环境到仓库。
> 
> 

# ROS2 安装与配置

ROS2 是上位机的神经系统——节点间通信、传感器驱动、算法模块化都靠它。

## 安装 ROS2 Humble（推荐）

> 虽然但是我更推荐各位去用鱼香ros的一键安装ros，可以自己下载对应版本：
> 
> 

```Plain Text
wget http://fishros.com/install -O fishros && . fishros
```

> 直接复制过去运行即可。
> 
> 

Ubuntu 22\.04 对应 ROS2 Humble，Ubuntu 24\.04 对应 ROS2 Jazzy。以 Humble 为例：

```Bash
# 设置源
sudo apt install software-properties-common
sudo add-apt-repository universe

# 添加 ROS2 GPG key
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# 添加源（清华镜像）
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# 安装
sudo apt update
sudo apt install ros-humble-desktop -y

# 安装开发工具
sudo apt install ros-humble-ros-base python3-colcon-common-extensions -y
```

## 环境激活

每次打开终端都要 source 一下，嫌麻烦就写进 `.bashrc`：

```Bash
# 写进 bashrc，开终端自动加载
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 验证安装

```Bash
# 终端 1：启动一个 talker
ros2 run demo_nodes_cpp talker

# 终端 2：启动一个 listener
ros2 run demo_nodes_py listener
```

如果 listener 能收到 talker 的消息，ROS2 就装好了。

## 创建 ROS2 工作空间

```Bash
# 创建工作空间
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# 创建一个包
ros2 pkg create --build-type ament_cmake my_robot --dependencies rclcpp std_msgs

# 编译
cd ~/ros2_ws
colcon build --packages-select my_robot

# 加载环境
source install/setup.bash
```

> `colcon build` 是 ROS2 的编译命令，相当于 `cmake + make` 的封装。`--packages-select` 只编译指定包，省时间。
> 
> 

## ROS2 核心概念速览

```Plain Text
┌──────────────┐    Topic: /chassis_status    ┌──────────────┐
│  serial_node │ ──────────────────────────── > │  decision    │
│  (串口驱动)  │                               │  (决策节点)  │
│              │ < ─────────────────────────── │              │
└──────────────┘    Topic: /cmd_vel           └──────────────┘
```

- **Node（节点）**：一个独立的可执行程序，负责一件事（串口通信、决策、控制……）

- **Topic（话题）**：节点间的数据管道，发布/订阅模型，异步通信

- **Service（服务）**：同步的请求/响应模式，适合偶尔调用的操作

- **Parameter（参数）**：运行时可调的配置项，不用重新编译

> RC 上位机典型节点划分：`serial_node`（串口驱动）、`lidar_node`（雷达）、`decision_node`（决策状态机）、`control_node`（运动控制）、`vision_node`（视觉识别）。
> 
> 

# 安装常用依赖

上位机开发需要装的东西大同小异，一并列出来：

## 编译工具链

```Bash
sudo apt install -y build-essential cmake git
```

## OpenCV（从源码编译）

> ROS2 自带的 OpenCV 版本可能偏旧，如果需要特定版本（比如 4\.9），从源码编译更可控。
> 
> 

```Bash
# 安装依赖
sudo apt install -y libgtk-3-dev pkg-config libavcodec-dev libavformat-dev \
    libswscale-dev libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-dev

# 下载源码
cd ~
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 4.9.0    # 选一个稳定版本

# 编译安装
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
make -j$(nproc)
sudo make install
```

> `make -j$(nproc)` 会用满你所有的 CPU 核心来编译，上位机如果是多核的话会快很多。
> 
> 

## 串口通信库

上位机和下位机（电控）通信基本靠串口：

```Bash
sudo apt install -y libserial-dev
# 或者用这个轻量的
git clone https://github.com/wjwwood/serial.git
cd serial && mkdir build && cd build
cmake .. && make -j$(nproc)
sudo make install
```

## 其他常用库

```Bash
# Eigen（矩阵运算）
sudo apt install -y libeigen3-dev

# yaml-cpp（读配置文件）
sudo apt install -y libyaml-cpp-dev

# spdlog（日志库）
sudo apt install -y libspdlog-dev
```

# Docker：把环境锁死

"Docker 有什么用？我直接装不就行了？"

直到比赛前一天，你换了一台电脑，发现 OpenCV 版本不对、ROS2 源挂了、Python 包冲突——这时候你就知道 Docker 有多香了。Docker 的核心价值：**环境可复现、可迁移、可回滚。**

## 安装 Docker

```Bash
# 安装 Docker
curl -fsSL https://get.docker.com | sh

# 让当前用户可以不用 sudo 执行 docker
sudo usermod -aG docker $USER

# 重新登录终端生效，或者临时用 newgrp
newgrp docker

# 验证
docker run hello-world
```

## 编写 Dockerfile

在项目根目录创建 `Dockerfile`：

```Dockerfile
FROM ros:humble-ros-base

# 安装依赖
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    libeigen3-dev \
    libserial-dev \
    libyaml-cpp-dev \
    libspdlog-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Python 依赖
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# 挂载工作空间
WORKDIR /ros2_ws
```

## 一行命令进入开发环境

```Bash
# 构建镜像
docker build -t rc_dev .

# 运行容器，把项目目录挂进去
docker run -it --rm \
    -v $(pwd):/ros2_ws \
    -v /dev:/dev \
    --privileged \
    rc_dev bash
```

> `-v /dev:/dev` 和 `--privileged` 是为了让容器能访问串口设备（`/dev/ttyUSB0`）。如果只是编译和测试算法，可以不加。
> 
> 

## Docker Compose：多服务编排

当你的系统需要同时跑 ROS2 节点、串口服务、Web 调试界面时，用 Docker Compose 统一管理：

```YAML
# docker-compose.yml
version: "3.8"
services:
  ros2:
    build: .
    volumes:
      - .:/ros2_ws
      - /dev:/dev
    privileged: true
    command: ros2 launch my_robot bringup.launch.py
```

```Bash
docker compose up -d    # 后台启动
docker compose logs -f  # 看日志
docker compose down     # 停止
```

# 验证环境

装完之后跑个小程序验证一下 C\+\+ 环境：

```C++
// test_env.cpp
#include <iostream>
#include <opencv2/opencv.hpp>
#include <Eigen/Dense>

int main() {
    // 验证 OpenCV
    std::cout << "OpenCV version: " << CV_VERSION << std::endl;

    // 验证 Eigen
    Eigen::Matrix3d m = Eigen::Matrix3d::Identity();
    std::cout << "Eigen identity matrix:\n" << m << std::endl;

    std::cout << "环境搭建成功！" << std::endl;
    return 0;
}
```

```Bash
# 编译
g++ test_env.cpp -o test_env $(pkg-config --cflags --libs opencv4)

# 运行
./test_env
```

验证 ROS2：

```Bash
ros2 run demo_nodes_cpp talker
```

验证 Docker：

```Bash
docker run --rm hello-world
```

如果都能正常跑，环境就没问题了。

# 快捷编译脚本

每次手动 `mkdir build && cd build && cmake .. && make` 太烦了。写个脚本一键搞定：

```Bash
#!/bin/bash
# build.sh - 放在项目根目录

set -e  # 出错即停

BUILD_DIR="build"
BUILD_TYPE="${1:-Release}"  # 默认 Release，传 Debug 切 Debug 模式

# 如果 build 目录不存在就创建
if [ ! -d "$BUILD_DIR" ]; then
    mkdir "$BUILD_DIR"
fi

cd "$BUILD_DIR"
cmake -DCMAKE_BUILD_TYPE=$BUILD_TYPE ..
make -j$(nproc)

echo "✅ 编译完成"
```

```Bash
chmod +x build.sh

# Release 模式
./build.sh

# Debug 模式
./build.sh Debug
```

> 更进一步，可以配合 VSCode 的 `tasks.json`，按 `Ctrl+Shift+B` 直接触发编译，连脚本都不用跑。
> 
> 

# 常见问题

> SSH 连不上？
> 
> 

检查几个东西：

- 上位机和你的电脑在不在同一个局域网（ping 一下试试）

- 防火墙有没有放行 22 端口

- openssh\-server 有没有装好（`sudo systemctl status ssh`）

> OpenCV 编译报错？
> 
> 

大概率是依赖没装全，回去把那堆 `libxxx-dev` 都装上。如果报 `libgtk` 相关错误，确认装了 `libgtk-3-dev`。

> 编译找不到库？
> 
> 

确认 `pkg-config` 能找到：

```Bash
pkg-config --modversion opencv4
```

如果找不到，可能需要把 `/usr/local/lib/pkgconfig` 加到 `PKG_CONFIG_PATH` 里：

```Bash
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
```

> ROS2 命令找不到？
> 
> 

检查有没有 source 环境：

```Bash
source /opt/ros/humble/setup.bash
```

如果每次开终端都要手动 source，把它写进 `~/.bashrc`。

> Docker 权限不足？
> 
> 

```Bash
sudo usermod -aG docker $USER
# 重新登录终端
```

# 第三章 串口协议与硬件接口抽象

> 从这一章开始，我们正式进入上位机的核心架构。第一个要解决的问题是：上位机（大脑）和下位机/电控（身体）之间怎么说话。这一章学完，你将得到一个干净的硬件接口层——上层代码永远不需要知道串口是什么。
> 
> 

# 为什么先讲串口？

RC 赛车的上位机不是孤立运行的。它需要告诉底盘"往前走、左转、停"，也需要从电控那里拿到轮速、气压、机械臂状态等反馈。而这些信息的载体，在 RC 赛场上基本就是**串口（UART）**。

为什么是串口而不是 USB、网口、CAN？

- 电控那边的单片机（STM32 之类的）天生就带 UART 外设，接线简单

- RS485/TTL 电平转换便宜可靠，几毛钱一个模块

- 赛场环境简单，不需要网络协议栈那么复杂的东西

但串口有一个本质问题：**它只是一根电线，传的是裸字节流，没有消息边界、没有校验、没有语义。** 你发 `0x01 0x02`，对方收到的可能是 `0x01` 然后隔了 50ms 才收到 `0x02`——字节流就是这样，随时可能被拆开或粘连。

所以这一章的核心任务是：**在裸字节流之上，设计一套可靠的消息协议。**

# 串口通信的物理本质

## 字节流，不是消息包

很多人刚接触串口时会有一个误解：以为发一个"包"对方就收到一个"包"。实际上串口只保证**字节顺序**，不保证**消息边界**。

```Plain Text
你发的：  [0xAA] [0x01] [0x02] [0x55]    ← 一帧
对方可能收到：
  第1次读：[0xAA] [0x01]               ← 只读到一半
  第2次读：[0x02] [0x55]               ← 后一半才到
```

也可能：

```Plain Text
你发两帧：  [帧1] [帧2]
对方一次读到：[帧1 的尾巴] [帧2 的开头]  ← 粘包
```

**这是串口编程的第一课：永远不要假设一次 read 就是一条完整消息。** 你必须自己从字节流里切分出消息帧。

## 波特率与常见配置

RC 赛场上串口配置基本是固定的：

```Bash
波特率：115200（主流，够快够稳）
数据位：8
停止位：1
校验位：无
流控：无
```

> 波特率不是越高越好。115200 在几米线长内足够可靠。到了 921600 或更高，线材质量、电磁干扰都可能导致误码。赛场环境电磁环境复杂，别贪快。
> 
> 

# 协议约定：先对表，再写码

**这是整个章节最重要的一节。** 协议不是上位机自己定的——它是上位机和电控之间的契约。你在电脑上写得再漂亮，电控那边不认、不解析、字段对不上，全是瞎jb写。

## 必须提前约定的清单

在开始写代码之前，拉着电控的人坐下来，把这些东西约定好写死在文档里：

|约定项|举例|不约定会怎样|
|---|---|---|
|**波特率**|115200|两边速度不一致，收全是乱码|
|**字节序**|小端序（Little\-Endian）|你发 `0x0001`，对方收到 `0x0100`|
|**帧头/帧尾**|`0xAA 0x55` / `0x55`|电控按 `0xFF` 解析，你发 `0xAA`，帧永远收不到|
|**CRC 多项式**|Modbus CRC\-16 \(0xA001\)|你算的校验和和对方对不上，全帧丢弃|
|**命令字定义**|`0x01` = 速度指令，`0x02` = 急停|你发 `0x01` 是速度，电控以为是急停|
|**数据字段顺序和类型**|先 linear\(float\) 再 angular\(float\)|你发 float 4 字节，电控按 int 解析|
|**数值范围和单位**|linear ∈ \[\-3\.0, 3\.0\] m/s|你发 5\.0，电控截断成 255，车疯了|
|**通信方向**|上位机→电控：速度指令；电控→上位机：轮速反馈|双方都在发，谁也不收|
|**发送频率**|50Hz（每 20ms 一帧）|你发 100Hz，电控处理不过来，队列溢出|

## 怎么落地：写一份协议文档

不要用口头约定，不要用微信聊天记录。在项目仓库里建一个 `docs/protocol.md`，长这样：

```Markdown
# R2 串口通信协议v1.2（下一届的好像叫BR？反正都是全自动）

## 物理层
- 接口：UART TTL 3.3V
- 波特率：115200
- 数据格式：8N1（8数据位，无校验，1停止位）

## 帧格式
| 字段   | 长度   | 说明          |
| ------ | ------ | ------------- |
| 帧头   | 2 byte | 0xAA 0x55     |
| 命令字 | 1 byte | 见命令表      |
| 长度   | 1 byte | 数据区字节数  |
| 数据   | N byte | 见各命令定义  |
| CRC    | 2 byte | CRC-16/Modbus |

## 字节序
所有多字节字段均为小端序（Little-Endian）

## 命令表
| 命令字 | 方向        | 含义     | 数据区                   |
| ------ | ----------- | -------- | ------------------------ |
| 0x01   | 上位机→电控 | 速度指令 | linear(4B) + angular(4B) |
| 0x02   | 上位机→电控 | 急停     | 无                       |
| 0x10   | 电控→上位机 | 轮速反馈 | left(4B) + right(4B)     |
| 0x11   | 电控→上位机 | 气压状态 | pressure(4B)             |

## 速度指令 (0x01) 数据区
| 偏移 | 长度 | 类型  | 字段    | 范围              |
| ---- | ---- | ----- | ------- | ----------------- |
| 0    | 4    | float | linear  | [-3.0, 3.0] m/s   |
| 4    | 4    | float | angular | [-5.0, 5.0] rad/s |

## 更新记录
- v1.2 (2026-07-26): 增加气压状态反馈
- v1.1 (2026-07-20): 修正 angular 范围为 [-5.0, 5.0]
- v1.0 (2026-07-15): 初始版本
```

> **这份文档就是你们团队的命根子。** 上位机和电控各自照着实现，出了问题对着文档查，而不是互相甩锅。
> 
> 

## 常见的"约定事故"

> 电控说"我发的 float 是 4 字节"，实际用的是 double（8 字节）
> 
> 

上位机按 4 字节读，后面 4 字节全错位，CRC 永远对不上。**约定时必须写死类型和字节数，不要说"float"，要说"IEEE 754 单精度浮点，4 字节，小端序"。**

> 上位机改了协议没通知电控
> 
> 

你加了一个新命令字 `0x03`，但电控那边的解析代码没更新。电控收到 `0x03` 直接丢弃，你以为指令发出去了。**协议变更必须同步两端，文档版本号递增。**

> 赛场上发现协议有问题，现场改
> 
> 

比赛前一天发现某个字段范围不够，现场改协议——这是灾难的开始。**协议在第一次联调时就应该定稿，之后只增不改（新增命令字可以，改已有字段不行）。**

## 联调验证：先发已知数据对答案

两边代码都写好后，不要直接上控制逻辑。先做一个最简单的验证：

```Plain Text
上位机发一帧固定数据 → 电控收到后原样返回 → 上位机比对
```

```C++
// 联调验证：发一个已知的测试帧，看对方能不能原样回传
void protocol_verify(SerialPort& serial) {
    // 构造测试帧
    uint8_t test_frame[] = {0xAA, 0x55, 0xFE, 0x04,
                            0x01, 0x02, 0x03, 0x04,  // 固定数据
                            0x00, 0x00};  // CRC 占位
    uint16_t crc = crc16(test_frame + 2, 6);  // 对命令+长度+数据算 CRC
    test_frame[8] = crc & 0xFF;
    test_frame[9] = (crc >> 8) & 0xFF;

    serial.write(test_frame, sizeof(test_frame));

    // 读回传
    uint8_t reply[64];
    int n = serial.read(reply, sizeof(reply), 1000);  // 超时 1 秒

    if (n == sizeof(test_frame) && memcmp(reply, test_frame, n) == 0) {
        std::cout << "✅ 协议验证通过，通信链路正常" << std::endl;
    } else {
        std::cout << "❌ 协议验证失败，检查帧格式和字节序" << std::endl;
        hex_dump(reply, n);
    }
}
```

> 这步通过了，才说明"两边说的是同一种语言"。之后再往上叠逻辑才有意义。
> 
> 

# 帧协议设计

## 为什么需要帧头和帧尾？

既然串口是无边界的字节流，那我们就要自己划边界。最经典的做法：**帧头 \+ 数据 \+ 帧尾**。

```Plain Text
┌────────┬────────┬────────┬──────────┬──────────┐
│ 帧头   │ 命令字 │ 长度   │ 数据     │ CRC 校验 │
│ 0xAA   │ 1 byte │ 1 byte │ N bytes  │ 2 bytes  │
└────────┴────────┴────────┴──────────┴──────────┘
```

- **帧头（0xAA）**：标记一条消息的开始。接收方逐字节扫描，看到 0xAA 就知道"一帧来了"

- **命令字**：区分不同类型的消息（速度指令、状态查询、急停……）

- **长度**：数据区有多少字节，接收方知道该读多少

- **数据**：实际内容，比如底盘速度、轮速反馈

- **CRC 校验**：数据在传输过程中有没有出错

## 帧头怎么选？

帧头不能太简单，否则数据区里碰巧出现同样的字节就会误判。

```C++
// 帧头设计原则：选一个数据区里不太可能出现的值
constexpr uint8_t FRAME_HEADER = 0xAA;
constexpr uint8_t FRAME_TAIL   = 0x55;

// 更稳妥的做法：用两个字节做帧头，误判概率降到 1/65536
constexpr uint8_t HEADER[] = {0xAA, 0x55};
```

> 如果你的数据区会传任意二进制数据（比如摄像头图像），帧头误判概率会升高。这时候就要靠**转义机制**或**长度字段**来兜底——读完长度字段指定的字节数后，紧接着的两个字节必须是 CRC，对不上就丢弃这帧。
> 
> 

# CRC 校验：数据有没有出错

## 什么是 CRC？

CRC（Cyclic Redundancy Check，循环冗余校验）就是对一帧数据算一个"指纹"。发送方算好附在帧尾，接收方收到后重新算一遍，对得上说明数据没坏，对不上就丢弃。

```Plain Text
发送方：数据 → CRC 计算 → 附在帧尾 → 发出去
接收方：收到数据 → 重新算 CRC → 和帧尾的 CRC 对比
  匹配 → 数据有效
  不匹配 → 丢弃，等下一帧
```

## CRC\-16 实现

RC 赛场上 CRC\-16 够用了。这里给一个可以直接抄的实现：

```C++
#include <cstdint>
#include <cstddef>

uint16_t crc16(const uint8_t* data, size_t length) {
    uint16_t crc = 0xFFFF;  // 初始值
    for (size_t i = 0; i < length; i++) {
        crc ^= data[i];
        for (int j = 0; j < 8; j++) {
            if (crc & 0x0001)
                crc = (crc >> 1) ^ 0xA001;  // 多项式
            else
                crc >>= 1;
        }
    }
    return crc;
}
```

用法：

```C++
// 假设要发送的数据是 {0x01, 0x02, 0x03}
uint8_t payload[] = {0x01, 0x02, 0x03};
uint16_t checksum = crc16(payload, sizeof(payload));

// checksum 的低字节和高字节分别附在帧尾
uint8_t crc_lo = checksum & 0xFF;
uint8_t crc_hi = (checksum >> 8) & 0xFF;
```

> CRC 的多项式有很多种，RC 赛场上用 Modbus 那个（0xA001）就行，上位机和电控约定好同一个即可。
> 
> 

# 内存对齐与高效编解码

## 为什么不能直接把结构体发出去？

很多人会想：既然上位机和下位机都是 C/C\+\+，直接把结构体通过串口发不就行了？

```C++
// ❌ 千万别这么干
struct SpeedCmd {
    float linear;   // 4 bytes
    float angular;  // 4 bytes
};

SpeedCmd cmd{1.0, 0.5};
serial.write((uint8_t*)&cmd, sizeof(cmd));  // 危险！
```

问题在于**内存对齐**。编译器为了访问效率，会在结构体成员之间插入填充字节：

```Plain Text
// 不加控制，编译器可能这样排列：
struct SpeedCmd {
    float linear;   // 4 bytes
    // ← 编译器插入 4 bytes 填充（取决于平台）
    float angular;  // 4 bytes
};
// sizeof = 12，而不是 8
```

而且不同平台（x86 vs ARM）、不同编译器（GCC vs MSVC）的对齐策略可能不一样。你电脑上 sizeof 是 8，Jetson 上可能就是 12，数据直接乱套。

## \#pragma pack\(1\)：禁用对齐填充

```C++
#pragma pack(push, 1)  // 告诉编译器：按 1 字节对齐，不要插填充
struct SpeedCmd {
    uint8_t header;    // 1 byte
    float   linear;    // 4 bytes
    float   angular;   // 4 bytes
    uint16_t crc;      // 2 bytes
};
#pragma pack(pop)      // 恢复默认对齐

static_assert(sizeof(SpeedCmd) == 11, "结构体大小必须是 11 字节");
```

> `static_assert` 是断言，如果编译器偷偷塞了填充字节，编译阶段就会报错，而不是到赛场上才发现数据对不上。
> 
> 

## 打包与解包

有了 pack 结构体，收发就很直接：

```C++
// 打包：结构体 → 字节数组 → 发送
SpeedCmd cmd;
cmd.header = 0xAA;
cmd.linear = 1.0f;
cmd.angular = 0.5f;
cmd.crc = crc16((uint8_t*)&cmd, sizeof(cmd) - 2);  // CRC 不包含自身

serial.write((uint8_t*)&cmd, sizeof(cmd));

// 解包：收到字节流 → 找到帧头 → 拷贝到结构体 → 校验 CRC
SpeedCmd received;
memcpy(&received, buffer + frame_start, sizeof(SpeedCmd));

if (received.crc != crc16((uint8_t*)&received, sizeof(SpeedCmd) - 2)) {
    // CRC 校验失败，丢弃
    return;
}
// CRC 通过，可以安全使用 received.linear 和 received.angular
```

## Python 端的打包

如果你需要用 Python 写测试脚本或快速验证协议，用 `struct` 模块：

```Python
import struct

# 打包：'<BffH' 表示小端序，1个uint8 + 2个float + 1个uint16
header = 0xAA
linear = 1.0
angular = 0.5
crc = 0x1234  # 实际要算

data = struct.pack('<BffH', header, linear, angular, crc)
ser.write(data)

# 解包
received = struct.unpack('<BffH', ser.read(11))
_, linear, angular, crc = received
```

> `<` 表示小端序（Little\-Endian），上位机和电控必须约定好字节序。RC 赛场上基本都是小端序（STM32 和 x86 都是），但约定就是约定，写死在文档里。
> 
> 

# 纯虚接口隔离：设计红线

## 为什么上层不能直接碰串口？

假设你写了一个决策状态机，里面直接调串口发指令：

```C++
// ❌ 决策代码直接依赖串口
class DecisionFSM {
    SerialPort serial_;  // 直接持有串口对象

    void grab_block() {
        serial_.write(grab_cmd, sizeof(grab_cmd));  // 决策层知道串口细节
    }
};
```

这有什么问题？

1. **没法单测**——没有真实硬件就跑不了

2. **换硬件就炸**——换了一种通信方式（比如 CAN 总线），决策代码全部要改

3. **职责混乱**——决策层在操心"怎么发字节"，而不是"该不该抓"

## 正确做法：定义纯虚接口

```C++
// 底盘接口：上层只需要知道"底盘能做什么"
class IChassis {
public:
    virtual ~IChassis() = default;

    // 设置速度（线速度 m/s, 角速度 rad/s）
    virtual void set_velocity(float linear, float angular) = 0;

    // 急停
    virtual void emergency_stop() = 0;

    // 获取当前轮速
    virtual WheelSpeed get_wheel_speed() = 0;
};

// 机械臂接口
class IArm {
public:
    virtual ~IArm() = default;

    // 抓取
    virtual void grab(int block_id) = 0;

    // 释放
    virtual void release() = 0;

    // 查询是否到位
    virtual bool is_ready() = 0;
};
```

上层代码只依赖接口，不依赖实现：

```C++
// ✅ 决策层只依赖接口
class DecisionFSM {
    IChassis& chassis_;  // 引用接口，不知道底层是什么
    IArm& arm_;

public:
    DecisionFSM(IChassis& chassis, IArm& arm)
        : chassis_(chassis), arm_(arm) {}

    void grab_block() {
        chassis_.set_velocity(0, 0);     // 停车
        arm_.grab(1);                     // 抓 1 号块
        // 不需要知道这些指令怎么变成字节发出去的
    }
};
```

## 串口实现：藏在接口后面

```C++
// 真实硬件实现：通过串口和电控通信
class SerialChassis : public IChassis {
    SerialPort serial_;

public:
    SerialChassis(const std::string& port, int baudrate)
        : serial_(port, baudrate) {}

    void set_velocity(float linear, float angular) override {
        SpeedCmd cmd;
        cmd.header = 0xAA;
        cmd.linear = linear;
        cmd.angular = angular;
        cmd.crc = crc16((uint8_t*)&cmd, sizeof(cmd) - 2);
        serial_.write((uint8_t*)&cmd, sizeof(cmd));
    }

    void emergency_stop() override {
        uint8_t stop_cmd[] = {0xAA, 0xFF, 0x00, 0x00};
        // ... 发送急停帧
    }

    WheelSpeed get_wheel_speed() override {
        // 从串口读取轮速反馈帧，解包返回
        // ...
    }
};
```

> **设计红线：上层（决策、控制）永远不知道串口的存在。** 它只知道"我有一个底盘，能设速度、能急停、能读轮速"。至于这个底盘是串口控制的、CAN 控制的、还是仿真的？上层不关心也不需要关心。
> 
> 

# Mock 假硬件：脱离实车做单测

接口隔离最大的好处之一：你可以用几行代码造一个"假底盘"。

```C++
// 假硬件实现：不接串口，纯内存操作
class MockChassis : public IChassis {
public:
    float linear_ = 0, angular_ = 0;
    bool stopped_ = false;
    WheelSpeed wheel_speed_{0, 0};

    void set_velocity(float linear, float angular) override {
        linear_ = linear;
        angular_ = angular;
    }

    void emergency_stop() override {
        linear_ = 0;
        angular_ = 0;
        stopped_ = true;
    }

    WheelSpeed get_wheel_speed() override {
        return wheel_speed_;
    }

    // 测试辅助：手动设置轮速反馈
    void mock_set_wheel_speed(float left, float right) {
        wheel_speed_ = {left, right};
    }
};

class MockArm : public IArm {
public:
    bool grabbed_ = false;
    bool ready_ = true;

    void grab(int block_id) override {
        grabbed_ = true;
        ready_ = false;
    }

    void release() override {
        grabbed_ = false;
        ready_ = true;
    }

    bool is_ready() override {
        return ready_;
    }
};
```

有了 Mock，不用连任何硬件就能测决策逻辑：

```C++
#include <cassert>

void test_grab_sequence() {
    MockChassis chassis;
    MockArm arm;
    DecisionFSM fsm(chassis, arm);

    // 模拟抓取流程
    fsm.grab_block();

    // 验证：决策层应该先停车再抓
    assert(chassis.linear_ == 0);
    assert(chassis.angular_ == 0);
    assert(arm.grabbed_ == true);

    std::cout << "✅ 抓取流程测试通过" << std::endl;
}

int main() {
    test_grab_sequence();
    return 0;
}
```

```Bash
g++ -std=c++20 test_decision.cpp -o test_decision
./test_decision
# 输出：✅ 抓取流程测试通过
```

> **这就是 Mock 的价值：你在笔记本电脑上就能验证决策逻辑对不对，不用等车造好、不用接线、不用怕撞墙。** 赛前改方案时，先在 Mock 上跑通，再上实车。
> 
> 

# 完整的收发流程

把前面的知识串起来，一个完整的"上位机发速度指令 → 收轮速反馈"流程：

```C++
// main.cpp
#include <iostream>
#include <thread>
#include <chrono>

int main() {
    // 1. 创建串口底盘（真实硬件）
    SerialChassis chassis("/dev/ttyUSB0", 115200);

    // 2. 或者创建假底盘（开发调试用）
    // MockChassis chassis;

    // 3. 发速度指令
    chassis.set_velocity(1.0, 0.3);  // 前进 1m/s，右转 0.3rad/s

    // 4. 读轮速反馈
    auto speed = chassis.get_wheel_speed();
    std::cout << "左轮: " << speed.left << " m/s" << std::endl;
    std::cout << "右轮: " << speed.right << " m/s" << std::endl;

    // 5. 急停
    chassis.emergency_stop();

    return 0;
}
```

# 常见坑

> 发出去的数据电控收不到？
> 
> 

检查顺序：

1. 串口有没有开对（`ls /dev/ttyUSB*` 看看设备在不在）

2. 波特率对不对（上位机和电控必须一样）

3. TX/RX 有没有接反（A 的 TX 要接 B 的 RX）

4. 电平对不对（TTL 3\.3V 和 RS485 不能直连，需要转换模块）

> 数据偶尔对不上，CRC 经常校验失败？
> 
> 

大概率是**字节序**或**结构体对齐**问题。用 `#pragma pack(1)` 强制对齐，并在两端打印原始字节比对：

```C++
// 调试用：打印原始字节
void hex_dump(const uint8_t* data, size_t len) {
    for (size_t i = 0; i < len; i++) {
        printf("%02X ", data[i]);
    }
    printf("\n");
}
```

> 串口读到的数据是乱码？
> 
> 

检查：是不是读到了上一帧的残留数据。每次打开串口后先清空缓冲区：

```C++
serial.flush();  // 清空收发缓冲区
```

# 小结

```Plain Text
字节流（串口原始数据）
    ↓ 帧头/帧尾切分
帧协议（结构化消息）
    ↓ CRC 校验
可靠数据（确认没出错）
    ↓ 纯虚接口隔离
干净的 API（IChassis / IArm）
    ↓ Mock 实现
脱离硬件的单测能力
```

这一章建立了上位机和硬件之间的"契约"。从下一章开始，我们在这个契约之上搭建消息总线和三层架构——上层代码将彻底和硬件解耦。

# 第四章 轻量消息总线与三层架构

> 串口协议搞定了，硬件接口也隔离好了，但上位机内部各个模块之间怎么传数据？这一章聊聊消息总线。
> 
> 

# 模块之间为什么要通信？

上位机不是一个 main 搞定所有事。串口驱动要收发硬件数据，决策状态机要发指令等反馈，传感器处理要跑雷达和视觉——这些东西同时在跑，还得互相传数据。串口驱动收到轮速得给决策用，决策发出速度指令得给串口驱动发出去。

最粗暴的做法是直接函数调用，但模块跑在不同线程甚至不同进程里，直接调不是锁死就是压根调不到。所以得有个中间人帮忙转发，这东西就叫消息总线。

# ROS2 Pub/Sub

2026 年做 RC 上位机的人大概率绕不开 ROS2。它继承了 ROS 1 十几年的生态，DDS 通信、节点管理、参数系统一应俱全，行业里的 SLAM、导航、视觉方案几乎都挂在上面。可以说 ROS2 就是机器人软件的事实标准。

但 RC 赛场不是工厂车间。一辆竞速赛车的上位机可能只需要串口驱动、一个决策状态机、一套 Pure Pursuit——总共三四个节点，跑在一台 Jetson 上，通信频率不过 50Hz。为这几个节点装一整套 ROS2 \+ DDS，就像为了喝杯水去建自来水厂。能喝到水吗？能。值不值是另一回事。

先不管值不值，ROS2 的 pub/sub 得会用，因为很多现成的东西（串口驱动、雷达驱动、定位算法）都挂在 ROS2 上。

## 跑通一个最小示例

ROS2 的核心模型就一句话：发布者往 Topic 扔消息，订阅者从 Topic 捡消息，两边互不认识。

**发布者：**

```Python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, '/chatter', 10)
        self.timer = self.create_timer(1.0, self.tick)

    def tick(self):
        msg = String()
        msg.data = 'hello'
        self.pub.publish(msg)

rclpy.init()
rclpy.spin(Talker())
```

**订阅者：**

```Python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(String, '/chatter', self.on_msg, 10)

    def on_msg(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

rclpy.init()
rclpy.spin(Listener())
```

两个终端各跑一个，能看到消息收发就说明跑通了。

## 自定义消息

`String`、`Twist` 这些标准消息不够用的时候要自定义。在 ROS2 包里建一个 `msg/Command.msg`：

```Plain Text
float32 x
float32 y
float32 yaw
int32 stair
int32 block
int32 spearhead
int32 area
```

CMakeLists\.txt 加上消息生成的配置，编译一下就能用了。具体怎么配网上到处都是，不展开了。

## QoS：传感器和指令不能一视同仁

ROS2 的 Topic 有 QoS 策略，控制消息的可靠性。传感器数据用 `BEST_EFFORT`——丢了下一帧还有，要的是快；控制指令用 `RELIABLE`——丢了车就飞，要的是稳。

> 26赛季的分法：轮速、雷达、里程计全 BEST\_EFFORT，/command 和 /decision 用 RELIABLE。传感器丢一帧还行，指令丢了车动都不动。
> 
> 

## 我项目里的实际架构

我的系统是 C\+\+ 串口驱动 \+ Python 决策，两个独立进程，靠 ROS2 topic 通信：

```Plain Text
┌─────────────────┐     /command      ┌──────────────────┐
│  C++ 串口驱动    │ ←───────────────  │  Python 决策节点   │
│                 │  /decision       │  async/await 决策 │
│                 │ ─────────────→    │                  │
└─────────────────┘                   └──────────────────┘
```

C\+\+ 端串口收到下位机的反馈帧，解析完发到 `/decision`；Python 端订阅，收到后唤醒对应的协程。反过来 Python 决策发出的速度指令发到 `/command`，C\+\+ 端订阅后通过串口发给电控。

```Python
# 订阅 /decision，收到后触发事件唤醒协程
self.create_subscription(Ack, '/decision', self.act.on_upper_ack, qos)

def on_upper_ack(self, msg):
    if msg.up_free == 2:
        self.post_event(Event("ARM_DONE", success=True))
```

ROS2 本身其实就是个传话的不是吗？

# ROS2 在 RC 赛场上的问题

用归用，不满意的地方也得说。

**启动慢。** ROS2 底层是 DDS，启动时要节点发现、Topic 匹配、QoS 协商。光 `rclpy.init()` 这一行就要几百毫秒到几秒。赛场上按完启动按钮车 2 秒后才动，这 2 秒可能就是 DDS 在握手。

**进程内通信也要序列化。** 不管发布者和订阅者是不是在同一个进程里，消息都要走一遍序列化 → 传输 → 反序列化。一个 `{x: 1.0, y: 2.0}` 变成字节再变回来，在 50Hz 控制频率下这个开销不是理论上的，是能感知到的。

**spin\(\) 单线程，回调互相卡。** `rclpy.spin()` 默认单线程跑所有回调。视觉处理耗时 200ms 的话，这 200ms 内急停回调也收不到。我后来把决策逻辑放到单独的 asyncio 线程里才解决，但这本身就说明 ROS2 默认模型不适合实时决策——你得绕过它的限制才能用好。

**装起来重。** 好几个 G，编译自定义消息要配 CMakeLists\.txt、package\.xml、setup\.py。RC 赛车就那么几个 Topic，杀鸡用牛刀。

## 什么时候还是得用 ROS2？

双进程架构（C\+\+ 驱动 \+ Python 决策）或者多机器架构（雷达在 Jetson，决策在 x86），ROS2 做桥接是目前最省事的。进程间通信确实需要一个管道，ROS2 帮你把序列化、断线重连、跨机器这些都封装好了，自己搞 socket 通信等于重新发明轮子。

全 Python 单进程的话就完全没必要用 ROS2 了，下面讲的 EventBus 够用。

# 自研 EventBus

很多人（包括我之前）都想：ROS2 太重了，我自己写个 pub/sub 不就行了？

核心逻辑确实不复杂。C\+\+ 版用模板和 `std::any` 实现类型擦除，让一个 EventBus 能传任意类型的数据，不用像 ROS2 那样提前定义 \.msg 文件：

```C++
class EventBus {
    // type_index → [回调列表]，用类型索引区分不同消息
    std::unordered_map<std::type_index,
        std::vector<std::function<void(const std::any&)>>> subs_;
    std::mutex mtx_;

public:
    template<typename T>
    void subscribe(const std::string& topic, std::function<void(const T&)> cb) {
        std::lock_guard<std::mutex> lock(mtx_);
        subs_[std::type_index(typeid(T))].push_back(
            [cb](const std::any& data) { cb(std::any_cast<T>(data)); });
    }

    template<typename T>
    void publish(const std::string& topic, const T& data) {
        std::lock_guard<std::mutex> lock(mtx_);
        for (auto& cb : subs_[std::type_index(typeid(T))])
            cb(data);
    }
};
```

`std::any` 能装任意类型的值，`std::type_index` 给每个类型一个唯一的 key，这样同一个 EventBus 实例既能传 `WheelSpeed` 又能传 `Command`，编译期就做类型检查，传错类型直接抛异常。

用起来就两行：

```C++
EventBus bus;
bus.subscribe<WheelSpeed>("/wheel_speed", [](const auto& msg) {
    std::cout << msg.left << ", " << msg.right << std::endl;
});
bus.publish("/wheel_speed", WheelSpeed{1.0, 1.2});
```

Python 版更简单，一个字典加一个回调列表：

```Python
class EventBus:
    def __init__(self):
        self._subs = {}

    def subscribe(self, topic, callback):
        self._subs.setdefault(topic, []).append(callback)

    def publish(self, topic, data=None):
        for cb in self._subs.get(topic, []):
            cb(data)
```

但实际用起来有几个坑：

**C\+\+ 和 Python 不共享内存。** 我的系统是两个进程，EventBus 在一个进程里创建，另一个进程根本访问不到。进程间通信还是得靠 ROS2、ZeroMQ 或者自己写 socket。ROS2 虽然重，但它帮你把这些都封装好了。

**多线程要加锁。** 串口驱动在自己的线程里 publish，决策在 asyncio 线程里 subscribe，不加锁的话回调列表会被踩坏。上面 C\+\+ 版用了 `std::mutex`，但锁的粒度要控制好——锁太大了 publish 和 subscribe 互相等，锁太小了保护不住。

**背压策略要自己想。** 发布者 100Hz 往 Topic 扔数据，订阅者处理一帧要 30ms，队列满了怎么办？ROS2 的 QoS 帮你处理了这些，自己写的话每种策略都要自己实现。

# 三层架构

不管用什么通信方式，上位机的分层是一样的。26 赛季踩了不少坑才搞清楚这件事。

```Plain Text
决策调度层    状态机 / 任务规划 / 路线选择
  ↑ 只管"做什么"
控制跟踪层    Pure Pursuit / 运动学解算 / PID
  ↑ 只管"怎么走"
感知驱动层    串口驱动 / 雷达 / 视觉 / DT35
  只管"提供干净数据"
```

就和我们常说的“高内聚，低耦合”一样，各层之间通过消息总线传数据，不直接调用。感知层不知道决策层在干什么，决策层不知道串口协议长什么样。

为什么要分这么清楚？因为**需求变的频率不一样**。感知层的协议定了基本不动，除非换硬件；控制层调完参数基本不动，除非换底盘；但决策层——比赛前一天要改流程的话，你就得改。如果决策代码里混着串口收发逻辑，改流程的时候一不小心把协议改了，车直接寄。

拿"走到 1 号点然后抓块"这个流程举个例：

```Python
async def zone1(fsm, act, cfg, state):
    await fsm.nav_to(1.0, 2.0)        # 走
    await fsm.spearhead_and_wait(1)    # 抓
    await fsm.rotate_to(0.0, 0.7, π)  # 转
```

决策层不知道 Pure Pursuit 怎么算的，不知道串口发了什么字节，它只管 `nav_to` → 等事件 → 下一步。底下发生了什么是感知层和控制层的事。

# 小结

ROS2 做 pub/sub 能用，但启动慢、序列化开销、spin 单线程这些问题是实际存在的。自研 EventBus 理论上简单，实际有跨进程、线程安全、背压等坑，全 Python 单进程可以搞，双进程老实用 ROS2 或 ZeroMQ。

三层架构的核心价值不是"代码好看"，是把变化频率不同的东西隔开——改决策不动控制，改控制不动感知。比赛前一天改方案的时候你会感谢这个分层。

下一章讲感知层——定位和视觉，搞清楚数据从哪来、什么质量。

# 第五章 感知与定位流水线

> 前面几章一直在说"定位数据"，但这个数据到底从哪来？精度怎么样？有什么坑？这一章把感知层的活讲清楚。
> 
> 

# 上位机需要什么数据

控制层和决策层不直接接触传感器，它们需要感知层提供干净的数据：

|谁需要|需要什么|干什么用|
|---|---|---|
|控制层|位姿 \(x, y, θ\)|Pure Pursuit 算前瞻点|
|控制层|速度 \(v, ω\)|闭环控制、航位推算|
|决策层|到达确认|知道车到了目标点，可以执行下一步|
|决策层|区域识别|知道车在哪个区域，切换任务|

感知层的活就是把这些数据从传感器里"榨出来"，滤波、校准、打包，交给上层用。

# 轮式里程计

最基础的定位方案：装在轮子上的编码器记录轮子转了多少圈，乘以轮子周长算出行驶距离，再根据左右轮差速算朝向。

```Plain Text
左轮走了 1.0m，右轮走了 1.05m
轮距 0.3m

前进距离 = (1.0 + 1.05) / 2 = 1.025m
转角 = (1.05 - 1.0) / 0.3 = 0.167 rad ≈ 9.6°
```

每帧做一次积分，不断累加就得到了全局位姿。

## 优势

- 不依赖外部传感器，纯靠轮子上的编码器

- 频率高（100Hz\+），更新快

- 计算量几乎为零

## 累积误差

里程计是积分算出来的，每帧都有微小误差，误差会不断累积：

```Plain Text
跑 1 圈（20m）：漂 2~5cm
跑 5 圈（100m）：漂 10~30cm
跑 10 圈（200m）：漂 30~80cm
```

轮子打滑（急加速、急转弯、地毯接缝）误差更大。

> 我 26 赛季用的就是纯里程计。短距离够用，跑几米到十几米误差在厘米级。但如果赛题要求跑几十米以上还不校正，里程计就不够了。
> 
> 

## **IMU 融合**

IMU（惯性测量单元）测三轴加速度和角速度，和轮式里程计融合后互相补短：

\- **打滑/碰撞检测：** 轮速显示在走，但 IMU 加速度对不上，说明轮子打滑或者车被撞了

\- **姿态补偿：** 车有俯仰、倾斜时，IMU 修正里程计的平面假设

\- **短时顶替：** 激光匹配失败、SLAM 输出不可信时，先用推算顶几秒

常见的融合方式是 EKF（扩展卡尔曼滤波）：把轮速和 IMU 数据按各自的噪声加权，输出一个比任何单一来源都稳的位姿。

```Plain Text
里程计（100Hz） + IMU（200Hz） → EKF → 融合位姿
```

> IMU 不是第二个里程计，它自己也会漂（尤其朝向角），单独用越跑越偏。它的价值是和轮式里程计融合：姿态归 IMU，位移归轮子，互相补短。纯 IMU 只能撑几秒，不是全程定位方案。
> 
> 

# 激光 SLAM

用激光雷达扫描周围环境，和已知地图（或在线建图）做匹配，算出车在地图里的位姿。

## 两个主流方案

**Cartographer（Google 开源）：** 建图和定位一体，第一次跑的时候在线建图，之后用这个地图定位。适合从零开始的场景。计算量比较大，在 Jetson 上跑要注意性能。

**AMCL（ROS 自带）：** 需要提前建好地图，然后在地图上做粒子滤波定位。比 Cartographer 轻量，但依赖已知地图。

```Plain Text
Cartographer：边跑边建图 → 生成地图 → 用地图定位
AMCL：提前建好地图 → 在地图上撒粒子 → 粒子收敛到位姿
```

## 匹配算法：ICP 和 NDT

激光 SLAM 的核心是点云匹配——把当前帧的点云和地图对齐，算出位姿。

**ICP（Iterative Closest Point）：** 迭代地找两个点云之间的对应关系，逐步对齐。简单直观，但对初始值敏感，初始偏差太大会收敛到错误结果。

**NDT（Normal Distributions Transform）：** 把空间划分成网格，每个网格用正态分布建模，然后优化点云在网格中的似然。比 ICP 对初始值更鲁棒，计算量也更稳定。

> 大多数 SLAM 框架用的是 NDT 或者改良版 ICP。选型的时候不用太纠结，用框架自带的就行，关键是调好参数（分辨率、最大迭代次数、收敛阈值）。
> 
> 

## 优势

- 全局定位：不靠积分，每帧独立算位姿，不累积误差

- 精度高：厘米级

- 能建图：第一次跑的时候在线建图，之后用这个地图定位

## 坑

**环境退化。** 长走廊、空旷区域、对称结构——激光雷达看到的特征太少，匹配不唯一，定位会飘或者跳。

退化的信号是匹配分数突然变差、协方差变大、位姿在相邻帧之间跳。发现退化后别继续信任激光输出，切到里程计 \+ IMU 的推算顶着，等特征恢复（出了走廊、拐了弯）再切回来：

```Plain Text
正常匹配：激光分数高、位姿连续
退化中：激光分数掉、位姿跳变 → 切里程计 + IMU 推算
恢复：分数回升、位姿稳定 → 切回激光 SLAM
```

有测距传感器（比如 DT35）时还能做"距离裁决"：激光里程计和 NDT 地图匹配"打架"、各说各话时，用测距量到已知墙面的距离，谁算出来的位置和这个距离对得上就信谁。

**匹配失败。** 车速太快、雷达转速不够、点云太稀疏，匹配算法找不到最优解，输出的位姿可能是错的。

**初始化。** 冷启动时不知道车在哪，需要在地图上撒一堆粒子（AMCL）或者靠里程计初值（Cartographer），这个过程要几秒到十几秒。

**地图依赖。** 赛场布局变了（每年赛题不同），地图要重新建。如果在线建图质量不好（建图时走的路径不够全），定位精度会受影响。

> 激光 SLAM 是 RC 赛场上定位精度最高的方案，但也是最容易踩坑的。环境退化和匹配失败在赛场上经常发生，需要做降级方案（匹配失败时切回里程计）。我没有实际用过 SLAM，这部分只是原理层面的了解，具体怎么调参怎么踩坑建议去找专门的 SLAM 教程。
> 
> 

# 相机标定

做视觉之前必须做的一件事。摄像头拍出来的图像有畸变——直线在边缘会变弯，距离测量不准。标定就是算出畸变参数，把图像"掰直"。

## 张正友标定法

用一张棋盘格标定板，从不同角度拍 15\~20 张照片，OpenCV 自动算出相机内参和畸变系数。

```Python
import cv2
import numpy as np

# 棋盘格内角点数（列, 行）
CHECKERBOARD = (9, 6)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 准备棋盘格的 3D 坐标（假设 z=0）
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

obj_points = []  # 3D 点
img_points = []  # 2D 点

for i in range(20):  # 拍 20 张
    frame = capture_frame()  # 你的摄像头取帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        obj_points.append(objp)
        img_points.append(corners2)

# 标定
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    obj_points, img_points, gray.shape[::-1], None, None)

print("相机内参:\n", camera_matrix)
print("畸变系数:\n", dist_coeffs)

# 保存
np.savez("calibration.npz", camera_matrix=camera_matrix, dist_coeffs=dist_coeffs)
```

标定完之后，用 `cv2.undistort()` 矫正图像：

```Python
data = np.load("calibration.npz")
undistorted = cv2.undistort(frame, data["camera_matrix"], data["dist_coeffs"])
```

> 标定做不好，后面所有视觉算法都是歪的。AprilTag 的位姿估计、色块的坐标测量、YOLO 的检测框位置——全依赖标定质量。拍棋盘格的时候多拍几个角度，远近左右倾斜都拍一些。
> 
> 

# 视觉定位

用摄像头识别赛场上的已知标记（AprilTag、色块、二维码），算出车的绝对位姿。

## AprilTag

AprilTag 是一种专门设计给机器人识别的二维码，贴在赛场的关键位置。摄像头拍到 AprilTag 后，通过 PnP 算法算出摄像头相对于 tag 的 6DoF 位姿（位置 \+ 朝向）。

```Plain Text
摄像头拍到 tag → 检测 tag 的角点 → PnP 算相对位姿 → 结合 tag 的已知坐标 → 车的全局位姿
```

```Python
from dt_apriltags import Detector

detector = Detector(families="tag36h11")
camera_params = (fx, fy, cx, cy)  # 从标定结果里拿

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
detections = detector.detect(gray, estimate_tag_pose=True, camera_params=camera_params, tag_size=0.1)

for det in detections:
    print(f"Tag ID: {det.tag_id}")
    print(f"位置: {det.pose_t.flatten()}")  # 相对于 tag 的平移
    print(f"旋转:\n{det.pose_R}")             # 相对于 tag 的旋转
```

## 色块识别

简单赛题可能只需要识别特定颜色的区域。HSV 颜色阈值 \+ 轮廓检测 \+ 最小外接矩形，几十行代码搞定。

```Python
import cv2
import numpy as np

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))  # 红色
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:
        x, y, w, h = cv2.boundingRect(cnt)
        center_x = x + w // 2
        center_y = y + h // 2
```

> 色块识别最大的问题是光照。同一个红色方块，在冷光灯下和暖光灯下 HSV 值差很多。现场调阈值是家常便饭，建议写成可调参数（上一章讲的 YAML 配置），别写死在代码里。
> 
> 

# YOLO 目标检测

当识别目标不是简单的色块或者 AprilTag，而是形状不规则、类别不同时（比如区分不同颜色的方块、识别障碍物、检测对手车辆），YOLO 是目前最常用的方案。

## YOLO 是什么

YOLO（You Only Look Once）是一个单阶段目标检测模型，输入一张图像，直接输出检测框的坐标、类别和置信度。速度快，适合实时场景。

```Plain Text
摄像头图像 → YOLO 模型 → [(x, y, w, h, class, confidence), ...]
```

## 训练

**准备数据集：** 用摄像头在赛场环境下拍 200\~500 张图片，用 LabelImg 或 Roboflow 标注。每个目标画框、标类别。

```Bash
pip install labelimg
labelimg  # 图形界面，框框点点就行
```

**训练配置（以 YOLOv8 为例）：**

```Bash
pip install ultralytics
```

```YAML
# data.yaml
train: ./dataset/train/images
val: ./dataset/val/images
nc: 3
names: ['red_block', 'blue_block', 'obstacle']
```

```Python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 加载预训练的 nano 模型（最轻量）
model.train(data="data.yaml", epochs=100, imgsz=640)
```

> 用 `yolov8n`（nano）就够了。RC 赛场上不需要大模型，推理速度比精度重要。nano 模型在 Jetson 上跑 30fps 没问题。
> 
> 

## 部署

训练完得到 `best.pt`，直接加载推理：

```Python
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

while True:
    ret, frame = cap.read()
    results = model(frame, conf=0.5)  # conf 是置信度阈值

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]
            print(f"{name}: ({x1:.0f},{y1:.0f})-({x2:.0f},{y2:.0f}) conf={conf:.2f}")
```

## TensorRT 加速

在 Jetson 上跑 YOLO，用 TensorRT 加速可以把推理速度提升 2\~3 倍：

```Python
# 导出 TensorRT 引擎
model.export(format="engine", device=0)  # 生成 best.engine

# 加载 TensorRT 引擎推理
model = YOLO("best.engine")
```

> TensorRT 引擎是和硬件绑定的，在 Jetson 上导出的 engine 不能拿到 x86 上用。每次换硬件要重新导出。
> 
> 

## YOLO 的坑

**数据集不够。** 200 张图训练出来的模型在训练集上 99% 准确率，到了赛场上灯光不一样、角度不一样、背景不一样，直接废掉。至少 500 张，多拍不同角度、不同光照。

**类别不平衡。** 训练集里红色方块 400 张、蓝色方块 50 张，模型会偏向识别红色。数据增强（翻转、旋转、亮度调整）可以缓解。

**误检。** 赛场上的背景杂物被识别成目标。提高置信度阈值（`conf=0.7`）可以减少误检，但也会漏检。需要在误检和漏检之间找平衡。

**推理延时。** YOLO 推理一帧要 20\~50ms（Jetson \+ TensorRT），加上摄像头采集延时，从目标出现到检测结果出来可能过了 80\~130ms。做实时控制的时候要考虑这个延时。

# OpenCV 图像预处理

不管是 AprilTag、色块还是 YOLO，原始图像在送进算法之前通常要做预处理。

## 常见预处理流水线

```Plain Text
原始图像
  → 畸变矫正（标定后的 undistort）
  → ROI 裁剪（只保留感兴趣区域，减少计算量）
  → 色彩空间转换（BGR → HSV / 灰度）
  → 滤波去噪（高斯模糊 / 中值滤波）
  → 送进检测算法
```

```Python
# 完整的预处理流水线
def preprocess(frame, roi, camera_matrix, dist_coeffs):
    # 1. 畸变矫正
    undistorted = cv2.undistort(frame, camera_matrix, dist_coeffs)

    # 2. ROI 裁剪（比如只看画面下方 2/3）
    x, y, w, h = roi
    cropped = undistorted[y:y+h, x:x+w]

    # 3. 高斯模糊去噪
    blurred = cv2.GaussianBlur(cropped, (5, 5), 0)

    # 4. 转 HSV
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    return hsv
```

## ROI 裁剪

ROI（Region of Interest）裁剪是减少计算量最简单有效的方法。如果你知道目标只出现在画面的某个区域，把其他区域裁掉：

```Python
# 只看画面下方 2/3（上方是天空/无关区域）
h, w = frame.shape[:2]
roi = frame[int(h*0.3):h, 0:w]
```

> 裁掉一半画面，计算量直接减半。在 Jetson 这种算力有限的平台上，ROI 裁剪是最简单的加速手段。
> 
> 

## 调试可视化

调视觉算法的时候一定要把中间结果画出来，不然出了问题不知道是哪一步坏的：

```Python
cv2.imshow("raw", frame)
cv2.imshow("undistorted", undistorted)
cv2.imshow("mask", mask)
cv2.imshow("result", result_frame)
cv2.waitKey(1)
```

> 不要只看最终结果。中间每一步的输出都看一下——畸变矫正对不对、HSV 阈值准不准、mask 有没有噪点、检测框位置对不对。哪一步出了问题就在哪一步修。
> 
> 

# DT35 校正

DT35 是一种激光位移传感器，精度很高（亚毫米级），可以用来做局部位置校正。

## 原理

在赛场的固定位置安装 DT35 传感器（或者把 DT35 装在车上对准固定参考面），测量车和参考面之间的距离。这个距离是绝对的、不累积的，可以用来修正里程计的累积误差。

```Plain Text
里程计说：我在 (1.02, 2.05)
DT35 说：我到墙面的距离是 0.400m，墙面在 x=1.428
实际 x 应该是 1.428 - 0.400 = 1.028
误差 = 1.028 - 1.02 = 0.008m = 8mm
```

## 26赛季的做法

我的代码里有一个 `dt35_correct()` 函数，在导航到目标点附近后开启 DT35，读取当前值，算误差，加到导航目标上做一次性修正：

```Python
async def dt35_correct(self, nav_x, nav_y, dt35_target_x, dt35_target_y, get_dt35, y_sign=-1.0):
    await asyncio.sleep(0.3)  # 等 DT35 值稳定

    dt35_x, dt35_y = get_dt35()
    err_x = dt35_x - dt35_target_x
    err_y = dt35_y - dt35_target_y

    corrected_x = nav_x + err_x
    corrected_y = nav_y + err_y * y_sign

    self.act.send_navigate(corrected_x, corrected_y, ...)
    return await self.wait_event("NAV_DONE")
```

思路是：先用里程计走到目标点附近（粗定位），再用 DT35 做精确修正（精定位）。里程计负责"大概到了"，DT35 负责"精确到位"。

> DT35 的局限是只能在特定位置生效（需要有参考面），不能全程提供定位。所以它适合做"到达校正"，不适合做"全程定位"。全程定位靠里程计或 SLAM，到了目标点附近用 DT35 修正。
> 
> 

# 选型建议

|方案|精度|频率|适用场景|复杂度|
|---|---|---|---|---|
|纯里程计|中（累积误差）|高（100Hz\+）|短距离、有校正点|低|
|激光 SLAM|高（厘米级）|中（10\~20Hz）|长距离、复杂环境|高|
|视觉 AprilTag|高（近距离）|中（30Hz）|有 tag 的固定位置|中|
|DT35 校正|极高（毫米级）|高|特定位置精校正|低|

实际比赛中大多数队伍用的是**组合方案**：

```Plain Text
里程计做高频推算（100Hz）→ 主要定位源
激光 SLAM 做低频校正（10Hz）→ 修正累积误差
DT35 做到达精校正 → 最后几厘米的精度
```

> 不要为了"高级"而上 SLAM。纯里程计够用就用纯里程计，简单、好调、不踩坑。等赛题真的要求长距离定位再上 SLAM。我是纯里程计 \+ DT35，差不多够用了。
> 
> 

# **降级链与冗余设计**

比赛现场什么都会坏：雷达过热、摄像头松了、IMU 掉线。设计定位系统时先想清楚一件事——如果这个传感器失灵了，谁来补？

一个可行的降级链：

```Plain Text
雷达 SLAM → 视觉 SLAM → 里程计 + IMU + DT35（机械定位）
```

- 雷达坏了：切视觉 SLAM，靠 AprilTag 或视觉里程计继续定位

- 雷达和摄像头都死了：切机械定位，码盘推算 \+ IMU 姿态 \+ DT35 到点校正

- 每一级切换都要有健康检查：匹配分数、检测频率、传感器心跳，连续几帧异常才降级，别被单帧噪声骗了

> 本质上前面所有方案都在做同一件事的两半：里程计负责"我相对刚才走了多少"，重定位负责"我在全局哪里"。怎么搭配、什么时候信谁，就是定位系统的设计核心。冗余设计花不了多少时间，但比赛时可能救一命。
> 
> 

# 第六章 协程驱动的异步决策系统

> 这一章讲的东西，是我 26 赛季重构决策代码的核心。1600 行 C\+\+ 嵌套状态机砍到 350 行 Python async 协程，改流程从"翻半天文件还经常改错"变成"改一个坐标就行了"。
> 
> 

# 为什么用 Python 而不是 C\+\+？

C\+\+20 也有协程了，`co_await`、`co_yield` 都有，理论上能写异步决策。但我还是选了 Python，原因很实际：

**决策逻辑不需要性能。** 决策层干的事是"走到 1 号点 → 抓块 → 走到 2 号点"，每个动作之间间隔几百毫秒到几秒，计算量几乎为零。不像 Pure Pursuit 要 50Hz 跑浮点运算，决策层一年的运算量可能还没有控制层一秒多。用 C\+\+ 跑决策就像开推土机去买菜。

**Python 的可读性和维护性碾压 C\+\+ 协程。** C\+\+20 协程的语法是出了名的难写难读——`promise_type`、`coroutine_handle`、`initial_suspend`、`final_suspend`，光配置一个协程就要写一堆 boilerplate。Python 的 `async/await` 是语言原生语法，写起来跟普通函数几乎一样。比赛前一天要改流程，Python 改两行就能跑，C\+\+ 可能要调半小时编译。

**C\+\+ 留给串口驱动和运动控制。** 真正吃性能的地方（串口收发、Pure Pursuit、图像处理）用 C\+\+，决策用 Python，各取所长。中间靠 ROS2 通信串起来。

> 不要为了"统一技术栈"而全部用 C\+\+，也不要因为"Python 慢"就不敢用。决策层不需要快，需要的是能改、能读懂、比赛前一天还能动。
> 
> 

# 阻塞代码的毁灭性后果

先看一段很多 RC 队伍都写过的代码：

```C++
void grab_block(int block_id) {
    send_command(block_id);           // 发指令
    while (!arm_done) {               // 死循环等
        sleep(100);                   // 每 100ms 看一眼
    }
    // 机械臂到位了，继续
}
```

看起来没问题对吧？发指令，等完成，继续。逻辑清晰。

但这个 `while + sleep` 会把整个线程卡住。在它 sleep 的这 100ms 里，ROS2 的回调全在排队——导航到了的到达信号、按钮按下的重试信号、传感器的新数据，全都处理不了。决策线程在睡觉，回调在等，两边互相卡。

> 我见过一个队，机械臂卡住了，`while (!arm_done)` 一直转，导航到了的回调排在后面收不到，车到了目标点不知道自己到了，继续在那原地等机械臂。
> 
> 

问题的根源是：**阻塞式代码一次只能干一件事。** 等机械臂的时候不能等急停，等导航的时候不能等按钮。你要是想同时等两件事，就得开多线程，然后线程之间共享状态、加锁、处理竞态。1600行的那坨就是这么来的。

# 异步：发指令，挂起，等回调

协程的思路完全不同。不是"发完指令然后死循环等"，而是"发完指令，挂起，让出控制权，等事件来了再唤醒"：

```Python
async def grab_block(fsm, block_id):
    send_command(block_id)                    # 发指令
    event = await fsm.wait_event("ARM_DONE")  # 挂起，让出控制权
    # 事件来了，自动恢复执行
```

`await` 的时候协程暂停了，但事件循环还在跑——急停回调、按钮回调、传感器回调全都能正常处理。等 `ARM_DONE` 事件到了，协程自动从 `await` 那一行恢复往下执行。

对比一下：

```Plain Text
阻塞写法：
  发指令 → sleep → sleep → sleep → sleep → 收到完成 → 继续
  （中间什么都干不了）

协程写法：
  发指令 → await（挂起）→ 事件循环继续跑其他回调 → 收到事件 → 恢复
  （挂起期间急停、按钮、传感器回调全不受影响）
```

这就是为什么 async/await 是硬件控制的"唯一解"——它解决了"等一件事的时候不能处理其他事"这个根本问题，而且不用开多线程。

# wait\_event 机制

核心就一个东西：**事件队列 \+ Future 挂起**。

```Python
class FSM:
    def __init__(self):
        self._waiters: list[tuple[str, asyncio.Future]] = []

    def post_event(self, event: Event):
        """从任意线程投递事件，唤醒所有匹配的 awaiter."""
        for event_type, future in self._waiters:
            if event_type == event.type and not future.done():
                future.set_result(event)
        self._waiters = [
            (et, f) for et, f in self._waiters if f.done()
        ]

    async def wait_event(self, event_type: str, timeout: float = None) -> Event:
        """等待指定类型的事件，挂起当前协程."""
        future = self._loop.create_future()
        self._waiters.append((event_type, future))

        try:
            if timeout:
                return await asyncio.wait_for(future, timeout)
            return await future
        except asyncio.TimeoutError:
            return Event(event_type, success=False)
```

流程是这样的：

1. 协程调 `wait_event("ARM_DONE")`，创建一个 Future，放进 waiters 列表，然后挂起

2. ROS2 回调线程收到 `/juece_ack`，调 `post_event(Event("ARM_DONE"))`

3. `post_event` 在 waiters 里找到匹配的 Future，`set_result` 唤醒它

4. 协程从 `await` 恢复，拿到事件，继续往下跑

`post_event` 用的是 `call_soon_threadsafe`，从 ROS2 回调线程安全地投递到 asyncio 事件循环：

```Python
def post_event(self, event: Event):
    if self._loop.is_running():
        self._loop.call_soon_threadsafe(self._dispatch_event, event)
    else:
        self._loop.call_soon(self._dispatch_event, event)
```

> 这个机制看起来简单，但它解决了一个很关键的问题：**ROS2 回调线程和 asyncio 决策线程之间的桥梁。** ROS2 回调是同步的，asyncio 是异步的，`call_soon_threadsafe` 是唯一安全的跨线程唤醒方式。
> 
> 

# 从 1600 行到 350 行

我 26 赛季之前的 C\+\+ 决策代码是这样的：

```C++
// 简化版，实际更惨
void DecisionNode::onTick() {
    switch (state_) {
        case ZONE1_NAV:
            if (nav_done_) {
                state_ = ZONE1_DT35;
                send_dt35_command();
            }
            break;
        case ZONE1_DT35:
            if (dt35_done_) {
                state_ = ZONE1_GRAB;
                send_grab_command(1);
            }
            break;
        case ZONE1_GRAB:
            if (arm_done_) {
                state_ = ZONE1_ROTATE;
                send_rotate_command(M_PI);
            }
            break;
        // ... 还有十几个 state
    }
}
```

每个状态一个 case，每个 case 里还要判断子状态、处理超时、处理异常。Zone1 有 8 个状态，Zone2 有 11 个状态，加上子状态总共 20 多个。状态之间的切换散落在 `onTick`、`handleSubEvent`、`enterSub` 三个函数里，改一个流程要在三个地方同步修改。

Python 协程版长这样：

```Python
async def zone1(fsm, act, cfg, state):
    for pt in cfg.zone1_route:
        await fsm.nav_to(pt.x, pt.y)          # 走到目标点
        await fsm.dt35_correct(...)             # DT35 微调
        await fsm.spearhead_and_wait(1)         # 抓矛头
        await fsm.rotate_to(0.0, 0.7, π)       # 转 180°
        await fsm.spearhead_and_wait(2)         # 对接
        await fsm.spearhead_and_wait(4)         # 完成
        await fsm.wait(3.0)                     # 等 3 秒
```

没有 switch\-case，没有状态编号，没有散落多处的切换逻辑。`await` 就是状态切换——每一行 `await` 就是一次"发指令 → 等完成 → 继续"。

> 1600 行里大概有 800 行是在管理状态切换本身（进入状态、退出状态、子状态、超时处理），真正干活的逻辑也就 300 行。协程把那 800 行管理代码全干掉了，剩下的就是业务逻辑本身。
> 
> 

# 原子动作与业务逻辑分离

这是重构过程中最重要的一个设计决策。

**原子动作**是硬件层面的能力，封装了时序和确认逻辑，改不得：

```Python
async def grab(fsm, act, block, need_stand=True, retract=False):
    """抓块流程：发指令 → 等机械臂到位 → 等吸盘确认."""
    if retract:
        act.publish_cmd_with_area(block=0, stand=1)
        await fsm.wait_event("ARM_DONE")

    act.publish_cmd_with_area(block=block, stand=1 if need_stand else 0)
    await fsm.wait(5.0 if block == 2 else 3.0)

    act.waiting_xipan = True
    act.publish_cmd_with_area(block=block, run=1)
    await fsm.wait_event("XIPAN_GRABBED")

    act.publish_cmd_with_area(block=block, run=0)
```

这里面的时序（先发 block 再发 run、等几秒再查吸盘、吸到了再清 run）是电控的硬件时序决定的，你改不了，也不该改。

**业务决策**是路线和顺序，天天变：

```Python
# 比赛前一天要改流程，你就改这里
cfg.zone1_route = [4, 5]    # → 改成 [5, 4]
cfg.zone2_tasks = [...]      # → 重新排任务顺序
```

```Python
async def zone2(fsm, act, cfg, state):
    await grab(fsm, act, block=2, need_stand=True)     # 先抓 2 号
    await grab(fsm, act, block=1, need_stand=True)     # 再抓 1 号
    await do_stair(fsm, act, 1)                         # 上台阶
```

grab 和 do\_stair 是原子动作，zone2 里的调用顺序是业务决策。改顺序不用动 grab 的实现，改 grab 的实现不影响业务逻辑。

> 26 赛季改过三次流程，每次就是改 `zone2` 函数里的几行调用顺序。如果还是 C\+\+ 那套 1600 行的状态机，改一次至少半天，还得祈祷没改错状态编号。
> 
> 

# 超时、重试与急停

## 超时

硬件不是每次都靠谱。机械臂可能卡住，导航可能到不了，每个 `wait_event` 都要带超时：

```Python
result = await fsm.wait_event("ARM_DONE", timeout=5.0)
if not result.success:
    log.warning("ARM_DONE 超时，跳过")
```

超时了就返回一个 `success=False` 的事件，协程继续往下跑，不会卡死。

我的代码里还有一个 `force_skip_upper()` 的机制——超时后不光跳过等待，还要抑制后续的 `up_free=1` 信号，防止下位机恢复后又触发一轮等待：

```Python
def force_skip_upper(self):
    self.suppress_up_busy = True    # 后续 up_free=1 全部忽略
    self.up_free = True             # 立即标记为空闲
```

## 重试

有些操作值得重试，比如矛头抓取：

```Python
result = await fsm.spearhead_and_wait(1, up_timeout=5.0)
if not result.success:
    log.warning("矛头抓取失败，重试一次")
    result = await fsm.spearhead_and_wait(1, up_timeout=5.0)
    if not result.success:
        log.warning("重试也失败了，继续往下走")
```

重试次数不能太多——赛场上时间是有限的，卡在一个动作上重试 5 次，后面的任务全来不及。

## 急停

急停不是软件管的事。我们的车用遥控器控制，有问题了直接按遥控器，电控那边收到信号直接断电停车，不经过上位机。

软件层面要做的是：车已经停了，决策协程还在 `await` 等事件呢，别让它卡在那。实际操作就是 kill 掉进程重新跑。不需要在每个 `await` 里检查急停标志——硬件都停了，软件清理不清理无所谓，重来就行。

> 急停要的是快，遥控器一按硬件就停了，比任何软件方案都可靠。别在软件里搞急停逻辑，那是电控的事。
> 
> 

# 并行等待

有时候需要同时等两件事。比如"一边走导航一边等机械臂准备好"：

```Python
await asyncio.gather(
    fsm.nav_to(1.0, 2.0),
    fsm.wait_event("ARM_READY"),
)
```

`asyncio.gather` 同时挂起两个协程，任意一个先完成都不影响另一个继续等。两个都完成了才往下走。

也有"等任意一个先到"的场景：

```Python
event = await fsm.wait_event_any("NAV_DONE", "EMERGENCY_STOP")
if event.type == "EMERGENCY_STOP":
    return  # 急停了，不继续
```

# 小结

协程决策的本质就一句话：**用 ****`await`**** 替代 ****`while + sleep`****，用事件替代状态变量。**

阻塞式代码把"等硬件"和"处理其他事件"耦合在一起，协程把它们彻底分开——挂起等硬件的时候，事件循环该处理急停处理急停，该处理按钮处理按钮。

1600 行到 350 行不是因为 Python 比 C\+\+ 短，而是因为协程干掉了状态管理本身。剩下的 350 行全是业务逻辑，改流程改的就是这 350 行里的几行调用顺序。

# 第七章 底盘运动学与 Pure Pursuit 轨迹跟踪

> 这一章的代码我 26 赛季没有实际写过（车用的是纯里程计 \+ DT35 微调），但 Pure Pursuit 是 RC 赛场上用得最多的路径跟踪算法，原理和实现都值得讲清楚。
> 
> 

# 为什么不用 nav2

ROS2 自带的 nav2 导航栈是给服务机器人设计的——在办公楼里慢悠悠地走，遇到人停下来，绕个障碍物再继续。它的核心是 Costmap（代价地图）\+ 全局规划器 \+ 局部控制器，整套流程假设你不知道地图、需要实时避障、速度很慢。

RC 赛场完全不是这个场景：

**地图是已知的。** 赛场布局提前公布，路径可以离线规划好，不需要边跑边建图。

**不需要避障。** 赛场上没有行人、没有突然出现的障碍物（如果有的话那是赛道设计有问题）。车要做的就是沿着规划好的路径高速通过。

**速度要求高。** nav2 的控制频率和响应速度跟不上 RC 赛车的需求。它的局部控制器（DWB / MPPI）要考虑避障、要考虑代价地图膨胀，计算量不小。

**Costmap 在 RC 赛场边缘会出问题。** 赛道边界在 Costmap 里是高代价区域，车靠近边界时 nav2 会试图"推开"，导致车在边缘原地打转或者反复震荡。这是架构层面的问题，调参解决不了。

> 结论：nav2 能用，但 RC 赛车不需要它的核心能力（避障、建图），反而会被它的开销拖累。自己写一个 Pure Pursuit 就够了。
> 
> 

# 底盘逆运动学

在写跟踪算法之前，得先搞清楚"给定一个速度指令，每个轮子该怎么转"。

## 差速底盘

两个驱动轮 \+ 一个万向轮，最常见的 RC 底盘。

```Plain Text
┌─────────┐
    │         │
  ┌─┤         ├─┐
  │L│         │R│
  └─┤         ├─┘
    │    C    │
    └─────────┘
```

给定线速度 `v` 和角速度 `ω`：

```Plain Text
v_L = v - (ω × L / 2)
v_R = v + (ω × L / 2)
```

其中 `L` 是轮距（两个驱动轮之间的距离）。

反过来，从轮速算整车速度：

```Plain Text
v = (v_R + v_L) / 2
ω = (v_R - v_L) / L
```

## 麦克纳姆轮底盘

四个轮子，每个轮子 45° 安装辊子，能全向移动。

```Plain Text
↖  ┌─────────┐  ↗
     │         │
  ↙  │         │  ↘
     └─────────┘
```

逆运动学：

```Plain Text
v_FL = v_x - v_y - ω × (L + W) / 2
v_FR = v_x + v_y + ω × (L + W) / 2
v_RL = v_x + v_y - ω × (L + W) / 2
v_RR = v_x - v_y + ω × (L + W) / 2
```

其中 `L` 是轴距，`W` 是轮距。FL/FR/RL/RR 分别是左前/右前/左后/右后。

> 麦克纳姆轮的好处是能横移，对需要侧方停靠的赛题很有用。但辊子磨损快，赛场地面如果有沙子或地毯接缝，打滑会很严重。
> 
> 

# Pure Pursuit 数学原理

Pure Pursuit 的思想非常直观：在规划路径上找一个"前瞻点"（lookahead point），然后算出一条圆弧让车沿着这条弧走到前瞻点。

## 几何推导

```Plain Text
●  前瞻点 (target)
        /|
       / |
    Ld/  | y
     /   |
    /    |
   ●─────●
 车当前位置
```

- 车在原点，朝向 x 轴正方向

- 前瞻点在车体坐标系下的坐标为 `(x, y)`

- `Ld` = 前瞻距离（车到前瞻点的直线距离）

- `α` = 前瞻点相对于车头朝向的夹角

由几何关系：

```Plain Text
sin(α) = y / Ld
```

跟踪圆弧的曲率 `κ`：

```Plain Text
κ = 2 × sin(α) / Ld = 2y / Ld²
```

角速度：

```Plain Text
ω = v × κ = 2vy / Ld²
```

这就是 Pure Pursuit 的全部数学。给定前瞻点坐标 `(x, y)` 和当前速度 `v`，算出角速度 `ω`，发给底盘。

## 前瞻距离 Ld 的选择

`Ld` 是 Pure Pursuit 唯一的关键参数，它决定了跟踪行为：

|Ld 大|Ld 小|
|---|---|
|跟踪平滑，不走蛇形|跟踪精确，紧跟路径|
|过弯时切弯严重|过弯时响应快但容易震荡|
|适合高速直道|适合低速弯道|

实践中通常让 `Ld` 随速度变化：

```Python
Ld = max(Ld_min, k × v)  # k 通常取 0.5~1.5
```

速度快的时候前瞻距离拉远，避免来回修正；速度慢的时候前瞻距离拉近，保证精度。

## 实现

```Python
import math

def pure_pursuit(state, path, v, Ld_min=0.3, k=1.0):
    """
    state: (x, y, theta) 当前位姿
    path: [(x1,y1), (x2,y2), ...] 路径点列表
    v: 当前线速度
    """
    x, y, theta = state

    # 1. 找到路径上离车最近的点
    min_dist = float('inf')
    nearest_idx = 0
    for i, (px, py) in enumerate(path):
        d = math.hypot(px - x, py - y)
        if d < min_dist:
            min_dist = d
            nearest_idx = i

    # 2. 从最近点往前搜索，找到距离 >= Ld 的前瞻点
    Ld = max(Ld_min, k * v)
    target = path[-1]  # 默认用终点
    for i in range(nearest_idx, len(path)):
        px, py = path[i]
        d = math.hypot(px - x, py - y)
        if d >= Ld:
            target = (px, py)
            break

    # 3. 把前瞻点转换到车体坐标系
    dx = target[0] - x
    dy = target[1] - y
    local_x =  dx * math.cos(theta) + dy * math.sin(theta)
    local_y = -dx * math.sin(theta) + dy * math.cos(theta)

    # 4. 算曲率和角速度
    Ld_actual = math.hypot(local_x, local_y)
    if Ld_actual < 0.01:
        return 0.0
    curvature = 2.0 * local_y / (Ld_actual ** 2)
    omega = v * curvature

    return omega
```

调用：

```Python
state = (1.0, 2.0, 0.5)  # x, y, theta
path = [(0, 0), (1, 0), (2, 0.5), (3, 1.5), (3, 3)]
v = 1.0

omega = pure_pursuit(state, path, v)
# omega 发给底盘
```

> 整个算法就一个 for 循环加几行三角函数，没有矩阵、没有优化器、没有迭代求解。这就是 Pure Pursuit 为什么适合 RC——简单、快、好调。
> 
> 

# 路径规划

Pure Pursuit 解决的是"怎么沿着路径走"，但路径本身从哪来？

## 手动标点

最简单的方式：提前在赛场地图上标好关键路径点，存成数组。

```Python
# 蓝区 Zone1 路径
path = [
    (0.0, 0.0),
    (1.0, 0.0),
    (2.0, 0.5),
    (3.0, 1.5),
    (3.0, 3.0),
]
```

够用就行，不需要花里胡哨。很多 RC 队伍就是手动标点 \+ Pure Pursuit 跑完全程。

## A\* 全局规划

如果赛场有障碍物需要绕行，可以用 A\* 在栅格地图上找最短路径：

```Python
import heapq

def astar(grid, start, end):
    """grid: 2D 数组, 0=可通行, 1=障碍"""
    rows, cols = len(grid), len(grid[0])
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_g = g_score[current] + (1.414 if dx*dy != 0 else 1)
                if new_g < g_score.get((nx,ny), float('inf')):
                    g_score[(nx,ny)] = new_g
                    f = new_g + abs(nx-end[0]) + abs(ny-end[1])
                    heapq.heappush(open_set, (f, (nx,ny)))
                    came_from[(nx,ny)] = current
    return []
```

A\* 出来的路径是折线，直接丢给 Pure Pursuit 会走出锯齿。需要做平滑。

## 贝塞尔曲线平滑

用贝塞尔曲线把折线路径变成光滑曲线：

```Python
def bezier_curve(points, n=100):
    """n 阶贝塞尔曲线，points 是控制点列表"""
    n_pts = len(points)
    curve = []
    for t_i in range(n + 1):
        t = t_i / n
        # de Casteljau 算法
        temp = list(points)
        for k in range(n_pts - 1):
            temp = [
                ((1-t) * temp[i][0] + t * temp[i+1][0],
                 (1-t) * temp[i][1] + t * temp[i+1][1])
                for i in range(len(temp) - 1)
            ]
        curve.append(temp[0])
    return curve
```

用法：

```Python
# A* 出来的折线
waypoints = [(0,0), (1,1), (2,1), (3,2)]

# 贝塞尔平滑
smooth_path = bezier_curve(waypoints, n=200)

# 丢给 Pure Pursuit
omega = pure_pursuit(state, smooth_path, v)
```

> 实际比赛中大多数队伍用的是手动标点，不用 A\*。赛场布局已知，路径就那么几条，手动标比跑 A\* 省事。贝塞尔平滑倒是值得用——手动标的点之间用贝塞尔连一下，过弯会顺滑很多。
> 
> 

# 物理世界的坑

算法在仿真里跑得好好的，上实车就出问题。这是 RC 导航最头疼的部分。

## 蛇形走位 / 画龙

车走直线的时候左右小幅摆动，像蛇一样。

**原因：** 定位数据有高频噪声。激光 SLAM 或里程计的输出每一帧都有几厘米的抖动，Pure Pursuit 每一帧都在修正这个抖动，越修越抖。

**解法：** 低通滤波。对定位数据做滑动平均，滤掉高频噪声：

```Python
class LowPassFilter:
    def __init__(self, alpha=0.3):
        self.alpha = alpha
        self.value = None

    def update(self, new_value):
        if self.value is None:
            self.value = new_value
        else:
            self.value = self.alpha * new_value + (1 - self.alpha) * self.value
        return self.value

# 用法
filter_x = LowPassFilter(alpha=0.3)
filter_y = LowPassFilter(alpha=0.3)

while running:
    raw_x, raw_y = get_position()
    x = filter_x.update(raw_x)
    y = filter_y.update(raw_y)
    omega = pure_pursuit((x, y, theta), path, v)
```

`alpha` 越小滤波越强，响应越慢。取值 0\.2\~0\.5 之间调。

## 过弯过冲 / 走对数曲线

车到了弯道应该转弯，但转不过来，冲出赛道。或者走着走着走出一条越来越弯的弧线。

**原因：** 定位数据有延时。激光 SLAM 处理一帧要 50\~100ms，你拿到的位姿是 100ms 之前的，但 Pure Pursuit 用这个"旧"位姿算出来的角速度是针对 100ms 前的位置的。速度越快，100ms 的位移越大，误差越大。

**解法：** 航位推算补偿。用上一帧的速度和角速度，把位姿往前推算 100ms：

```Python
def predict_state(state, v, omega, dt):
    """航位推算：用运动模型预测 dt 秒后的位姿"""
    x, y, theta = state
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt
    return (x, y, theta)

# 收到定位数据后，推算到"当前时刻"
state = get_position()              # 这是 100ms 前的位姿
state = predict_state(state, v, omega, 0.1)  # 推算到现在
omega = pure_pursuit(state, path, v)
```

## 坐标瞬移 / 重定位跳变

车走着走着，定位突然跳了几十厘米甚至几米。Pure Pursuit 看到位置突然变了，以为车偏了，猛打方向，车直接甩尾。

**原因：** ICP/NDT 匹配失败后重新匹配成功，或者粒子滤波重采样后粒子收敛到了新位置。这在环境退化（长走廊、空旷区域）时容易发生。

**解法：** 没有完美解法。几个缓解措施：

- 对定位输出做异常值检测，跳变超过阈值就丢弃这一帧

- 用轮式里程计做降级，定位跳变时切回里程计

- 过滤器的 `alpha` 调小，让定位变化更平滑

> 这些问题在仿真里全都碰不到——仿真器的定位是完美的，没有噪声、没有延时、没有跳变。所以上实车之前一定要做故障注入测试（下一章会讲）。
> 
> 

# 小结

Pure Pursuit 就三步：找前瞻点 → 算曲率 → 发角速度。数学不复杂，实现不复杂，调 `Ld` 一个参数就能出效果。

真正难的是物理世界——定位有噪声、有延时、有跳变，算法在仿真里跑得好好的上实车就蛇形走位。低通滤波、航位推算、异常值检测这些"补丁"才是决定车能不能跑稳的关键。

# 第八章 脱离硬件的软件在环仿真

> 上一章的 Pure Pursuit 代码在控制台跑了一下输出数字就完事了，根本看不出来车走得好不好。这一章我们把它接到一个 2D 仿真器里，屏幕上能看到车在走、路径在那、前瞻点在动——改一个参数立刻看到效果。
> 
> 

# 为什么要仿真？

上实车之前先在电脑上跑通，这不是偷懒，是省时间。

**实车调试成本高。** 要搬设备、接线、找场地、调完发现问题要重新编译部署。一轮下来半小时起步。

**仿真可以无限重复。** 同一条路径跑 100 遍，改 100 个参数，每遍 5 秒出结果。实车跑 100 遍要一整天。

**仿真可以注入故障。** 给定位加 100ms 延时、加高频噪声、模拟跳变——这些在实车上很难复现，在仿真里改一个数字就行。

**仿真不会撞墙。** 算法有 bug 车飞出赛道，在仿真里就是屏幕上一个小图标飞出画面，重启就行。实车上飞出去要捡车、可能还要修。

# 开始之前你需要什么

这个仿真方案用的是 Python \+ Pygame，不需要装 ROS2，不需要 Docker，不需要任何重型工具。

**Python 3\.10\+：** 你电脑上应该已经有了。

**Pygame：** 一个 Python 的 2D 游戏库，用来画画面和处理键盘输入。

```Bash
pip install pygame
```

装完跑一下确认没问题：

```Python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("test")
print("pygame ok")
pygame.quit()
```

能看到窗口弹出来就行。

**上一章的 Pure Pursuit 函数：** 直接拿过来用，不用改。

就这些。不需要 ROS2，不需要 C\+\+，不需要编译。

# 仿真器的基本结构

一个 2D 仿真器的核心就三样东西：

```Plain Text
物理模型：给定速度指令，算出下一帧的位姿
渲染：把位姿画到屏幕上
循环：每帧执行 物理更新 → 渲染 → 等待下一帧
```

## 运动学积分器

上一章讲了底盘逆运动学（给定 v 和 ω 算轮速），这里用它的正运动学——给定 v 和 ω 算下一帧的位姿：

```Python
import math

def step(state, v, omega, dt):
    """
    运动学积分：给定当前位姿和速度指令，算出 dt 秒后的位姿。
    state: (x, y, theta)
    v: 线速度 m/s
    omega: 角速度 rad/s
    dt: 时间步长 s
    """
    x, y, theta = state
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt
    return (x, y, theta)
```

这就是仿真的"物理引擎"——一条公式。车每帧根据当前速度和朝向往前走一小步。

> dt 取 0\.02s（50Hz），和实际控制频率一致。dt 太大积分会不准（车走出折线），dt 太小浪费算力。
> 
> 

## 坐标系

屏幕坐标系和数学坐标系不一样——屏幕 y 轴向下，数学 y 轴向上。仿真里用数学坐标系（y 向上），画到屏幕上的时候做一次翻转：

```Python
def world_to_screen(x, y, screen_w, screen_h, scale, offset_x, offset_y):
    """数学坐标 → 屏幕坐标"""
    sx = int(x * scale + offset_x)
    sy = int(screen_h - (y * scale + offset_y))  # y 轴翻转
    return sx, sy
```

`scale` 控制"1 米等于多少像素"，`offset_x/offset_y` 控制画面偏移。

# 完整的仿真器

把上面的东西组装起来：

```Python
import pygame
import math

# ── Pure Pursuit（上一章的代码） ──

def pure_pursuit(state, path, v, Ld_min=0.3, k=1.0):
    x, y, theta = state
    min_dist = float('inf')
    nearest_idx = 0
    for i, (px, py) in enumerate(path):
        d = math.hypot(px - x, py - y)
        if d < min_dist:
            min_dist = d
            nearest_idx = i
    Ld = max(Ld_min, k * v)
    target = path[-1]
    for i in range(nearest_idx, len(path)):
        px, py = path[i]
        d = math.hypot(px - x, py - y)
        if d >= Ld:
            target = (px, py)
            break
    dx = target[0] - x
    dy = target[1] - y
    local_x =  dx * math.cos(theta) + dy * math.sin(theta)
    local_y = -dx * math.sin(theta) + dy * math.cos(theta)
    Ld_actual = math.hypot(local_x, local_y)
    if Ld_actual < 0.01:
        return 0.0, target
    curvature = 2.0 * local_y / (Ld_actual ** 2)
    omega = v * curvature
    return omega, target

# ── 运动学积分 ──

def step(state, v, omega, dt):
    x, y, theta = state
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt
    return (x, y, theta)

# ── 坐标转换 ──

def world_to_screen(x, y, sw, sh, scale, ox, oy):
    return (int(x * scale + ox), int(sh - (y * scale + oy)))

# ── 主仿真 ──

def main():
    # 路径
    path = [(0,0), (2,0), (4,1), (5,3), (5,5), (3,6), (1,6)]

    # 初始状态
    state = (0.0, 0.0, 0.0)
    v = 1.5          # 速度 m/s
    dt = 0.02         # 50Hz
    trail = []        # 轨迹

    # Pygame 初始化
    pygame.init()
    sw, sh = 900, 700
    screen = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption("Pure Pursuit 仿真")
    clock = pygame.time.Clock()

    # 坐标参数：1米=80像素，原点偏移到左下角
    scale = 80
    ox, oy = 100, 100

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R 键重置
                    state = (0.0, 0.0, 0.0)
                    trail.clear()
                if event.key == pygame.K_UP:
                    v += 0.2
                if event.key == pygame.K_DOWN:
                    v -= 0.2

        # 物理更新
        omega, target = pure_pursuit(state, path, v)
        state = step(state, v, omega, dt)
        trail.append((state[0], state[1]))

        # 渲染
        screen.fill((30, 30, 30))

        # 画路径
        pts = [world_to_screen(px, py, sw, sh, scale, ox, oy) for px, py in path]
        if len(pts) > 1:
            pygame.draw.lines(screen, (100, 200, 100), False, pts, 2)

        # 画轨迹
        if len(trail) > 1:
            tpts = [world_to_screen(tx, ty, sw, sh, scale, ox, oy) for tx, ty in trail]
            pygame.draw.lines(screen, (50, 100, 200), False, tpts, 1)

        # 画前瞻点
        tx, ty = world_to_screen(target[0], target[1], sw, sh, scale, ox, oy)
        pygame.draw.circle(screen, (255, 200, 0), (tx, ty), 5)

        # 画车（三角形）
        cx, cy = world_to_screen(state[0], state[1], sw, sh, scale, ox, oy)
        angle = state[2]
        car_len = 15
        p1 = (cx + car_len * math.cos(angle), cy - car_len * math.sin(angle))
        p2 = (cx + car_len * math.cos(angle + 2.5), cy - car_len * math.sin(angle + 2.5))
        p3 = (cx + car_len * math.cos(angle - 2.5), cy - car_len * math.sin(angle - 2.5))
        pygame.draw.polygon(screen, (255, 80, 80), [p1, p2, p3])

        # HUD
        font = pygame.font.SysFont(None, 24)
        hud = font.render(f"v={v:.1f} m/s  Ld={max(0.3, 1.0*v):.2f}m  [R]重置 [↑↓]调速", True, (200,200,200))
        screen.blit(hud, (10, 10))

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()

if __name__ == "__main__":
    main()
```

```Bash
python pursuit_sim.py
```

跑起来你能看到：

- 绿线是规划路径

- 蓝线是车实际走的轨迹

- 黄点是前瞻点

- 红色三角形是车

- 按上下箭头调速度，按 R 重置

改一下 `path` 里的坐标、改一下 `v` 的值、改一下 `Ld_min`，立刻看到效果。比控制台输出数字直观一万倍。

# 故障注入：压测算法鲁棒性

仿真器跑通了，但这只是理想情况——定位完美、没有延时、没有噪声。实车上不是这样的。

## 加定位延时

激光 SLAM 处理一帧要 50\~100ms，你拿到的位姿是过去的。在仿真里模拟这个延时：

```Python
from collections import deque

class DelayBuffer:
    def __init__(self, delay_steps):
        self.buffer = deque(maxlen=delay_steps + 1)

    def push(self, state):
        self.buffer.append(state)

    def get(self):
        if len(self.buffer) < self.buffer.maxlen:
            return self.buffer[0]  # 缓冲区没满，用最早的
        return self.buffer[0]      # 返回 delay_steps 帧前的数据

# 用法
delay = DelayBuffer(delay_steps=5)  # 5帧 × 0.02s = 100ms 延时

while running:
    delay.push(state)                    # 每帧把真实位姿塞进缓冲区
    delayed_state = delay.get()          # 取出 100ms 前的位姿
    omega, target = pure_pursuit(delayed_state, path, v)  # 用旧位姿算控制量
    state = step(state, v, omega, dt)    # 但物理更新用真实位姿
```

加上 100ms 延时后，过弯的时候车会明显切弯。速度越快切得越厉害。

## 加定位噪声

```Python
import random

def add_noise(state, pos_std=0.02, angle_std=0.01):
    """给位姿加高斯噪声"""
    x, y, theta = state
    return (
        x + random.gauss(0, pos_std),      # 位置噪声 2cm
        y + random.gauss(0, pos_std),
        theta + random.gauss(0, angle_std), # 角度噪声 0.01rad
    )

# 用法
noisy_state = add_noise(state)
omega, target = pure_pursuit(noisy_state, path, v)
```

噪声加到 5cm 以上，车就开始蛇形走位了。这时候就知道上一章说的低通滤波为什么重要。

## 加定位跳变

```Python
def maybe_jump(state, jump_prob=0.005, jump_dist=0.3):
    """0.5% 概率产生 30cm 的跳变"""
    if random.random() < jump_prob:
        x, y, theta = state
        return (x + random.uniform(-jump_dist, jump_dist),
                y + random.uniform(-jump_dist, jump_dist),
                theta)
    return state
```

跳变发生的时候，Pure Pursuit 会猛打方向。这就是为什么实车上要做异常值检测。

## 组合起来

```Python
delay = DelayBuffer(delay_steps=5)

while running:
    # 真实位姿
    omega, target = pure_pursuit(observed_state, path, v)
    state = step(state, v, omega, dt)

    # 观测位姿 = 真实位姿 + 延时 + 噪声 + 可能的跳变
    observed = add_noise(state)
    observed = maybe_jump(observed)
    delay.push(observed)
    observed_state = delay.get()
```

> 仿真的价值不是"跑通了算法"，而是"在各种恶劣条件下跑通了算法"。加上延时、噪声、跳变之后还能稳定跟踪的代码，上实车才有底气。
> 
> 

# 改参数的直观感受

仿真最大的好处是改参数立刻看到效果。试一下这些：

```Python
# Ld 从 0.3 改到 2.0，看车怎么变
# v 从 0.5 改到 3.0，看过弯切多少
# 噪声从 0.01 改到 0.1，看蛇形走位多严重
# 延时从 0 改到 200ms，看过弯过冲多少
```

每个参数改一下，跑 10 秒看效果，比在实车上调参快 100 倍。

# 小结

仿真的核心就是三条：运动学积分算位姿、Pygame 画到屏幕上、故障注入压测算法。

不需要 ROS2，不需要 Gazebo，不需要 Docker。一个 Python 文件，几十行代码，就能在电脑上看到车怎么跑、哪里会出问题。上一章的 Pure Pursuit 调好参数、加上滤波和补偿，再往这个仿真器里一跑，上实车之前心里就有数了。

# 第九章 现场调参与参数热加载

> 前面几章的代码里到处是 magic number——Pure Pursuit 的前瞻距离写死 0\.8，速度上限写死 1\.5，PID 增益写死 1\.2。这些数字在赛场上是要反复调的，如果每次改一个数字都要改代码、重新编译、重新部署，那赛前调试的时间全浪费在等编译上了。
> 
> 

# 为什么需要参数管理

赛场上调参是这样的：

"速度太快了过弯打滑，降到 1\.2 试试。"

"前瞻距离太小了走蛇形，改大一点。"

"PID 的 D 项太大了有高频抖动，去掉。"

每一句都是在改一个数字。如果这个数字写死在代码里，流程就是：改代码 → 编译 → 部署 → 跑一遍 → 不行再改 → 编译 → 部署……一轮下来 5 分钟没了，一天调不了几轮。

如果这个数字在配置文件里，流程就是：改配置文件 → 重启程序（甚至不重启）→ 跑一遍 → 不行再改。一轮 30 秒。

> 赛场上一天能跑的次数是有限的，每多编译一次就少跑一次。参数管理不是锦上添花，是直接决定赛前能调多少轮。
> 
> 

# YAML 配置文件

把所有可调参数抽到 YAML 文件里，程序启动时读取。

```YAML
# config/params.yaml

pure_pursuit:
  lookahead_min: 0.3      # 最小前瞻距离 m
  lookahead_k: 1.0        # 前瞻距离 = max(min, k * v)
  max_speed: 2.0          # 最大速度 m/s
  min_speed: 0.3          # 最小速度 m/s

pid:
  linear_kp: 1.2
  linear_ki: 0.01
  linear_kd: 0.3
  angular_kp: 2.0
  angular_ki: 0.0
  angular_kd: 0.5

chassis:
  wheel_base: 0.3         # 轮距 m
  max_angular_vel: 2.0    # 最大角速度 rad/s

paths:
  zone1:
    - [0.0, 0.0]
    - [1.0, 0.0]
    - [2.0, 0.5]
    - [3.0, 1.5]
```

Python 读取用 `pyyaml`：

```Bash
pip install pyyaml
```

```Python
import yaml

def load_config(path="config/params.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

cfg = load_config()

# 用的时候
v_max = cfg["pure_pursuit"]["max_speed"]
Ld_min = cfg["pure_pursuit"]["lookahead_min"]
kp = cfg["pid"]["angular_kp"]
```

C\+\+ 读取用 `yaml-cpp`：

```C++
#include <yaml-cpp/yaml.h>

YAML::Node cfg = YAML::LoadFile("config/params.yaml");

double v_max = cfg["pure_pursuit"]["max_speed"].as<double>();
double Ld_min = cfg["pure_pursuit"]["lookahead_min"].as<double>();
double kp = cfg["pid"]["angular_kp"].as<double>();
```

> 把路径点也写在 YAML 里，改流程就是改坐标，不用动代码。我的 `decision.py` 里 zone1 的路线就是从 ROS2 参数读的，改一个数字就行。
> 
> 

# ROS2 Parameter

如果你的系统已经在用 ROS2，那它自带一套参数系统，不用白不用。

## 声明参数

在节点里声明参数，带默认值：

```Python
class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')

        # 声明参数，默认值在括号里
        self.declare_parameter('lookahead_min', 0.3)
        self.declare_parameter('lookahead_k', 1.0)
        self.declare_parameter('max_speed', 2.0)
        self.declare_parameter('pid_kp', 1.2)

    def get_params(self):
        return {
            'Ld_min': self.get_parameter('lookahead_min').value,
            'Ld_k': self.get_parameter('lookahead_k').value,
            'v_max': self.get_parameter('max_speed').value,
            'kp': self.get_parameter('pid_kp').value,
        }
```

## 从 launch 文件传参

```Python
# launch/control.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('max_speed', default_value='2.0'),
        Node(
            package='r2_control',
            executable='control_node',
            parameters=[{
                'max_speed': LaunchConfiguration('max_speed'),
                'lookahead_min': 0.3,
                'pid_kp': 1.2,
            }]
        )
    ])
```

启动时传参：

```Bash
ros2 launch r2_control control.launch.py max_speed:=1.5
```

## 运行时改参数

程序跑着的时候，一行命令改参数：

```Bash
ros2 param set /control_node max_speed 1.2
ros2 param set /control_node lookahead_min 0.5
```

不用重启程序，改完立刻生效（如果代码里处理了参数更新的话）。

## 参数更新回调

要让参数改了立刻生效，注册一个回调：

```Python
class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.declare_parameter('max_speed', 2.0)
        self.v_max = 2.0

        # 注册参数更新回调
        self.add_on_set_parameters_callback(self.on_param_change)

    def on_param_change(self, params):
        for param in params:
            if param.name == 'max_speed':
                self.v_max = param.value
                self.get_logger().info(f'v_max updated to {param.value}')
        return SetParametersResult(successful=True)
```

> 26赛季的决策节点参数全是通过 ROS2 Parameter 加载的，红蓝区两套参数、zone1 路径点、DT35 目标值全在 launch 文件里。切红蓝区就是换一套参数，不用改代码。
> 
> 

# 不用 ROS2 的热重载方案

如果你没用 ROS2，自己实现一个文件监听也很简单。思路是：起一个后台线程，每隔几秒检查 YAML 文件的修改时间，变了就重新读取。

```Python
import os
import time
import yaml
import threading

class ConfigWatcher:
    def __init__(self, path, callback, interval=2.0):
        self.path = path
        self.callback = callback
        self.interval = interval
        self._last_mtime = 0
        self._running = False

    def start(self):
        self._running = True
        threading.Thread(target=self._loop, daemon=True).start()

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            try:
                mtime = os.path.getmtime(self.path)
                if mtime != self._last_mtime:
                    self._last_mtime = mtime
                    with open(self.path) as f:
                        cfg = yaml.safe_load(f)
                    self.callback(cfg)
            except Exception as e:
                print(f"Config reload failed: {e}")
            time.sleep(self.interval)

# 用法
def on_config_change(cfg):
    global v_max, Ld_min
    v_max = cfg["pure_pursuit"]["max_speed"]
    Ld_min = cfg["pure_pursuit"]["lookahead_min"]
    print(f"Config reloaded: v_max={v_max}, Ld_min={Ld_min}")

watcher = ConfigWatcher("config/params.yaml", on_config_change)
watcher.start()

# 之后改 params.yaml 文件，2 秒内自动生效
```

> 这个方案比 ROS2 Parameter 轻量得多，但要注意：修改 YAML 文件的时候不要有语法错误，否则 `yaml.safe_load` 会抛异常。用 `try-except` 包住，加载失败就用上一次的配置。
> 
> 

# 哪些参数值得抽出来

不是所有变量都要写进 YAML。判断标准：**赛场上会不会调这个值？**

|该抽出来的|不用抽的|
|---|---|
|前瞻距离、速度上限|帧头 0xAA|
|PID 增益|循环里的计数器|
|路径点坐标|数学常量（π）|
|红蓝区标志|内部状态变量|
|超时时间|数据结构字段|

> 原则：和物理世界打交道的参数抽出来，纯逻辑的东西不用抽。速度、距离、增益、超时这些是和底盘、场地、硬件绑定的，换一辆车就要改。帧头、校验方式这些是协议层面的，定了就不动。
> 
> 

# 调参的顺序

赛场上时间有限，不能瞎调。推荐的顺序：

```Plain Text
1. 先调前瞻距离 Ld
   → 蛇形走位？Ld 调大
   → 过弯切太多？Ld 调小
   → 这一个参数影响最大

2. 再调速度上限
   → 过弯打滑？降速
   → 直道太慢？提速
   → 和 Ld 配合调

3. 最后调控制参数（PID / 其他控制器的增益）
   → 这部分取决于你用什么控制器，具体怎么调看你自己的方案
```

> 不要一次改三个参数。改一个，跑一遍，看效果，再改下一个。同时改多个参数出了问题你不知道是哪个改坏了。
> 
> 

# 小结

参数管理就一件事：把会变的东西和不变的东西分开。会变的写配置文件，不变的，很少变的写代码里面。

用 ROS2 的话自带 Parameter 系统，`ros2 param set` 一行命令改参数。不用 ROS2 的话写个文件监听，改 YAML 自动重载。

赛场上每多编译一次就少跑一次。参数热加载不是锦上添花，是直接决定赛前能调多少轮。

# 第十章 赛场联调诊断与排错复盘

> 赛场上车出了问题，最怕的不是问题本身，是不知道问题出在哪。上位机说是电控的事，电控说是雷达的事，雷达说是上位机的算法有问题——互相甩锅半小时，时间全浪费了。这一章给一套快速定位的方法，出了问题先搞清楚是谁的责任，再想办法修。
> 
> 

# 症状→根因映射表

车在赛场上出问题了，先看症状，对着表查可能的原因。

## 蛇形走位 / 直线画龙

车走直线的时候左右小幅摆动，幅度越来越大或者一直抖。

**最可能的原因：定位数据有高频噪声。**

激光 SLAM 或里程计的输出每一帧都有几厘米的抖动，控制算法每帧都在修正这个抖动，越修越抖，形成正反馈。

**排查步骤：**

1. 打开 RViz（或者自己写个可视化），看定位轨迹是不是锯齿状

2. 如果是锯齿 → 定位噪声太大，加低通滤波

3. 如果轨迹平滑但车还是抖 → 控制器增益太大，降低 P 项

**另一个可能：EKF 没收敛。** 如果用了 EKF 融合多传感器，刚启动时 EKF 需要几秒钟收敛，这段时间定位是不准的。等几秒再启动任务。

## 走对数曲线 / 过弯过冲

车走弯道的时候不走圆弧，走出一条越来越弯的线，像对数函数图像。或者到了弯道该转弯了，转不过来，冲出赛道。

**最可能的原因：定位数据有高延时。**

你拿到的位姿是 100ms 前的，但控制算法用这个"旧"位姿算出来的角速度是针对 100ms 前的位置的。速度越快，100ms 的位移越大，过弯时就切弯或者冲出去。

**排查步骤：**

1. 在代码里打印定位数据的时间戳和当前系统时间，算差值

2. 如果延时 \> 50ms → 定位处理太慢，降分辨率或者换更快的算法

3. 如果延时正常但还是过冲 → 运动学参数不对（轮距、最大角速度），或者前瞻距离太小

**另一个可能：运动学参数错误。** 代码里写的轮距和实际轮距不一样，算出来的左右轮速比例是错的，车就会走出奇怪的弧线。

## 坐标瞬移 / 90° 甩尾

车走着走着突然跳了一截，或者朝向突然转了 90°。Pure Pursuit 看到位置突然变了，猛打方向，车直接甩尾。

**最可能的原因：重定位跟丢了。**

激光 SLAM 的 ICP/NDT 匹配失败，重新匹配成功后位置跳了一大截。在环境退化（长走廊、空旷区域、相似结构）时容易发生。

> 但是还有一个因素会导致各种奇奇怪怪的bug，就是你们的雷达过热，需要散热。就比如我们26赛季用的Odin1，因为雷达过热出现了原点偏移，导致比赛途中出现重大事故
> 
> 

**排查步骤：**

1. 看定位轨迹有没有突然的跳变

2. 如果有 → SLAM 匹配失败，检查地图质量、检查雷达有没有被遮挡

3. 如果没有跳变但车还是甩 → 检查是不是里程计编码器松了，轮子打滑导致里程计突变

**缓解措施：**

- 对定位输出做异常值检测，跳变超过阈值就丢弃

- 用轮式里程计做降级，定位跳变时切回里程计

- 控制器加输出限幅，角速度不能超过某个值

## 无中生有急停 / 空气墙

车走着走着突然停了，面前什么都没有。或者明明前面是空的，车就是不过去。

**最可能的原因：雷达点云有噪点。**

灰尘、阳光直射、反光表面都会在雷达点云里产生噪点。如果没做 ROI 裁剪，这些噪点会被当成障碍物，触发避障或者急停。

**排查步骤：**

1. 打开 RViz 看点云，找有没有离群点

2. 如果有 → 加 ROI 裁剪，只保留赛场范围内的点

3. 加点云滤波（统计滤波、半径滤波）去掉离群点

**另一个可能：雷达脏了或者被遮挡。** 比赛前检查一下雷达镜片有没有灰尘，线有没有松。

# 抓包与数据比对

出了问题不要猜，看数据。

## ROS2 Topic 日志

ROS2 自带命令行工具，可以实时查看每个 Topic 的数据：

```Bash
# 查看某个 Topic 的最新消息
ros2 topic echo /decision

# 查看 Topic 的发布频率
ros2 topic hz /odom

# 列出所有活跃的 Topic
ros2 topic list
```

> 车走蛇形的时候，先 `ros2 topic hz /odom` 看定位频率正不正常。频率正常说明定位没问题，是控制的问题；频率不对说明定位有延迟或者丢帧。
> 
> 

## 录包回放

ROS2 可以把所有 Topic 的数据录下来，事后回放分析：

```Bash
# 录包（所有 Topic）
ros2 bag record -a

# 录指定 Topic
ros2 bag record /odom /decision /command

# 回放
ros2 bag play <bag文件路径>
```

录包的好处是：赛场上出了问题，把包录下来，回实验室慢慢分析。不用在赛场上现调。

## 分离责任的思路

出了问题，先搞清楚是哪一层的：

```Plain Text
车走蛇形？
  → 看 /odom 的轨迹
    → 轨迹是锯齿 → 定位层的问题（噪声太大）
    → 轨迹平滑 → 控制层的问题（增益太大）

车不到目标点？
  → 看 /command 里的坐标
    → 坐标不对 → 决策层的问题（路径点标错了）
    → 坐标对了但车没到 → 控制层或感知层的问题

机械臂不动作？
  → 看 /command 里的 block/stair 字段
    → 字段值不对 → 决策层的问题
    → 字段值对了但没动 → 电控的问题（串口通信或硬件）
```

> 每一层只看它的输入和输出。输入对了输出不对，是这一层的问题。输入就不对，是上一层的问题。从上往下查，5 分钟内定位到问题出在哪。
> 
> 

# 技术资产沉淀

赛季结束了，代码和文档要留给下一届。

## 写文档，不写注释

代码里的注释是给写代码的人看的，文档是给接手的人看的。下一届的人不会逐行读你的代码，他们需要的是：

- **系统架构图：** 整个上位机有哪些模块，模块之间怎么通信

- **模块 API 文档：** 每个模块对外暴露什么接口，输入输出是什么

- **配置说明：** YAML 里每个参数是什么意思，改了会怎样

- **赛场排错指南：** 就是上面那张症状→根因映射表

```Markdown
# R2 上位机架构文档

## 模块列表
- serial_node (C++): 串口驱动，负责和电控通信
- decision_node (Python): 决策状态机，负责任务调度
- control_node (C++): 运动控制，负责 Pure Pursuit

## 通信接口
- /command (robot_serial/msg/Command): 决策 → 串口驱动
- /decision (robot_serial/msg/Ack): 串口驱动 → 决策
- /odom (nav_msgs/msg/Odometry): 定位 → 控制

## 配置参数
见 config/params.yaml 注释
```

## 仓库结构

```Plain Text
r2_upper/
├── README.md              # 项目说明、怎么跑起来
├── docs/
│   ├── architecture.md    # 架构文档
│   ├── troubleshooting.md # 排错指南
│   └── protocol.md        # 串口协议文档
├── config/
│   └── params.yaml        # 所有可调参数
├── src/
│   ├── r2_serial/         # 串口驱动
│   ├── r2_decision_py/    # 决策（Python）
│   └── r2_control/        # 运动控制
└── launch/
    └── r2_system.launch.py
```

> README 里要写清楚三件事：怎么把环境搭起来、怎么把代码跑起来、改了配置怎么生效。下一届的人拿到仓库，30 分钟内能跑起来，你的文档就合格了。
> 
> 

# 小结

赛场上出了问题，先看症状对着映射表查可能的原因，再用 Topic 日志和录包定位是哪一层的问题。不要猜，看数据。

赛季结束后把架构、接口、参数、排错经验写成文档留给下一届。代码会过时，但文档里的排错经验不会——蛇形走位是定位噪声、过弯过冲是延时太大、坐标跳变是重定位发散，这些因果关系十年后还是这样。

# 最后：写给视觉/感知/上位机组的各位

在RC圈子里面大伙讨论的大多数都是机械，结构，下位机等，能讨论上位机相关内容的属实寥寥无几，也可能是软件人的特点，比较原子化。不过，从我写好初版发pdf开始，陆陆续续有50\+人加我，其中不乏对我的初版稿子做出很高评价的哥们，希望有更多队伍的nb哥们可以更加social一点，rc不只有机械电控，也有上位机的一份力。

# 鸣谢名单

[MTFTau\-5](https://github.com/MTFTau-5)



