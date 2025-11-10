import cv2

# [print(i) for i in dir(cv2) if 'EVENT' in i]

# EVENT_FLAG_ALTKEY
# EVENT_FLAG_CTRLKEY
# EVENT_FLAG_LBUTTON
# EVENT_FLAG_MBUTTON
# EVENT_FLAG_RBUTTON
# EVENT_FLAG_SHIFTKEY
# EVENT_LBUTTONDBLCLK
# EVENT_LBUTTONDOWN
# EVENT_LBUTTONUP
# EVENT_MBUTTONDBLCLK
# EVENT_MBUTTONDOWN
# EVENT_MBUTTONUP
# EVENT_MOUSEHWHEEL
# EVENT_MOUSEMOVE
# EVENT_MOUSEWHEEL
# EVENT_RBUTTONDBLCLK
# EVENT_RBUTTONDOWN
# EVENT_RBUTTONUP

def click_event (event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ', ' + str(y), (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, " ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ', ' + str(y), (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

# This is needed because we are calling a function from the current page?
if __name__ =="__main__":

    img = cv2.imread('../images/Cat2.jpg', 1) # 1 = BGR
    cv2.imshow('image', img)
    cv2.setMouseCallback(window_name='image', on_mouse=click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
