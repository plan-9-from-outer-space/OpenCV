import cv2
import numpy as np
import time

# Components of HSV in OpenCV:
#     Hue (H):
#           Represents the pure color type, such as red, green, or blue. In OpenCV, Hue values range from 0 to 179.
#     Saturation (S):
#           Indicates the intensity or purity of the color. A fully saturated color is vibrant, while a color 
#           with zero saturation appears as a shade of gray. In OpenCV, Saturation values range from 0 to 255.
#     Value (V):
#           Controls the lightness or brightness of the color. A Value of zero represents black, while increasing
#           the Value leads to lighter colors. In OpenCV, Value values range from 0 to 255. 

capture_video = cv2.VideoCapture(0) # web cam

time.sleep(1)
count = 0
background = 0

# Read the first 60 frames to capture the background
for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

background = np.flip(background, axis=1)

while (capture_video.isOpened()):
    return_val, img = capture_video.read()
    if not return_val: break
    count = count + 1

    img = np.flip (img, axis=1)
    hsv = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)

    # setting the lower and upper range for mask1
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # setting the lower and upper range for mask2
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx (mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate (mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not (mask1)

    res1 = cv2.bitwise_and (background, background, mask=mask1)
    res2 = cv2.bitwise_and (img, img, mask=mask2)

    final_output = cv2.addWeighted (res1, 1, res2, 1, 0)

    cv2.imshow("Invisible T-Shirt", final_output)
    k = cv2.waitKey(10)
    if k==27: break

capture_video.release()
cv2.destroyAllWindows()
