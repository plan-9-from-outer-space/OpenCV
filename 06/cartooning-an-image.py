import cv2

# image = cv2.imread('../images/Cat2.jpg')
image = cv2.imread('../images/people-headshot-lauren-lieberman.jpg')

# d = diameter of filtering pixel neighborhood (kernel)
color = cv2.bilateralFilter (image, d=9, sigmaColor=75, sigmaSpace=75)

gray = cv2.cvtColor (image, code=cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur (gray, ksize=7)

edges = cv2.adaptiveThreshold (gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

cartoon = cv2.bitwise_and (color, color, mask=edges)

cv2.imshow('Orginal Image', image)
cv2.imshow('Cartoonized Image', cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
