import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanSunucu(Node):
    def __init__(self):
        super().__init__('alan_sunucu')
        self.srv = self.create_service(
            RectangleArea,
            'rectangle_area',
            self.hesapla_callback
        )
        self.get_logger().info('RectangleArea servisi hazir, istek bekleniyor...')

    def hesapla_callback(self, request, response):
        # Negatif kenar uzunluklarini reddet (bonus)
        if request.width < 0.0 or request.height < 0.0:
            response.area = 0.0
            response.success = False
            self.get_logger().warn(
                f'Gecersiz istek (negatif deger): width={request.width}, height={request.height}'
            )
            return response

        response.area = request.width * request.height
        response.success = True
        self.get_logger().info(
            f'Istek: width={request.width}, height={request.height} -> area={response.area}'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AlanSunucu()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
