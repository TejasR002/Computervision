# import cv2
# import numpy as np
# from datetime import datetime
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# current_time = datetime.now().time()
# file_name = f'OUTPUT at time {current_time}.mp4'
# writer = cv2.VideoWriter(file_name,fourcc,30,(1280,720))

# while True:
    
#     ret,  frame = cap.read()
#     print(ret)

#     IMG_GRY = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     writer.write(IMG_GRY)
#     cv2.imshow("webcame", IMG_GRY)


#     if cv2.waitKey(1) == ord('x'):
#         break

# cv2.destroyAllWindows()


import cv2
from datetime import datetime

# Start webcam
cap = cv2.VideoCapture(0)

# Get frame size from webcam
ret, frame = cap.read()
if not ret:
    print("Error: Unable to read from webcam.")
    cap.release()
    exit()

x = frame.shape
print(x)
height, width = frame.shape[:2]

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Format time for filename (colons replaced with dashes)
current_time = datetime.now().strftime("%H-%M-%S")
file_name = f'OUTPUT_at_{current_time}.mp4'

writer = cv2.VideoWriter(file_name, fourcc, 60, (width, height))


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Write the original BGR frame (not RGB)
    writer.write(frame)

    # Display the video feed
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release everything
cap.release()
writer.release()
cv2.destroyAllWindows()
