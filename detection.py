import cv2 as cv
import numpy as np

haystack_img = cv.imread('images/testing/diamond_scene_2.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('images/ores/diamond_ore/diamond_ore_1.png', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# Get the best match position from the haystack.
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print(f'Best match {max_loc}')
print(f'Best match confidence {max_val}')

threshold = 0.5
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))

if locations:
    print("Found needle")
    
    #Dimensions of the needle
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    line_color = (0, 255, 0)
    line_type = cv.LINE_4
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

cv.imshow('Matches', haystack_img)
cv.waitKey()