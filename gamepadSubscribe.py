#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from rpiHAT import ServoNT
import time

topic = 'controller'

def callback(data):
    # test no threading
    s=ServoNT(channel=1, freq=97.9)
   #s.pulse(0.1)
#    print(data.data)
    if data == "X":
       print(data.data)
       s.pulse(float(data.data))
#    s.pulse(0.1)
#    try:
#        while True:
#            time.sleep(0.5)
#    except (KeyboardInterrupt, SystemExit):
#        s.pulse(data.data)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('FastBoi', anonymous=True)
    rospy.Subscriber(topic, String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    print('waiting')
    rospy.spin()

if __name__ == '__main__':
    listener()
