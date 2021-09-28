#! /usr/bin/python

import rospy
import time
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class my_class:
	def __init__(self):
		self.r = rospy.Rate(0.33)
		self.x_turtle1 = 0
		self.y_turtle1 = 0
		self.x_turtle2 = 0
		self.y_turtle2 = 0

		self.velocity_x = 0
		self.velocity_y = 0
		self.angle_prev = 0

		self.pub1 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size = 1)
		
		self.sub2 = rospy.Subscriber('/turtle2/pose', Pose, self.listener_turtle2)
		self.sub3 = rospy.Subscriber('/turtle1/pose', Pose, self.listener_turtle1)	
    		self.sub1 = rospy.Subscriber('/turtle1/cmd_vel', Twist, self.follow_func)

	def follow_func(self, msg):
		new_msg = Twist()

		self.velocity_x = self.x_turtle1-self.x_turtle2 
		self.velocity_y = self.y_turtle1-self.y_turtle2 

		angle = math.atan2(self.velocity_y, self.velocity_x)
		magnitude = math.sqrt(pow(self.velocity_x,2)+pow(self.velocity_y,2))

		new_msg.angular.z = angle - self.angle_prev
		new_msg.linear.x = 0
		self.angle_prev = angle
		self.pub1.publish(new_msg)
		self.r.sleep()

		new_msg.angular.z = 0
		new_msg.linear.x = magnitude * 0.5
		self.pub1.publish(new_msg)
		self.r.sleep()

	def listener_turtle1(self, msg):
		self.x_turtle1 = msg.x
		self.y_turtle1 = msg.y
		
	def listener_turtle2(self, msg):
		self.x_turtle2 = msg.x
		self.y_turtle2 = msg.y
		
rospy.init_node('follow_node')

m = my_class()

rospy.spin()
