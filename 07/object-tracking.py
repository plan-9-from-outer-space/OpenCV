import cv2
import numpy as np

# cap = cv2.VideoCapture(0)  # web cam
cap = cv2.VideoCapture("../videos/IMG_1548.mov")

def nothing(x):
    pass

cv2.namedWindow('Tracking')

# Create the track bars for color change
cv2.createTrackbar ('LH', "Tracking", 0, 255, nothing) # Lower hue
cv2.createTrackbar ('LS', "Tracking", 0, 255, nothing) # Lower saturation
cv2.createTrackbar ('LV', "Tracking", 0, 255, nothing) # Lower value
cv2.createTrackbar ('HH', "Tracking", 200, 255, nothing) # Higher hue
cv2.createTrackbar ('HS', "Tracking", 200, 255, nothing) # Higher saturation
cv2.createTrackbar ('HV', "Tracking", 200, 255, nothing) # Higher value

while True:
    check, frame = cap.read()
    if not check: break

    frame2 = cv2.resize (frame, (600, 400))
    frame = frame2

    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV) # convert to HSV
    
    l_h = cv2.getTrackbarPos ("LH", "Tracking")
    l_s = cv2.getTrackbarPos ("LS", "Tracking")
    l_v = cv2.getTrackbarPos ("LV", "Tracking")
    h_h = cv2.getTrackbarPos ("HH", "Tracking")
    h_s = cv2.getTrackbarPos ("HS", "Tracking")
    h_v = cv2.getTrackbarPos ("HV", "Tracking")
    
    l_b = np.array ([l_h, l_s, l_v]) # Lower bounds
    u_b = np.array ([h_h, h_s, h_v]) # Upper bounds
    
    mask = cv2.inRange (hsv, l_b, u_b)
    result = cv2.bitwise_and (frame, frame, None, mask)

    # print (frame.shape) # (1440, 1920, 3)
    # break
    
    cv2.imshow ("Frame", frame)
    cv2.imshow ("Mask", mask)
    cv2.imshow ("Result", result)
    
    if cv2.waitKey(25) and 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
