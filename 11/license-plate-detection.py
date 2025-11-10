import cv2
import imutils
import pytesseract as pyt

# Initialize Tesseract OCR executable path
pyt.pytesseract.tesseract_cmd = 'tesseract'

# Pre-trained ML model for Russian car plate detection
haarcascade = "haarcascade_russian_plate_number.xml"
count = 0
cap = cv2.VideoCapture ("../videos/russian-license-plate.mov")

while True:
    ret, img = cap.read()
    if not ret: break

    # Reduce size of the image to speed up processing or if it's too large
    img2 = imutils.resize (img, height = min(800, img.shape[1]))
    
    plate_cascade = cv2.CascadeClassifier (haarcascade)
    
    gray = cv2.cvtColor (img2, cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale (gray, 1.1, 4)
    
    for (x, y, w, h) in plates:
        cv2.rectangle (img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText (img2, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
        img_roi = img2[y:y+h, x:x+w]
        cv2.imshow ("ROI", img_roi)

    cv2.imshow ("Car Plate", img2)

    # s = Save plate image and text (of the last plate in the above loop)
    # q = Quit
    if cv2.waitKey(1) & 0xFF == ord('s'):

        # Capture the license plate image and save it to file
        cv2.imwrite ("Plates/Car_plate_" + str(count) + ".jpg", img_roi)
        cv2.rectangle (img2, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText (img2, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow ("Car Plate", img2)
        cv2.waitKey (500)

        # Capture the license plate numbers using OCR, save to text file
        # NOTE: The license plate numbers are too small and fuzzy, so it does not work well
        gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        text = pyt.image_to_string (image=gray) # lang='eng')
        file = open("Plates/Car_plate_" + str(count) + ".txt", "w+")
        file.write(text)
        file.close()

        count += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
