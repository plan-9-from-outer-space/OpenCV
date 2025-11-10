import cv2 as cv
import numpy as np

img = cv.imread('../images/Cat2.jpg')

cv.imshow('Boston', img)

# Translation
def translate (img, x, y):
    # Create a translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine (img, transMat, dimension)
# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down
translated = translate (img, 100, -100)
cv.imshow("translated", translated)

cv.waitKey(0)
