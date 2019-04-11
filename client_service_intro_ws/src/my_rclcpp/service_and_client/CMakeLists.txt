cmake_minimum_required(VERSION 3.5)
project(my_rclcpp_service_and_client)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(merged_service_main service_main.cpp)
ament_target_dependencies(merged_service_main rclcpp example_interfaces)

add_executable(merged_client_main client_main.cpp)
ament_target_dependencies(merged_client_main rclcpp example_interfaces)

install(TARGETS merged_service_main merged_client_main
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
