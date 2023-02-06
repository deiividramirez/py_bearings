#!/usr/bin/env python3
import rospy
import rostopic

from std_msgs.msg import Float64

class PyBearings:
    def __init__(self):
        self.bearing_sub = rospy.Subscriber('/bearing', Float64, self.bearing_callback)
        self.bearing_pub = rospy.Publisher('/bearing', Float64, queue_size=10)

        while not rospy.is_shutdown():
            rospy.loginfo("Waiting for bearing topic...")
            if rostopic.get_topic_class('/bearing')[0] == Float64:
                rospy.loginfo("Found bearing topic!")
                #break
            rospy.Rate(90).sleep()

    def bearing_callback(self, msg):
        rospy.loginfo("Bearing: {}".format(msg.data))
        self.bearing_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('py_bearings', anonymous=True)
    py_bearings = PyBearings()
    rospy.spin()
