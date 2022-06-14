from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition


def generate_launch_description():
    
    urdf_path = PathJoinSubstitution(
        [FindPackageShare("shoebot_description"), "urdf", "shoebot.urdf.xacro"]
    )
        
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
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'robot_description': Command(['xacro ', urdf_path])
                }
            ]
        )
    ])