"""
bitwise_and: Applies a logical AND operation to each pixel of two images or an image and a mask.
bitwise_or:  Applies a logical OR operation.
bitwise_xor: Applies a logical XOR operation.
bitwise_not: Inverts the pixels (logical NOT).
"""

import cv2 as cv
import numpy as np

# Create a blank image (black).
blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle (blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle (blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise And (intersection)
bitwise_and = cv.bitwise_and (rectangle, circle)
# cv.imshow('bitwise_and', bitwise_and)

# Bitwise Or (union)
bitwise_or = cv.bitwise_or (rectangle, circle)
# cv.imshow('bitwise_or', bitwise_or)

# Bitwise Xor (masking)
bitwise_xor = cv.bitwise_xor (rectangle, circle)
# cv.imshow('bitwise_xor', bitwise_xor)

# Bitwise Not (inversion)
bitwise_not = cv.bitwise_not (circle)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
