import cv2
import numpy as np

img = np.zeros((1080,1920, 3))


drawing = False
ix = -1
iy = -1


def draw_shape(event,x,y,flags,params):
    global ix,iy,drawing

    if event == 1 : # for mouse single click
        
        drawing = True
        ix = x
        iy = y
       
    elif event == 0: # for moving the mouse 
        if drawing :
            cv2.rectangle(img, pt1 = (ix,iy), pt2 = (x,y), color = ( 255,255,0),thickness = -1)

        
    elif event == 4 :# for releasing the mouse
        drawing = False
        cv2.rectangle(img, pt1 = (ix,iy), pt2 = (x,y), color = ( 255,255,0),thickness = -1)


        

        


cv2.namedWindow(winname = "window")
cv2.setMouseCallback('window',draw_shape)


while True:
    cv2.imshow('window',img)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        print("\nclosing window\n")
        break   

cv2.destroyAllWindows()