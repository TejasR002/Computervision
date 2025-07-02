import cv2
from ultralytics import YOLO

# Load YOLOv8 model (adjust the path if needed)
model = YOLO("D:/cmputerVisionSimform/basics/savedModels/my_model.pt")  # or 'runs/detect/train/weights/best.pt'

# Set confidence threshold (e.g., 0.5)
model.conf = 0.5

# Input and output video paths
input_video_path = "D:/cmputerVisionSimform/basics/sampleVideos/video_20250513_210149.mp4"
output_video_path = "D:/cmputerVisionSimform/basics/predictedVideos/predicted_video.mp4"

# Load input video
cap = cv2.VideoCapture(input_video_path)
width  =  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height =  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    =  cap.get(cv2.CAP_PROP_FPS)
print(f'FPS of video is {fps}')
print(f'type of fps variable {type(fps)}')

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Inference loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 prediction on the frame
    results = model(frame,verbose = True)[0]
    

    # Draw bounding boxes on the frame
    annotated_frame = results.plot()
    annotated_frame = cv2.resize(annotated_frame, (width, height)) 
    cv2.imshow("displayed",annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
             break
    

    # Write frame to output video
    out.write(annotated_frame)

# Cleanup
cap.release()
out.release()

cv2.destroyAllWindows()

print(f"Inference complete. Video saved to: {output_video_path}")
