import cv2
import numpy as np


image = cv2.imread("D:/cmputerVisionSimform/Images/bus.jpg")


resized = cv2.resize(image, (320,320))



#fliped upside down
fliped_images = [resized]


cordinates = [0 , 1 , -1]
for i in cordinates:
    fliped_images.append(cv2.flip(resized, i))

tupe = tuple(fliped_images)
flipped = np.hstack(tupe)
cv2.imshow("pellets", flipped)
cv2.waitKey(0)

