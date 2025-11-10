import cv2 as cv
import numpy as np

img = cv.imread('../images/Cat2.jpg')

cv.imshow('cat', img)

resized = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# Flipping
flip = cv.flip (img, -1)
# cv.imshow('flip', flip)

# Cropping
cropped = img[50:200, 100:200]
cv.imshow('cropped', cropped)

cv.waitKey(0)
