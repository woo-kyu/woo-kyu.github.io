---
layout: single
title: Lidar Setup
toc_label: Lidar Setup
categories: Lidar
tags: [Lidar, Sensor_Data_Process]
author_profile: false
search: true
use_tex: true
---

> Lidar System 사용 환경 설정

# 사용 환경
- Lidar: RPLIDAR A2M12
- Edge Computer: Nvidia Jetson Xavier (aarch64)
- System OS: Linux (Ubuntu 20.04)
- Jetson Setting
  - Jetpack 5.1
  - CUDA 11.4
  - TensorRT 8.5.2.2
  - OpenCV: 4.5.5
  - Python 3.8.10

<br>

# Lidar Official Library

- [git](https://github.com/Slamtec/rplidar_ros)

<br>

# For ROS (Robot Operating System) 

### Catkin Workspace 생성

> Catkin 워크스페이스란?
> Catkin: ROS의 빌드 시스템입니다. Catkin을 사용하여 ROS 패키지를 빌드하고 관리합니다.
> 워크스페이스: ROS 패키지들을 개발, 빌드, 실행하기 위한 폴더 구조입니다. 일반적으로 사용자는 자신의 프로젝트에 맞게 하나 이상의 워크스페이스를 생성합니다.

```c
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
```

<br>

### Git repository clone
```c
cd ~/catkin_ws/src
git clone https://github.com/Slamtec/rplidar_ros.git
```

<br>

### ros Noetic 설치

- 시스템 업데이트 및 필요한 소프트웨서 설치
```c 
sudo apt update
sudo apt install curl gnupg2 lsb-release
```

- Ros repository 설정
```c 
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

- Ros Noetic 설치
```c 
sudo apt update
sudo apt install ros-noetic-desktop-full
```

- Setup
```c 
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

- Rosdep install
```c 
sudo apt install python3-rosdep2
sudo rosdep init
rosdep update
rosdep install roscpp rosconsole
```