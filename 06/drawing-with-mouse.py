import cv2

img = cv2.imread("../images/Cat2.jpg")

def draw_circle (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("Hello")
        cv2.circle (img, (x, y), 100, (0, 255, 0), -1)

cv2.namedWindow (winname="Popup Window")
cv2.setMouseCallback ("Popup Window", draw_circle)

while True:
    cv2.imshow("Popup Window", img)
    if cv2.waitKey(10) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
