#! /usr/bin/env python3

#SPDX-License-Identifer: GPL-2.0
#*Copyright (c) 2021 Ryoya Sato. All rights resrved.

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up',Int32,queue_size=1)
rate = rospy.Rate(10)
n = 1
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
