# Template Matching is a method for searching and finding the location of a template image in a larger image. 

import cv2

img = cv2.imread('../images/soccer.jpg', 0)
# template = cv2.imread('../images/football.jpg', 0)
template = cv2.imread('../images/shoe.jpg', 0)

h, w = template.shape

# Template matching methods/algorithms
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    print('method = ', method)
    img2 = img.copy()
    result = cv2.matchTemplate (img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc (result)
    # print(min_val, max_val, min_loc, max_loc)
    # The methods TM_SQDIFF and TM_SQDIFF_NORMED return the minimum value as the best match.
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle (img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
