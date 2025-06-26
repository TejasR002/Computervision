import cv2
import numpy as np

img = np.zeros((512, 512, 3))

#Rectangle
cv2.rectangle(img, pt1 = (100,100),pt2=(300,300),color=(255,255,0),thickness=-1) # if want to fill the shape then put -1 in thickness
#Circle
cv2.circle(img, center = (255,255),radius =50,color=(255,0,0),thickness=-3)
#line
cv2.line(img, pt1 = (0,0),pt2=(512,512),color=(255,255,255),thickness=1)
cv2.line(img, pt1 = (512,0),pt2=(0,512),color=(255,255,255),thickness=1)
#text
cv2.putText(img, org=(100,100),text = "Goku", fontScale=2,color = (0,0,255), thickness=1,lineType = cv2.LINE_AA,fontFace=cv2.FONT_HERSHEY_SIMPLEX)
cv2.imshow('window', img)
cv2.waitKey(0)