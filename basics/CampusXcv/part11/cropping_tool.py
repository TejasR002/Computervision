import cv2
import numpy as np

img = cv2.imread("D:/cmputerVisionSimform/Images/istockphoto-2170331014-612x612.jpg")

Flag = False
ix = -1 
iy = -1

def crop(event,x,y,flags,params):
    
    global Flag,ix,iy

    if event == 1 :
        Flag = True
        ix = x
        iy = y 
    



    elif event == 4 :
        fx = x
        fy = y
        Flag = False
        
        cv2.rectangle(img,pt1 = (ix,iy),pt2 = (fx,fy),thickness = 2, color = (0,25,255))
        croped_img = img[iy:fy,ix:fx]
        cv2.imwrite( "cropedimg.png",croped_img)
        cv2.imshow("cropped",croped_img)




cv2.namedWindow(winname = "window")
cv2.setMouseCallback('window',crop)

while True:
    cv2.imshow("window",img)

    if cv2.waitKey(1)  &  0xFF == ord("x"):
        break

cv2.destroyAllWindows()
