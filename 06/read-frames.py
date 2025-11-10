import cv2

def FrameCapture(path):
    vidobj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        success, image = vidobj.read()
        if not success: break
        success = cv2.imwrite ("Frame_%d.jpg" % count, image)
        count += 1
        if count >= 3: break

if __name__== '__main__':
    FrameCapture ("../videos/video1.mp4")
