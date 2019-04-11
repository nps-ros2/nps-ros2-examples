from example_interfaces.srv import AddTwoInts
import rclpy

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('my_client_async')

    cli = node.create_client(AddTwoInts, 'add_two_ints')

    req = AddTwoInts.Request()
    req.a = 41
    req.b = 1
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            if future.result() is not None:
                node.get_logger().info(
                    'py Result of add_two_ints: for %d + %d = %d' %
                    (req.a, req.b, future.result().sum))
            else:
                node.get_logger().info('Service call failed %r' % (future.exception(),))
            break

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
