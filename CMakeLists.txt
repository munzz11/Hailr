cmake_minimum_required(VERSION 3.0.2)
project(hailr)

find_package(catkin REQUIRED COMPONENTS
	  rosbridge_server
	  )

    catkin_package(
	      CATKIN_DEPENDS rosbridge_server
	      )

