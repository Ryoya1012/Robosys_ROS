#SPDX-License-Identifer: GPL-3.0
#*Copyright (c) 2021 Ryoya Sato. All rights resrved.

#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 1

def cb(message):
    global n
    n = message.data*4

if __name__ == '__main__':
    rospy.init_node('quadruple')
    sub = rospy.Subscriber('third', Int32, cb)
    pub = rospy.Publisher('quadruple', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
