import cv2
import numpy as np


#converting from RGB to grayscale image
image = cv2.imread("D:/cmputerVisionSimform/Images/Screenshot 2025-06-26 162615.jpg")

# resized_image = cv2.resize(image,(350,350)) # <- using descrete size
# cv2.imshow("resized_bus",resized_image)
# cv2.waitKey(0)


print(image.shape[1])
resized_image50 = cv2.resize(image,(int(image.shape[1])//2,int(image.shape[0])//2)) # <- 50% redueced size
cv2.imshow("resized_bus",resized_image50)
cv2.waitKey(0)