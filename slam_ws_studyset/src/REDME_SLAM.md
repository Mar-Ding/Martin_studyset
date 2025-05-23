# REDME_SLAM

+++

#### pre:

###### 本内容基于古月居的教程，是我的作业内容，在github上提交作业的文件无其他用途；本作业的world(被建图的地图),带有激光雷达的小车（.xacro文件）是直接取用了教程的文件。

+++

### 功能：

在Gazebo仿真中用一个带有激光雷达的小车实现Slam的建图功能；

+++

### 复现步骤：

1.下载本文件后保留这个文件结构：

 	slam_ws-|

​		--src

2.打开终端在slam_ws的文件中输入：

```bash
colcon build
```

实现编译;

```bash
source install/setup.bash
```

配置环境路径；

```bash
ros2 launch learning_gazebo slam_launch.py
```

运行后会打开rviz界面;

3.跑小车实现建图：

打开一个新的终端:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

运行操作节点实现建图;





