#!/usr/bin/env python3

from pathlib import Path
WORKSPACE = Path(__file__).parent.absolute()
print(f"WORKSPACE: {WORKSPACE}")

import sys
import rospy
import roslib
import rostopic

from std_msgs.msg import Float64
from sensor_msgs.msg import Image
from src import saveDesires

import cv2
from cv_bridge import CvBridge

class PyBearings:
    def __init__(self):
        rospy.init_node('py_bearings', anonymous=True)
        
        # Node handle for charging yaml file
        nh = [rospy.get_param(f"ns{i}") for i in range(1,5)]
        gen = rospy.get_param("general")
        
        SAVE_DESIRED_IMAGES = gen["SAVE_DESIRED_IMAGES"]
        SAVE_IMAGES = gen["SAVE_IMAGES"]
        SHOW_IMAGES = gen["SHOW_IMAGES"]

        seg1 = gen["seguimiento_1"]
        seg2 = gen["seguimiento_2"]
        seg3 = gen["seguimiento_3"]
        seg4 = gen["seguimiento_4"]

        print(f"\n[INFO] SAVE_DESIRED_IMAGES: {'True' if SAVE_DESIRED_IMAGES else 'False'}")

        if SAVE_DESIRED_IMAGES:
            subs_front = [rospy.Subscriber(f"/iris_{i}/camera_front_camera/image_raw", Image, saveDesires.saveFront, callback_args=(i,)) for i in range(1,5)]
            subs_under = [rospy.Subscriber(f"/iris_{i}/camera_under_camera/image_raw", Image, saveDesires.saveUnder, callback_args=(i,)) for i in range(1,5)]
        else:
            pass

        print(f"PASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1")
        RATE = rospy.Rate(30)
        contGEN = 0

        if not SAVE_DESIRED_IMAGES:
            pass

        if not SAVE_DESIRED_IMAGES:
            pass


        print(f"PASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA2")
        while not rospy.is_shutdown():
            contGEN += 1
            if contGEN > 50 and SAVE_DESIRED_IMAGES:
                print(f"[INFO] Desired images saved")
                rospy.on_shutdown(self.shutdown)
                break
            else:
                print("DUERMIENDO")
                RATE.sleep()

            rospy.spin()
        print(f"FUNCA")
        print('\n')
        exit()

        self.bearing_sub = rospy.Subscriber('/bearing', Float64, self.bearing_callback)
        self.bearing_pub = rospy.Publisher('/bearing', Float64, queue_size=10)

        while not rospy.is_shutdown():
            rospy.loginfo("Waiting for bearing topic...")
            if rostopic.get_topic_class('/bearing')[0] == Float64:
                rospy.loginfo("Found bearing topic!")
                #break
            rospy.Rate(90).sleep()

    def shutdown(self):
        rospy.loginfo("Shutting down py_bearings node...")
        rospy.signal_shutdown("Shutting down py_bearings node...")
        print(f"{rospy.is_shutdown()}")

    def bearing_callback(self, msg):
        rospy.loginfo("Bearing: {}".format(msg.data))
        self.bearing_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('py_bearings', anonymous=True)
    py_bearings = PyBearings()
    rospy.spin()
