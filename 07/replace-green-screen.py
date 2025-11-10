import cv2
import numpy as np

frame_size = (640, 480)

background = cv2.imread ('../images/soccer.jpg')
background = cv2.resize (background, frame_size)

# Define the green color range in HSV
# lower_green = np.array ([35, 100, 100])
# upper_green = np.array ([85, 255, 255])
lower_green = np.array ([35, 60, 60])
upper_green = np.array ([85, 255, 255])

cap = cv2.VideoCapture ("../videos/green-screen.mov")

if not cap.isOpened():
    print("Video not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret: break
   
    frame = cv2.resize (frame, frame_size)
    hsv = cv2.cvtColor (frame, code=cv2.COLOR_BGR2HSV)
   
    mask = cv2.inRange (hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not (mask)
   
    person = cv2.bitwise_and (frame, frame, mask=mask_inv)
    background_part = cv2.bitwise_and (background, background, mask=mask)
   
    result = cv2.add (person, background_part)
   
    cv2.imshow ("Demo", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
