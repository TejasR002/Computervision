# converting from rgb to grayscale
import cv2
import numpy as np

image = cv2.imread("D:/cmputerVisionSimform/Images/bus.jpg")


image_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("bus",image_gray)

cv2.waitKey(0)
