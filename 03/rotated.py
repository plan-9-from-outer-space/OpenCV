import cv2 as cv
import numpy as np

img = cv.imread('../images/Cat2.jpg')

cv.imshow('Boston', img)

# Rotation
def rotate (img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    # Rotation Point (center)
    if rotPoint is None:
        rotPoint = (width // 2, height // 2) # center of the image
    # Rotation Matrix
    rotMat = cv.getRotationMatrix2D (center=rotPoint, angle=angle, scale=1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate (img, 45, (250, 250))
cv.imshow("rotated", rotated)

cv.waitKey(0)
