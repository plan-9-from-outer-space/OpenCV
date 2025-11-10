# Saving Video from a webcam using OpenCV

import cv2

cap = cv2.VideoCapture(0)
FourCC = cv2.VideoWriter_fourcc (*'XVID')
vw = cv2.VideoWriter ('output.avi', FourCC, fps=20.0, frameSize=(640, 480))

while (True):
    ret, frame = cap.read()
    vw.write(frame)
    cv2.imshow('Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
vw.release()

cv2.destroyAllWindows()
