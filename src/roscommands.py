#!/usr/bin/env python

import roslib; roslib.load_manifest('cloud_ros')
import rospy
from cloud_ros.srv import *
from pySpacebrew.spacebrew import Spacebrew
from std_msgs.msg import String
import rosgraph.masterapi
import time
import os
import subprocess
import threading
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def rosCommandsFunctions(command, brew):

	commandSplit = command.split(" ")
	if len(commandSplit) == 1:
		data = {'commandRos':'roscommands', 'function':'roscommands', 'action':'send', 'commands':commandSplit[0]}
		brew.publish("Publisher", data)
		rospy.logwarn("Command sent = "+command)
	elif (comandoSplit[1] == "set_robot"):
		data = {'commandRos':'roscommands', 'function':'set_robot', 'action':'send', 'commands':commandSplit[2]}
		brew.publish("Publisher", data)
		rospy.logwarn("Command sent = "+command)
	else:
		rospy.logwarn("Incorrect command syntax")	
	
'''INICIO ROSCOMMANDS'''
def set_robot(brew, commands):
	global robot 
	robot = commands

def roscommands(brew, commands):
	global robot
	rospy.logwarn(robot)

	vel = Twist()
	global proc

	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0

	if(commands == "up"): 
		vel.linear.x = 2
	elif(commands == "down"):
		vel.linear.x = -2
	elif(commands == "right"):
		vel.angular.z = -2
	elif(commands == "left"):
		vel.angular.z = 2

	robots = robot.split(":")

	for rob in robots:
		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)
		pub.publish(vel)

		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
	
		time.sleep(0.5)

		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)
		pub.publish(vel)

'''FIM ROSCOMMANDS'''


