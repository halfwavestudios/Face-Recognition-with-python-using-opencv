"""
Face Detection with OpenCV using Haar Cascade
--------------------------------------------------

This script performs face detection on a static image using a pre-trained Haar Cascade classifier.
It identifies human faces, draws rectangles around them, and displays the final image.

Dependencies:
- OpenCV (Install using: pip install opencv-python)

Required Files:
- haarcascade_frontalface_default.xml (Haar cascade data for face detection)
- Input image (e.g., 'faces/bill.jpg')

Author: Halfwave Studios
GitHub: https://github.com/halfwavestudios
"""

import cv2
import os

# === Load the Haar Cascade Classifier ===
cascade_path = 'haarcascade_frontalface_default.xml'

if not os.path.exists(cascade_path):
    raise FileNotFoundError(f"[ERROR] Haar cascade file not found: {cascade_path}")

face_cascade = cv2.CascadeClassifier(cascade_path)

# === Load the Input Image ===
img_path = 'faces/bill.jpg'

if not os.path.exists(img_path):
    raise FileNotFoundError(f"[ERROR] Image file not found: {img_path}")

img = cv2.imread(img_path)

if img is None:
    raise ValueError(f"[ERROR] Failed to load image from: {img_path}")

# === Convert the Image to Grayscale ===
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# === Detect Faces in the Image ===
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4
)

# === Draw Rectangles Around Detected Faces ===
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# === Display the Result ===
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# === Optional: Save the Output ===
# cv2.imwrite('output_faces_detected.jpg', img)
