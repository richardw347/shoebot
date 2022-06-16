from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        # Realsense
        launch_ros.actions.Node(
            name='realsense2_camera',
            package='realsense2_camera', executable='realsense2_camera_node',
            output='screen',
            parameters=[
                {"publish_tf": False},
            ]
        )
    ])
