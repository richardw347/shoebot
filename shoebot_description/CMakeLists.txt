cmake_minimum_required(VERSION 3.5)
project(shoebot_description)

find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)

install(
  DIRECTORY meshes launch urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
