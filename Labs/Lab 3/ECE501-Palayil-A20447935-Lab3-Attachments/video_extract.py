import cv2
import numpy as np
import os


def extract_shapes(image):
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 192, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        elif 6 < len(approx) < 15:
            cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        else:
            cv2.putText(img, "Circle", (x, y), font, 1, (0))
    
    return img

if __name__ == "__main__":
    # Provide the path to the directory containing frames
    frames_directory = "/home/apalayil/Project/frames1"

    # Provide the path to the directory where annotated frames will be saved
    annotated_frames_directory = "/home/apalayil/Project/annotated_frames1"

    # Process frames iteratively
    for image_file in os.listdir(frames_directory):
        if image_file.endswith(".png") or image_file.endswith(".jpg"):
            image_path = os.path.join(frames_directory, image_file)
            annotated_image = extract_shapes(image_path)
            annotated_image_path = os.path.join(annotated_frames_directory, image_file)
            cv2.imwrite(annotated_image_path, annotated_image)

