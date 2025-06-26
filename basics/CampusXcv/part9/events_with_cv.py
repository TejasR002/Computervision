import cv2
import numpy as np

img = np.zeros((1080,1920, 3))


def draw(event,x,y,flags,params):
    print(event)
    if event == 1 : # for mouse single click
        cv2.circle(img, (x,y),radius = 30,color = (255,255,0), thickness = 1)
    if event == 7 :# for mouse double click 
        cv2.rectangle(img, pt1 = (x,y),pt2=(x+ 50,y + 50),color=(255,0,0),thickness=-1)
    if event == 4 : # for releasing the mouse
        print("mouse released")
    if event == 0: # for moving the mouse 
        cv2.putText(img, org=(x,y),text = f"mouse moved to cordinates {(x,y)}", fontScale=1,color = (0,0,255), thickness=1,lineType = cv2.LINE_AA,fontFace=cv2.FONT_HERSHEY_SIMPLEX)


cv2.namedWindow(winname = "window")
cv2.setMouseCallback('window',draw)
while True:
    cv2.imshow('window',img)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        print("\nclosing window\n")
        break   

cv2.destroyAllWindows()