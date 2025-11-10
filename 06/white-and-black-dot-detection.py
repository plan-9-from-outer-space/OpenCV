# White and black dot detection using OpenCV | Python
import cv2 as cv

# path = "../images/black-dot.jpg"
path = "../images/white-dot.png"

gray = cv.imread(path, flags=0) # 0 = grayscale
cv.imshow("Gray", gray)

# threshold
# th, threshed = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
th, threshed = cv.threshold(gray, 100, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# find contours 
cnts = cv.findContours(image=threshed, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 3    # square pixels
s2 = 20
xcnts = []

for cnt in cnts:
    if s1 < cv.contourArea(cnt) < s2:
        xcnts.append(cnt)

print(f"Total Number of black dots is {len(xcnts)}")

cv.waitKey(0)

