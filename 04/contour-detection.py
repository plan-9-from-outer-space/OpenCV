import cv2 as cv
import numpy as np

img = cv.imread ('../images/Cat2.jpg')
# cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

gray = cv.cvtColor (img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blurring reduces the number of contour lines detected
# kernel size = (5, 5)
# blur = cv.GaussianBlur (gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny (blur, 125, 175)
# cv.imshow('canny', canny)

# Threshold produces a binary image (black and white)
ret, thresh = cv.threshold (gray, 125, 255, cv.THRESH_BINARY)
cv.imshow ('thresh', thresh)

contours, hierarchise = cv.findContours (
    image=thresh, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours (blank, contours, -1, (0, 0, 255), 1)
cv.imshow ('blank', blank)

cv.waitKey(0)
