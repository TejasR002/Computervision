import cv2
from ultralytics import YOLO



model = YOLO('D:/cmputerVisionSimform/basics/savedModels/my_model.pt')

results = model(source = 1,show =True,conf = 0.79) # change source for mulitple cameras attached, for using default cam try 0 




