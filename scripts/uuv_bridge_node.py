#!/usr/bin/env python                                                            
import rospy
from std_msgs.msg import Float64
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Iheard %f", data.data)
    pub = rospy.Publisher('lauv/fins/0/input', FloatStamped, queue_size=10)
    header = rospy.Time.now()
    pubdata = FloatStamped()
    pubdata.header.stamp = header
    pubdata.data = data.data
    rospy.loginfo("header = %s, data = %f", header, pubdata.data)
    pub.publish(pubdata)

def listener():
    rospy.init_node('rosbridge_node', anonymous=True)
    rospy.Subscriber("lauv/fins/fin0/input", Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()