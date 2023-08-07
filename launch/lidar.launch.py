import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='urg_node',
            executable='urg_node_driver',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyACM0',
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
               
 
            }]
        )
    ])

