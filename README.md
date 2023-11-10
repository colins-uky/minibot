# Minibot

Minibot is a ROS2 package that uses the ROS2 NAV2 stack and slam_toolbox to perform Simultaneous Localization and Mapping. This package was created in coordination by members of the Kentucky Organization of Robotics and Automation (KORA).

## Contents

1. [Overview](#overview)
2. [Materials](#materials)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Launch Minibot](#launch-minibot)
6. [Credits](#credits)



## Overview

Minibot uses pre compiled package ROS nodes to publish data from the sensors onboard the bot. Users can interact with Minibot by sending a `home` and `target` pose. The Minibot will initialize its own `home` position by default (as the pose Minibot is in when powered on). Once a `target` has been provided, Minibot will use SLAM to find an efficient route from `home` to `target`.


If no `target` pose is provided for `2` minutes, Minibot will (do something interesting idk blink, play noise, etc)

## Materials

We will be using the following materials for this minibot:




## Prerequisites


### 1. Install Ubuntu 20.04

This package requires ROS2 Foxy Fitzroy, which can only be installed on **Ubuntu 20.04 (Focal Fossa)**.


#### For x86_64:

* An installation guide provided by Ubuntu can be found [here](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

#### For Nvidia Jetson Nano (ARM):



* A precompiled Ubuntu 20.04 image for the Nvidia Jetson Nano can be found [here](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image).
    * (We will be using the barebones version)
    * Note: Normally Nvidia does not support Ubuntu versions past 18.04 (Bionic Beaver) for the Jetson Nano, but up to 20.04 has been used with success.


### 2. Install ROS2 Foxy Fitzroy

An installation guide for ROS2 Foxy Fitzroy can be found [here](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)

## Installation

### 1. Clone the Repo
Clone the repository package to your ROS2 workspace /src/ directory.

```bash
cd ~/Desktop/ros2_ws/src/
git clone https://github.com/colins-uky/minibot.git
```

### 2. Install Dependencies

Minibot borrows a few ROS2 nodes from other packages for publishing raw sensor data. Many of these packages are built by the creators of the sensors themselves.

#### rplidar_ros

```bash
sudo apt install blahblahblah
```

## Launch Minibot

Run the following command the verify the package was installed correctly:

```bash
source ./install/setup.bash
ros2 run minibot brb 
```



## Credits

- [Colin S.](https://github.com/colins-uky)
    * Package Creator