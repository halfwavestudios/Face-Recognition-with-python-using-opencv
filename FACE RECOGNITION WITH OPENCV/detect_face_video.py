import cv2

# LOAD THE CASCADE
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# TO CAPTURE THE FACE IN THE WEBCAM/CAMERA 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # CONVERT THE FACES READ INTO GRAYSCALE
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # DETECT THE GRAYSCALED FACES 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # DRAW A RECTANGLE AROUND THE DETECTED FACE(S)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # DISPLAY THE OUTPUT
    cv2.imshow('img', img)

    # STOP THE PYTHON SCRIPT WITH ESCAPE KEY
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# RELEASE THE VIDEO CAPTURE PROCESS
cap.release()
