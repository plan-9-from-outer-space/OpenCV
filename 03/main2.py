import cv2 as cv

# img = cv.imread('images/cat1.jpg')

# cv.imshow('cat', img)
capture = cv.VideoCapture('videos/video1.mp4')
# capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
