import cv2
import imutils
import numpy as np
from pyzbar.pyzbar import decode

# Initialize video
# cap = cv2.VideoCapture (0)
cap = cv2.VideoCapture ("../videos/bar-code.mov")
# cap = cv2.VideoCapture ("../videos/qr-code-2.mov")

barcode_detected = False  # Flag to stop after first detection

while True:
    success, frame = cap.read()
    if not success: break

    # Decode the barcodes/QR codes in the frame
    for code in decode (frame):
        data = code.data.decode ('utf-8')  # Extract data
        points = code.polygon              # Get the boundary points
        
        # Draw a polygon around the detected code 
        # Avoid this code block if you don't want to display the text in the current frame
        if points:
            pts = np.array ([(p.x, p.y) for p in points], np.int32)
            pts = pts.reshape ((-1, 1, 2)) # reshape the array for CV2
            cv2.polylines (frame, [pts], True, (0, 255, 0), 2)

        # Display the decoded text above the code
        x, y, w, h = code.rect
        cv2.putText (frame, data, (x, y - 10), 
                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        
        print(f"Detected Code: {data}")

        barcode_detected = True  # Set flag when barcode is found

        break  # Exit the inner loop after first detection

    # Show video feed
    frame = imutils.resize (frame, width = min(800, frame.shape[1]))
    cv2.imshow ('Barcode/QR Code Scanner', frame)

    # Exit conditions
    if barcode_detected or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
