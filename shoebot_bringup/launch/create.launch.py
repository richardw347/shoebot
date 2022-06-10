import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    create_config_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_bringup"), "config", "create_driver.yaml"]
    )

    return LaunchDescription([
        Node(
            package='create_driver',
            executable='create_driver',
            name='create_driver',
            output='screen',
            parameters=[create_config_path]
        )
    ])