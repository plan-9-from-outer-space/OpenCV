import cv2
import numpy as np

def emptyFunction(x):
    # print(x)
    pass

image = np.zeros((512, 512, 3), np.uint8) # BGR
windowName = "Open CV Color Palette"

cv2.namedWindow(windowName)

# cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunction) # old way

args = (windowName, 0, 255, emptyFunction)

cv2.createTrackbar('Blue', *args)
cv2.createTrackbar('Green', *args)
cv2.createTrackbar('Red', *args)

while (True):
    cv2.imshow(windowName, image)
    if cv2.waitKey(1) == 27: break  # ESC key

    blue = cv2.getTrackbarPos('Blue', windowName)
    green = cv2.getTrackbarPos('Green', windowName)
    red = cv2.getTrackbarPos('Red', windowName)

    # Set all pixels to the selected color
    image[:] = [blue, green, red]  # BGR
    # print(blue, green, red)
