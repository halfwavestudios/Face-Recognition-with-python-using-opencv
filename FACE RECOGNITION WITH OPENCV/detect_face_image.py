
# INSTALL CV2 WITH :PIP INSTALL OPENCV-PYTHON
import cv2

# LOAD THE CASCADE
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# READ THE PROVIDED INPUT IMAGE
img = cv2.imread('faces/bill.jpg')

# CONVERT THE PROVIDED IMAGE INTO GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# DETECT THE FACES PRESENT IN THE IMAGE "READ"
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# DRAW A RECTANGLE AROUND THE DETECTED FACE(S)

for (x, y, w, h) in faces:
    
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# DISPLAY THE OUTPUT

cv2.imshow('img', img)
cv2.waitKey()
