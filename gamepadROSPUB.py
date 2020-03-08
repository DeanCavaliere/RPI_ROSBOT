#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
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
    twist.linear.x = data.axes[1] #Left Veritcal Stick
    twist.angular.z = data.axes[0] #Left Horizontal Stick
    #twist.linear.x = data.axes[4] #Right Vertical Stick
    #twist.angular.z = data.axes[3] #Right Horizontal Stick
    pub.publish(twist)
    #print(str(Twist))
    # FORWARD/BACK =  1/-1.
    if Float32(twist.linear.x) < (-0.2):
        print('Backwards: '+ Float32(twist.linear.x))
    elif twist.linear.x > (0.2):
        print('Forwards: ' + Float32(twist.linear.x))
    else:
        print('Stop: ' + Float32(twist.linear.x))
    # LEFT/RIGHT = 1/-1
    if Float32(twist.angular.z) < (-0.2):
        print('Right: '+ Float32(twist.angular.z))
    elif twist.linear.x > (0.2):
        print('Left: ' + Float32(twist.angular.z))
    else:
        print('Straight: ' + Float32(twist.angular.z))

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