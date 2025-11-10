import cv2 as cv

img = cv.imread ('../images/cat2.jpg')
cv.imshow('cat', img)

# Averaging (default method)
average = cv.blur (img, (7, 7))
cv.imshow('Average', average)

# Gaussian Blur
gauss = cv.GaussianBlur (img, (7, 7), 0)
cv.imshow('Gaussian', gauss)

# Median Blur
median = cv.medianBlur (img, 9)
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter (img, 9, 75, 75)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
