import cv2
import numpy as np
import json
import os

# Load video
path = "C:/Users/TEJAS/Downloads/video_20250602_151517.mp4"

trim_video_path = "trimmedVideo1/"
try:
    os.mkdir(trim_video_path)
except:
    print("Already Exist" , trim_video_path)


trim_video_metadata_path  = "trimmedVideoMetadata1/"
try :
    os.mkdir(trim_video_metadata_path)
except:
    print("Already Exist" , trim_video_metadata_path)

    
def process_video(path):

    cap = cv2.VideoCapture(path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # out = cv2.VideoWriter("output_motion_video.mp4",
    #                       cv2.VideoWriter_fourcc(*'mp4v'),
    #                       fps, (width, height))

    video_name = os.path.splitext(os.path.basename(path))[0]
    output_video_path = f'{trim_video_path}{video_name}.avi'
    output_log = f"{trim_video_metadata_path}{video_name}.json"

    out = cv2.VideoWriter(output_video_path, 
                            cv2.VideoWriter_fourcc(*'XVID'),
                            5, (width , height))


    previous_gray = None
    threshold = 20000000
    frame_number = 0
    metadata_list = []


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        motion_score = 0
        if previous_gray is not None:
            diff = cv2.absdiff(gray, previous_gray)
            motion_score = int(np.sum(diff))

        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        print(f"Frame: {frame_number}, Time: {timestamp:.2f}s, Motion: {motion_score}")
        if motion_score > threshold:

            label = f"Frame: {frame_number}, Time: {timestamp:.2f}s, Motion: {motion_score}"
            cv2.putText(frame, label, (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2, cv2.LINE_AA)

            print("Inside video processing")
            out.write(frame)

            metadata_list.append({
                "frame": frame_number,
                "timestamp": round(timestamp, 3),
                "motion_score": motion_score
            })

        previous_gray = gray
        frame_number += 1

    cap.release()
    out.release()

    # Save metadata as JSON
    with open(output_log, "w") as f:
        json.dump(metadata_list, f, indent=4)
    
    if len(metadata_list) == 0:
        os.remove(output_video_path) 
        print("Processing complete. No change detected so no trim video but log saved.")
    
    else:
        print("Processing complete. Video and log saved")



def get_all_file_paths(folder_path):
    file_paths = []
    for root, os.dirs, files in os.walk(folder_path):
        print("inside get all file paths")
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    return file_paths

folder = "data_one"
print(folder)
all_files = get_all_file_paths(folder)
print(all_files)
for file in all_files:
    print(file)
    process_video(file)
    print(file) 