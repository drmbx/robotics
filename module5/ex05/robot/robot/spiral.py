#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpiralMovementNode(Node):
    def __init__(self):
        super().__init__('spiral_movement_node')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        
        # Начальные параметры движения
        self.linear_speed = 0.5  # постоянная линейная скорость
        self.angular_speed = 1.0  # начальная угловая скорость
        self.speed_reduction_factor = 0.99  # фактор уменьшения угловой скорости для создания спирали

        # Устанавливаем таймер для периодической отправки команд движения
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = self.linear_speed  # поддерживаем постоянную линейную скорость
        twist_msg.angular.z = self.angular_speed  # уменьшаем угловую скорость постепенно

        # Публикуем команду движения
        self.publisher_.publish(twist_msg)

        # Уменьшаем угловую скорость для расширения радиуса спирали
        self.angular_speed *= self.speed_reduction_factor

def main(args=None):
    rclpy.init(args=args)
    node = SpiralMovementNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

