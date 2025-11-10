import cv2 as cv
import numpy as np

img = cv.imread ('../images/Cat2.jpg')
cv.imshow('Cat', img)

# The mask must have the same shape as the original image.
blank = np.zeros (img.shape[:2], dtype='uint8')
# blank = np.zeros (300, 300, dtype='uint8') # Causes an error, wrong shape.
# cv.imshow('Blank', blank)

mask = cv.circle (blank, (img.shape[1] // 2 + 0, img.shape[0] // 2 - 45), 125, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and (img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)
