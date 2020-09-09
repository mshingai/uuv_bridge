#!/usr/bin/env python                                                            
import rospy
from std_msgs.msg import Float64
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped

def actuator_callback(inTopic, publisher):
    pub = publisher

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + " I heard %f", data.data)

        pubdata = FloatStamped()
        pubdata.header.stamp = rospy.Time.now()
        pubdata.data = data.data
        
        pub.publish(pubdata)
    return callback

def converter(list):
    rospy.init_node('rosbridge_node', anonymous=True)


    for item in list:
        callback = actuator_callback(item[0], rospy.Publisher(item[1], FloatStamped, queue_size=10))
        rospy.Subscriber(item[0], Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    convert_list = [
        ('/lauv/fins/fin0/input', '/lauv/fins/0/input'),
        ('/lauv/fins/fin1/input', '/lauv/fins/0/input'),
    ]
    converter(convert_list)