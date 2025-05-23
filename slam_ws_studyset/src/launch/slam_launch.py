import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 获取包路径
    pkg_path = get_package_share_directory('learning_gazebo')
    
    # 加载已有的激光小车Gazebo启动文件
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(pkg_path, 'launch', 'load_mbot_laser_into_gazebo.launch.py')
        ])
    )
    
    # SLAM工具箱节点
    slam_toolbox_node = Node(
        parameters=[
            os.path.join(pkg_path, 'config', 'mapper_params_online_async.yaml'),
            {'use_sim_time': True}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen'
    )
    
    # RViz2节点 - 使用你已有的配置添加地图显示
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'slam_config.rviz')],
        parameters=[{'use_sim_time': True}]
    )
    
    return LaunchDescription([
        gazebo_launch,
        slam_toolbox_node,
        rviz_node
    ])