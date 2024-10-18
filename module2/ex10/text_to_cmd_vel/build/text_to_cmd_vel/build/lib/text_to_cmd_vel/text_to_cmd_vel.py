from math import pi

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.subscription_ = self.create_subscription(
            String,
            'text_to_cmd_vel',
            self.callback,
            10)
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10)

    def callback(self, msg_string):
        msg_twist = Twist()
        print(msg_string)
        print(msg_string.data)
        match msg_string.data:
            case 'turn_right':
                msg_twist.angular.z = -pi
                self.publisher_.publish(msg_twist)
            case 'turn_left':
                msg_twist.angular.z = pi
                self.publisher_.publish(msg_twist)
            case 'move_forward':
                msg_twist.linear.x = 1
                self.publisher_.publish(msg_twist)
            case 'move_backward':
                msg_twist.linear.x = -1
                self.publisher_.publish(msg_twist)

def main(args=None):
    rclpy.init(args=args)
    text_to_cmd_vel = TextToCmdVel()
    rclpy.spin(text_to_cmd_vel)

    text_to_cmd_vel.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()