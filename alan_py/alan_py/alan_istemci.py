import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanIstemci(Node):
    def __init__(self):
        super().__init__('alan_istemci')
        self.client = self.create_client(RectangleArea, 'rectangle_area')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')

    def istek_gonder(self, width, height):
        req = RectangleArea.Request()
        req.width = width
        req.height = height
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    if len(sys.argv) < 3:
        print('Kullanim: ros2 run alan_py alan_istemci <width> <height>')
        sys.exit(1)

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    except ValueError:
        print('Hata: width ve height sayisal deger olmalidir.')
        sys.exit(1)

    rclpy.init(args=args)
    node = AlanIstemci()

    try:
        response = node.istek_gonder(width, height)
        if response.success:
            node.get_logger().info(
                f'Sonuc: {width} x {height} = {response.area} (success=True)'
            )
        else:
            node.get_logger().warn(
                f'Istek reddedildi: negatif deger girilemez (width={width}, height={height}, success=False)'
            )
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
