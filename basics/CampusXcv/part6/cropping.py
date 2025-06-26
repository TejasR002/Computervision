import cv2
import numpy as np


image = cv2.imread("D:/cmputerVisionSimform/Images/bus.jpg")

#                           hight , width
#                       start:end , start: end 
#                    top : bottom , left: right
image_crop =          image[0:500 ,  0:380]

cv2.imshow("cropped", image_crop)
cv2.waitKey(0)