import cv2

cascade = 'cars.xml'
video = '../videos/cars.mp4'

cap = cv2.VideoCapture (video)
car_cascade = cv2.CascadeClassifier (cascade)

while True:
    ret, image = cap.read()
    if not ret: break

    gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale (gray, 1.1, 1)
    
    for (x, y, w, h) in cars:
        cv2.rectangle (image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imshow ('Cars', image)
    
    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()
