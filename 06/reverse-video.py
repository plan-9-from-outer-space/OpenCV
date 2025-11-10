import cv2
import os
import shutil

cap = cv2.VideoCapture("../videos/IMG_1546.mov")

check, frame = cap.read()
if not check: 
    print("Video not found or unable to open")
    exit()

counter = 0
scale_factor = 0.5
frame_list = []

# Create a temp directory to store the frames (optional)
# if os.path.isdir('temp'):
#     shutil.rmtree('temp')
# os.mkdir('temp')

while (check == True):
    check, frame = cap.read()
    if not check: break
    # Resize the frames, if they are too large
    resized_frame = cv2.resize (frame, None, fx=scale_factor, fy=scale_factor)
    # Write the frame images to the temp directory (optional)
    # cv2.imwrite("temp/frame_%d.jpg" % counter, resized_frame)
    frame_list.append(resized_frame)
    counter += 1

# frame_list.pop()
frame_list.reverse()  # Reverse the frames

# Write the reversed frames to a new video.
fourcc = cv2.VideoWriter_fourcc (*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
height, width = frame_list[0].shape[:2]  # ignore channels
frame_size = (width, height)
print('FPS = ', fps, ' Frame Size = ', frame_size)
vw = cv2.VideoWriter ('reversed.mov', fourcc, fps=fps, frameSize=frame_size)

for frame in frame_list:
    # cv2.imshow("Frame", frame)
    # if cv2.waitKey(25) and 0xff == ord("q"):
    #     break
    vw.write(frame)

# Delete the saved frames (if they were saved)
# shutil.rmtree('temp')

cap.release()
vw.release()
cv2.destroyAllWindows()
