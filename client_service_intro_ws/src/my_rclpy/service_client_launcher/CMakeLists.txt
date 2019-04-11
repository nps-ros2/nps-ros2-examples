cmake_minimum_required(VERSION 3.5)
project(my_rclpy_service_and_client_launcher)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
