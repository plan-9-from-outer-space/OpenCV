
import pyautogui
import cv2
import numpy as np

# Specify resolution (must match your screen size)
# resolution = (1920, 1080)
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)
print(f"Screen Width: {screen_width} pixels")
print(f"Screen Height: {screen_height} pixels")

# Specify video codec, output file name, FPS
codec = cv2.VideoWriter_fourcc (*"XVID")
filename = "Recording.avi"
fps = 10.0

# Creating a VideoWriter object
out = cv2.VideoWriter (filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow ("Live", cv2.WINDOW_NORMAL)
# Resize the window
# cv2.resizeWindow ("Live", 480, 270)
cv2.resizeWindow ("Live", int(0.25 * screen_width), int(0.25 * screen_height))

while True:
	# Take a screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array (img)

	# Convert the frame from BGR to RGB
	frame = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)

	# Write the frame to the output file
	out.write (frame)
	
	# Optional: Display the recorded screen
	cv2.imshow ('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
