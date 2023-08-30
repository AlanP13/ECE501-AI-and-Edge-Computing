import cv2
import os

def generate_video(frames_directory, output_video, framerate):
    # Get the list of frames
    frames = sorted(os.listdir(frames_directory))

    # Read the first frame to get dimensions
    frame_path = os.path.join(frames_directory, frames[0])
    frame = cv2.imread(frame_path)
    height, width, _ = frame.shape
    size = (width, height)

    # Create video writer object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video = cv2.VideoWriter(output_video, fourcc, framerate, size)

    # Write each frame to the video
    for frame_name in frames:
        frame_path = os.path.join(frames_directory, frame_name)
        frame = cv2.imread(frame_path)
        video.write(frame)

    # Release resources
    video.release()
    cv2.destroyAllWindows()

# Usage
frames_directory = "/home/apalayil/Project/annotated_frames1"
output_video = "video_processed1.avi"
framerate = 30

generate_video(frames_directory, output_video, framerate)

