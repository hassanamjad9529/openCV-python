import cv2
import numpy as np

img = cv2.imread("Resources/whatsapp.jpeg")
print(img.shape)
imgResize = cv2.resize(img, (300,900))
print(imgResize.shape)

imgCropped = img[0:200]


cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)