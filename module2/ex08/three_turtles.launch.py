import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim1'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim2'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim3'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            remappings=[
                ('/input/pose', '/turtle1/pose'),
                ('/output/cmd_vel', '/turtle2/cmd_vel'),
            ]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            remappings=[
                ('/input/pose', '/turtle2/pose'),
                ('/output/cmd_vel', '/turtle3/cmd_vel'),
            ]
        ),
    ])
