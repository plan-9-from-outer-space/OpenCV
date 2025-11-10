# Pedestrian Detection using OpenCV-Python

# The cv2.HOGDescriptor class in OpenCV implements the Histogram of 
# Oriented Gradients (HOG) feature descriptor, which is widely used 
# for object detection, particularly for pedestrian detection.

import cv2
import imutils

hog = cv2.HOGDescriptor ()
hog.setSVMDetector (cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture ('../videos/people.mp4')

while cap.isOpened ():
    ret, img = cap.read ()
    if not ret: break
    # Reduce size of the image to speed up processing, if needed
    img = imutils.resize (img, width = min(600, img.shape[1]))
    # Detect pedestrians in the image
    (regions, confidence_scores) = hog.detectMultiScale (img, winStride=(4, 4), padding=(4, 4), scale=1.05)
    # Draw bounding boxes around detected pedestrians
    threshold = 0.25  # Confidence threshold
    for i, (x, y, w, h) in enumerate(regions):
        # Only consider detections with a confidence score above the threshold
        print(confidence_scores[i])
        if confidence_scores[i] > threshold: 
            cv2.rectangle (img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Display the output image
    cv2.imshow ('Img', img)
    if cv2.waitKey (25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
