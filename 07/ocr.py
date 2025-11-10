# Text Detection and Extraction using OpenCV and OCR

import cv2
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = 'tesseract'

img = cv2.imread("../images/sample.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pyt.image_to_string(gray)
print(text)

file = open("ocr.txt", "w+")
file.write(text)
file.close()

# cv2.imshow("Demo", gray)
# cv2.waitKey(0)
