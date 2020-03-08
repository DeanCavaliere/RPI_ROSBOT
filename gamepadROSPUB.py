#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
#http://wiki.ros.org/mallasrikanth/joystick%20control
#
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim or any other robot

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    twist.linear.x = data.axes[7]
    twist.angular.z = data.axes[6]

    twist.linear.x = data.axes[1] #Left Veritcal Stick
    twist.angular.z = data.axes[0] #Left Horizontal Stick
    #twist.linear.x = data.axes[4] #Right Vertical Stick
    #twist.angular.z = data.axes[3] #Right Horizontal Stick
    pub.publish(twist)
    print(str(Twist))

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('controller', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('joy2robot')
    rospy.spin()

if __name__ == '__main__':
    start()