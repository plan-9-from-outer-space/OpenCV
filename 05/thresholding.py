import cv2 as cv

img = cv.imread('../images/Cat2.jpg')
# cv.imshow("Cat", img)

gray = cv.cvtColor (img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold (
    src=gray, thresh=120, maxval=255, type=cv.THRESH_BINARY)
# cv.imshow('Simple Threshold', thresh)

# Inverse thresholding
threshold, thresh_inv = cv.threshold (
    gray, 120, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Threshold Inv', thresh_inv)

# Adaptive Thresholding (CV will find the optimal threshold)
a_thresh = cv.adaptiveThreshold (
    src=gray, 
    maxValue=255, 
    adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, 
    thresholdType=cv.THRESH_BINARY, 
    blockSize=11,  # kernel size
    C=3)
cv.imshow('Adaptive Threshold', a_thresh)

cv.waitKey(0)
