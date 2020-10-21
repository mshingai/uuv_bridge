# -*- coding: utf-8 -*-
#!/usr/bin/env python                                                            
import rospy
from std_msgs.msg import Float64
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped

# Subscriber用のコールバックを生成するクロージャー
def actuator_callback(inTopic, publisher):
    pub = publisher

    def callback(data):
        # rospy.loginfo(rospy.get_caller_id() + " I heard %f", data.data)

        pubdata = FloatStamped()
        pubdata.header.stamp = rospy.Time.now()
        pubdata.data = data.data
        
        pub.publish(pubdata)
    return callback

def converter(list):
    rospy.init_node('rosbridge_node', anonymous=True)

    # 変換リストからPublisher，SubScriberを設定
    for item in list:
        callback = actuator_callback(item[0], rospy.Publisher(item[1], FloatStamped, queue_size=10))
        rospy.Subscriber(item[0], Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    convert_list = [
        # 変換元をSubscribeし，データをそのまま変換先へPublishする
        # 変換元，　　　　　　　　　　　　変換先
        ('/lauv/fins/fin0/input', '/lauv/fins/0/input'),
        ('/lauv/fins/fin1/input', '/lauv/fins/1/input'),
        ('/lauv/fins/fin2/input', '/lauv/fins/2/input'),
        ('/lauv/fins/fin3/input', '/lauv/fins/3/input'),
        ('/lauv/thrusters/thruster0/input', '/lauv/thrusters/0/input'),
    ]
    converter(convert_list)