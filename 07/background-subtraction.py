# Background subtraction – OpenCV
"""
BackgroundSubtractorMOG :  It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.
                           It detects movement in the image frame.

BackgroundSubtractorMOG2 :  It is also a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. 
                            It provides better adaptability to varying scenes due illumination changes etc.
                            This is the best algorithm among the three and is widely used.

BackgroundSubtractorGMG :  This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation.
"""

import cv2
import imutils

fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()

# cap = cv2.VideoCapture (0)  # web cam
cap = cv2.VideoCapture ('../videos/people.mp4')

while (True):
    ret, img = cap.read ()
    if not ret: break

    # Reduce size of the image to speed up processing, if needed
    img2 = imutils.resize (img, width = min(800, img.shape[1]))

    fgmask1 = fgbg1.apply(img2)
    fgmask2 = fgbg2.apply(img2)
    fgmask3 = fgbg3.apply(img2)

    cv2.imshow('Orginal', img2)
    cv2.imshow('MOG', fgmask1)
    cv2.imshow('MOG2', fgmask2)
    cv2.imshow('GMG', fgmask3)

    k = cv2.waitKey(30) & 0xff
    if k == 27: break  # ESC key

cap.release()
cv2.destroyAllWindows()
