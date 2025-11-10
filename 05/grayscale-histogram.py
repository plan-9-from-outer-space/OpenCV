import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../images/Cat2.jpg')
cv.imshow('Cat', img)

# Convert the original image to grayscale.
gray = cv.cvtColor (src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

def get_centerpoint (img):
    height, width = img.shape[:2]
    center_x = width // 2
    center_y = height // 2
    return (center_x, center_y)

# Create a mask
blank = np.zeros (img.shape[:2], dtype='uint8')
circle = cv.circle (
    img = blank, 
    # center = (img.shape[1] // 2, img.shape[0] // 2), 
    center = get_centerpoint (img),
    radius = 100, 
    color = 255, 
    thickness = -1)
cv.imshow('Circle', circle)
mask = cv.bitwise_and (src1=gray, src2=gray, mask=circle)
cv.imshow('Mask', mask)

gray_hist = cv.calcHist (
    images = [gray],   # input image
    channels = [0],    # color channels
    mask = mask,       # optional mask
    histSize = [256],  # number of histogram bins
    ranges = [0, 256]  # histogram bin range
    )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
