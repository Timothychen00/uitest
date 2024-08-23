import cv2
import numpy as np
from icecream import ic

img = cv2.imread('screenshots/target.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
 
lower_blue = np.array([100, 30, 0])
upper_blue = np.array([150, 255, 255])
 
mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
 
res = cv2.bitwise_and(img, img, mask=mask)
r, g, b = cv2.split(res)
r_num = 0
for i in b:
    for j in i:
        if j > 170:
            r_num += 1
print(r_num)