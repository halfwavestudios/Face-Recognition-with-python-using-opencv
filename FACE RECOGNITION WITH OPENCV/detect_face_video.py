"""
Real-Time Face Detection Using OpenCV and Haar Cascade

This script captures video from the webcam and uses OpenCV's Haar Cascade classifier
to detect and highlight human faces in real-time.

Author: Halfwave Studios
GitHub: https://github.com/halfwavestudios
"""

import cv2

# === Load the Haar Cascade Classifier ===
cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# === Initialize Webcam Video Capture ===
cap = cv2.VideoCapture(0)  # Use 0 for default webcam
# To use a video file instead, replace the line above with:
# cap = cv2.VideoCapture('your_video_file.mp4')

if not cap.isOpened():
    raise IOError("[ERROR] Cannot open webcam or video file.")

print("[INFO] Press 'ESC' to exit the application.")

while True:
    # === Read a Frame from the Camera ===
    ret, frame = cap.read()
    if not ret:
        print("[WARNING] Failed to grab frame. Exiting.")
        break

    # === Convert Frame to Grayscale ===
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # === Detect Faces in the Grayscale Frame ===
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # === Draw Bounding Boxes Around Detected Faces ===
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # === Display the Frame with Detected Faces ===
    cv2.imshow('Face Detection - Halfwave Studios', frame)

    # === Exit Loop on ESC Key Press ===
    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # ESC key
        print("[INFO] ESC key pressed. Exiting...")
        break

# === Release Resources ===
cap.release()
cv2.destroyAllWindows()
