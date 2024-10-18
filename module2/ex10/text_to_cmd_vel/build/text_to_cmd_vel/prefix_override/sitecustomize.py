import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/drmbx/study/robotics/ros2_ws/src/text_to_cmd_vel/install/text_to_cmd_vel'
