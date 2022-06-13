from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition, LaunchConfigurationEquals
from launch_ros.actions import Node


def generate_launch_description():
    urg_config_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_bringup"), "config", "urg_driver.yaml"]
    )

    return LaunchDescription([
        Node(
            package='urg_node',
            executable='urg_node_driver',
            name='urg_node',
            output='screen',
            parameters=[urg_config_path]
        )
    ])

