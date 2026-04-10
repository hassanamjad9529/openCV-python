import cv2
import numpy as np
from numpy.ma.core import masked


def empty(a):
    pass

img = cv2.imread("Resources/whatsapp.jpeg")
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 81, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 111, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 71, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 102, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 170, 255, empty)

while True:
    img1 = cv2.imread("Resources/whatsapp.jpeg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img1, mask= mask)


    cv2.imshow("real", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image result", imgResult)
    cv2.  waitKey(1 )