#!/usr/bin/env python

import roslib; roslib.load_manifest('cloud_ros')
import rospy
from cloud_ros.srv import *
from pySpacebrew.spacebrew import Spacebrew
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import rosgraph.masterapi
import time
import os
import subprocess

import importlib

def rosSensors(brew):
	global brew_

	brew_ = brew
	rospy.Subscriber("chatter", String, callback)

def callback(req):
	data = {'comandoRos':'sensor', 'funcao':'walk', 'acao':'enviar', 'dados':req.data}
	brew_.publish("Publisher", data)
	
def walk(brew, data):
	if(data['dados']>0.1):
		vel = Twist()

		vel.linear.x = 2
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0

		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)

		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
	
		time.sleep(0.5)

		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)
