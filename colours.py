#!/usr/bin/env python

import rospy
#from cv2 import namedWindow, cvtColor, imshow
#from cv2 import destroyAllWindows, startWindowThread
#from cv2 import COLOR_BGR2GRAY, waitKey
#from cv2 import blur, Canny
#from cv2 import inRange
import cv2
from cv2 import startWindowThread, namedWindow, imshow, waitKey
import numpy
from numpy import mean
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class image_converter:

    def __init__(self):

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",
                                          Image, self.callback)
        # self.image_sub = rospy.Subscriber(
        #     "/camera/rgb/image_raw",
        #     Image, self.callback)

    def callback(self, data):
        namedWindow("Image window")
        namedWindow("Threshold")
        #namedWindow("blur")
        #namedWindow("canny")
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_grey = numpy.array([10, 10, 10])
        upper_grey = numpy.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower_grey, upper_grey)
        cv2.bitwise_and(cv_image, cv_image, mask=mask)
        imshow("Threshold", mask)

        #gray_img = cvtColor(cv_image, COLOR_BGR2GRAY)
        #print mean(gray_img)
        #img2 = blur(gray_img, (3, 3))
        #imshow("blur", img2)
        #img3 = Canny(gray_img, 10, 200)
        #imshow("canny", img3)

        imshow("Image window", cv_image)
        waitKey(1)

startWindowThread()
rospy.init_node('image_converter')
ic = image_converter()
rospy.spin()

destroyAllWindows()