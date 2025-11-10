import cv2
import imutils

gun_cascade = cv2.CascadeClassifier ('gun_cascade.xml')

# camera = cv2.VideoCapture (0) # web cam
cap = cv2.VideoCapture ("../videos/gun.mov")

firstFrame = None
guns_exist = None

while True:
   ret, frame = cap.read()
   if not ret: break
   frame = imutils.resize(frame, width=500)
   gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
   guns = gun_cascade.detectMultiScale (
       image=gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))
   
   if len(guns) > 0:
       guns_exist = True

   for (x, y, w, h) in guns:
       frame = cv2.rectangle (frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
   cv2.imshow("Security", frame)

   key = cv2.waitKey(1) & 0xff
   if key == ord('q'): break
   
if guns_exist:
    print("Guns Detected")
else:
    print("Guns not found")

cap.release()
cv2.destroyAllWindows()
