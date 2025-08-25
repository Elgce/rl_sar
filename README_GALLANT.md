# Gallant Gazebo Sim2sim Implementation
This repo is derived from `RL_SAR` and for `IsaacSim` to `Gazebo` verification. For more details of installation and other kind of usage, please turn to `README.md`.
## Installation
### Setup
* Ubuntu 22.04
* ROS2 humble (recommended desktop version)
* cuda 12.04
* cudnn 9.12.0
* onnxruntime-linux-x64-gpu-1.22.0
## Compilation
```
./build.sh
```
## Usage
Remember to close all conda envs
* Terminal 1 (publish topic */desired_goal_pose*)
```
source install/setup.bash
ros2 launch rl_sar rviz.launch.py
```
* Terminal 2
```
source install/setup.bash
ros2 launch rl_sar gazebo.launch.py rname:=g1
```
* Terminal 3
```
source install/setup.bash
ros2 run rl_sar rl_sim
0 # setup the env
1 # start to use onnx policy to control robot
```

### onnxruntime
reference [为推理构建 ONNX Runtime](https://runtime.onnx.org.cn/docs/build/inferencing.html)
start container and exec in container

0. add gazebo-11 model environment
    ```base
    vim ~/.bashrc
    export GAZEBO_MODEL_PATH=/usr/share/gazebo-11/models
    ```

1. CMake3.28 
    ```bash
    cd libiaries/
    wegt https://cmake.org/files/v3.28/cmake-3.28.1-linux-x86_64.tar.gz
    tar xf cmake-3.28.1-linux-x86_64.tar.gz
    ln -sf /home/zwt/docker/humble/libraries/cmake-3.28.1-linux-x86_64/bin/* /usr/bin/
    # show 3.28.1
    cmake --version
    ```

2. onnxruntime
    ```bash
    cd libiaries/
    git clone --recursive https://github.com/Microsoft/onnxruntime.git
    cd onnxruntime
    ./build.sh --config RelWithDebInfo --build_shared_lib --parallel --compile_no_warning_as_error --skip_submodule_sync
    # you may get error relate to root or other similar staff. just add `--allow xxxx` to aproval
    cmake --install ./build/Linux/RelWithDebInfo/
    ```