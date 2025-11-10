import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../images/Cat2.jpg')
cv.imshow('cat', img)

# plt.imshow(img)
# plt.show()

# BGR to GrayScale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

# CV2 uses BGR, but other apps use RGB.
# bgr to rgb
rgb = cv.cvtColor (img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor (hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
