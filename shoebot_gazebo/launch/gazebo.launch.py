import os
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
)
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = True

    joy_launch_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_bringup"), "launch", "joy_teleop.launch.py"]
    )

    world_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_gazebo"), "worlds", "home.world"]
    )

    description_launch_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_description"), "launch", "description.launch.py"]
    )

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=[
                    "gazebo",
                    "--verbose",
                    "-s",
                    "libgazebo_ros_factory.so",
                    "-s",
                    "libgazebo_ros_init.so",
                    world_path,
                ],
                output="screen",
            ),
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py",
                name="urdf_spawner",
                output="screen",
                arguments=["-topic", "robot_description", "-entity", "shoebot"],
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(description_launch_path),
                launch_arguments={
                    "use_sim_time": str(use_sim_time),
                    "publish_joints": "false",
                }.items(),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(joy_launch_path),
            ),
        ]
    )
