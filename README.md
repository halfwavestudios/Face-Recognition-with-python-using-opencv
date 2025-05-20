# 🧠 Real-Time Face Detection with OpenCV

A simple and effective face detection project using Python and OpenCV’s Haar Cascade Classifier. This application can detect human faces in both **static images** and **real-time webcam streams**, drawing rectangles around the faces it identifies.

---

## 📸 Features

- 🧍 Detects faces in real-time using your webcam
- 🖼️ Also supports static image or video file input
- 🧠 Based on Haar Cascade — fast and efficient
- 💻 Easy to set up and run locally
- 🧰 Beginner-friendly, well-commented Python code

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/halfwavestudios/face-detection-opencv.git
   cd face-detection-opencv
Install dependencies

bash
Copy
Edit
pip install opencv-python
Ensure you have the Haar cascade file
The file haarcascade_frontalface_default.xml should be in the same directory as your script. If not, download it from OpenCV's GitHub.

🚀 Usage
▶️ Run real-time face detection from webcam:
bash
Copy
Edit
python webcam_face_detection.py
🖼️ Run face detection on an image:
bash
Copy
Edit
python image_face_detection.py
Make sure your image path is set correctly in the script.

🧪 Example Output
(You can insert your own screenshots or gifs here)

Real-time Webcam	Static Image Detection

📂 Project Structure
pgsql
Copy
Edit
face-detection-opencv/
├── haarcascade_frontalface_default.xml
├── webcam_face_detection.py
├── image_face_detection.py
├── faces/
│   └── bill.jpg
├── screenshots/
│   └── webcam_demo.gif
└── README.md
🧠 How It Works
OpenCV loads a Haar Cascade — a pre-trained classifier for face detection.

The image or video is converted to grayscale to simplify detection.

detectMultiScale() finds the face regions.

Detected faces are highlighted using cv2.rectangle().

The result is displayed or saved.

🙌 Credits
Developed by Halfwave Studios
📷 Powered by OpenCV

📃 License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy
Edit

