# Real-Time Face Detection using your webcam as a primary camera.
# You need to download the haarcascade xml file for this to work.
# This file is the result of training a classifier.

# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# cap = cv2.VideoCapture(0) # web cam
cap = cv2.VideoCapture("../videos/people.mp4")

blur = True  # Set to True to enable face blurring

while True:
    ret, img = cap.read()
    if not ret: break
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    faces = a.detectMultiScale (image=gray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        if not blur:
            cv2.rectangle (img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        else:
            face_roi = img[y:y+h, x:x+w]  # Region of Interest
            blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
            img[y:y+h, x:x+w] = blurred_face

    if not blur:
        cv2.imshow("Faces", img)
    else:
        cv2.imshow("Blurred Faces", img)
    
    if cv2.waitKey(1) & 0xff == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
