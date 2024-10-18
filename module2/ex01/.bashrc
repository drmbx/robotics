#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Set ROS2 Humble
source /opt/ros/humble/setup.bash
source ~/study/robotics/ros2_ws/install/local_setup.bash
