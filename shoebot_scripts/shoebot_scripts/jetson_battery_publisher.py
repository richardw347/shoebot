import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import struct
import smbus

ADDRESS = 0x36

class BatteryPublisher(Node):

    def __init__(self):
        super().__init__('battery_publisher')
        # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
        self._bus = smbus.SMBus(1) 
        self.publisher_ = self.create_publisher(Float32, 'jetson/battery_percentage', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self._timer_callback)

    def _timer_callback(self):
        msg = Float32()
        msg.data = self._read_capacity()
        self.publisher_.publish(msg)
        self.get_logger().info(f"Battery Capacity: {msg.data}%")
        
    def _read_voltage(self):
        read = self._bus.read_word_data(ADDRESS, 2)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = swapped * 1.25 /1000/16
        return voltage

    def _read_capacity(self):
        read = self._bus.read_word_data(ADDRESS, 4)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        capacity = swapped/256
        return capacity

def main(args=None):
    rclpy.init(args=args)
    battery_publisher = BatteryPublisher()
    rclpy.spin(battery_publisher)
    battery_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()