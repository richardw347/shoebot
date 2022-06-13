from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition


def generate_launch_description():
    joy_launch_path = PathJoinSubstitution(
        [FindPackageShare('shoebot_bringup'), 'launch', 'joy_teleop.launch.py']
    )

    create_launch_path = PathJoinSubstitution(
        [FindPackageShare('shoebot_bringup'), 'launch', 'create.launch.py']
    )

    laser_launch_path = PathJoinSubstitution(
        [FindPackageShare('shoebot_bringup'), 'launch', 'urg_node.launch.py']
    )

    realsense_launch_path = PathJoinSubstitution(
        [FindPackageShare('shoebot_bringup'), 'launch', 'realsense.launch.py']
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(joy_launch_path)
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(create_launch_path),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(laser_launch_path),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(realsense_launch_path),
        ),
    ])