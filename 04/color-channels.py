import cv2 as cv
import numpy as np

img = cv.imread('../images/pic.jpg')
cv.imshow('image', img)

b, g, r = cv.split (img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

merged = cv.merge ([b, g, r])
cv.imshow('merged', merged)

print(img.shape)
print(g.shape)
print(merged.shape)

cv.waitKey(0)
