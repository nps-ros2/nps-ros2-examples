# Adapted from https://github.com/ros2/demos/blob/master/demo_nodes_cpp/launch/services/add_two_ints.launch.py

"""Launch a add_two_ints_server and a (synchronous) add_two_ints_client."""

import launch
import launch_ros.actions


def generate_launch_description():
    server = launch_ros.actions.Node(
        package='my_rclcpp_service_and_client', node_executable='merged_service_main', output='screen')
    client = launch_ros.actions.Node(
        package='my_rclcpp_service_and_client', node_executable='merged_client_main', output='screen')
    return launch.LaunchDescription([
        server,
        client,
        # TODO(wjwwood): replace this with a `required=True|False` option on ExecuteProcess().
        # Shutdown launch when client exits.
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=client,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )),
    ])
