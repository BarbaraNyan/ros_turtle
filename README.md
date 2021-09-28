# ros_turtle
This code allows /turtle1 to follow /turtle2
P.S. /turtle1 is controlled by turtle_teleop_key

# Steps:
1. rosrun turtlesim turtlesim_node
2. rosservice call /spawn "x: 0.0
  y: 0.0
  theta: 0.0
  name: 'turtle2'"
3. rosrun my_pkg follow_turtle.py
4. rosrun turtlesim turtle_teleop_key
