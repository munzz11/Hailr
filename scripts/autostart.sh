#!/bin/bash


sleep 5

source /opt/ros/noetic/setup.bash
source /home/field/project11/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://mdt:11311
export ROS_IP=172.30.0.180



/usr/bin/tmux new -d -s hailr
/usr/bin/tmux send-keys -t hailr "rosrun rosmon rosmon --name=hailr hailr vessel.launch" C-m
