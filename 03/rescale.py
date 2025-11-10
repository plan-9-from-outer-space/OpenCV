import cv2 as cv

# img = cv.imread('../images/cat2.jpg')
# cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('resized_cat', resized_image)
# cv.waitKey(0)

capture = cv.VideoCapture('../videos/video1.mp4')

while True:
    ret, frame = capture.read()
    if not ret: break
    frame_resized = rescaleFrame(frame, scale=.30)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

