import cv2
import os
import subprocess

# Step 1: Video Processing to Extract Frames
video_path = "/home/apalayil/Project/video1.mp4"
frames_directory = "frames1"

# Create frames directory if it doesn't exist
if not os.path.exists(frames_directory):
    os.makedirs(frames_directory)

# Open the video file
cap = cv2.VideoCapture(video_path)
frame_counter = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Save frame as image
        frame_path = os.path.join(frames_directory, f"{frame_counter}.png")
        cv2.imwrite(frame_path, frame)

        frame_counter += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()

# Step 2: Shape Extraction
shape_extraction_script = "video_extract.py"
annotated_frames_directory = "annotated_frames1"

# Create annotated frames directory if it doesn't exist
if not os.path.exists(annotated_frames_directory):
    os.makedirs(annotated_frames_directory)

# Process frames iteratively using shape extraction script
for i in range(frame_counter):
    frame_path = os.path.join(frames_directory, f"{i}.png")
    annotated_frame_path = os.path.join(annotated_frames_directory, f"{i}.png")

    # Execute shape extraction script on the frame
    subprocess.run(["python", shape_extraction_script, frame_path, annotated_frame_path])

# Step 3: Generate Video with Labeled Shapes
output_video = "labeled_video1.avi"
framerate = 30

# Create video from annotated frames
subprocess.run(["python", "video_generate.py", annotated_frames_directory, output_video, str(framerate)])

print("Video processing and shape extraction completed!")

