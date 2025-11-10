import cv2 as cv

img = cv.imread('../images/Cat2.jpg')
cv.imshow('Cat', img)

# Converting image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)
# blur2 = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('blur 2', blur2)

# Edge Cascade (blurring, grading, ???)
# canny = cv.Canny(img, 125, 175)
# canny2 = cv.Canny(blur2, 125, 175)
# cv.imshow('canny', canny)
# cv.imshow('canny2', canny2)

# Dilating the image
# dilated = cv.dilate(canny, kernel=(3, 3), iterations=3)
# cv.imshow('dilated', dilated)

# Resize
resize = cv.resize(img, (400, 400))
cv.imshow('resize', resize)

# Cropping
cropped = img[50:250, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
