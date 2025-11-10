import cv2 as cv
import numpy as np

# Create a blank image (black)
black = np.zeros((500, 500, 3), dtype='uint8')
# gray = np.full((500, 500, 3), 128, dtype=np.uint8)
# white = np.full((500, 500, 3), 255, dtype=np.uint8)
# cv.imshow('black', black)
# cv.imshow('gray', gray)
# cv.imshow('white', white)

# Paint the image in certain colors
# black[:] = 0, 255, 0  # RGB
# black[200:300, 300:400] = 0, 0, 255  # RGB
# cv.imshow('green', black)

# Draw a rectangle
# cv.rectangle(black, (50, 50), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# cv.rectangle(black, (0, 0), (black.shape[1] // 2, black.shape[0] // 3), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('rectangle', black)

# Draw a Circle
# red = (0, 0, 255)
# cv.circle(black, (250, 250), 40, red, thickness=-1)
# cv.imshow('circle', black)

# Draw a line
# white = (255, 255, 255)
# cv.line(black, (20, 20), (black.shape[1] // 2, black.shape[0] // 3), white, thickness=3)
# cv.imshow('line', black)

# Write text on image
green = (0, 255, 0)
cv.putText(black, 'hello world', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, green, 1)
cv.imshow('Text', black)

cv.waitKey(0)
cv.destroyAllWindows()
