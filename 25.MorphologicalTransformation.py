#operations performaed based on the image shape
#performed on gray scale images

import cv2
import numpy as np

img = cv2.imread("./assets/col_balls.jpg", 0)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((5, 5), np.uint8)
e = cv2.erode(mask, kernal)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("erossion", e)

cv2.waitKey(0)
cv2.destroyAllWindows()


kernal = np.ones((1, 1), np.uint8)
d = cv2.dilate(mask, kernal)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("erossion", e)
cv2.imshow("dilate", d)

cv2.waitKey(0)
cv2.destroyAllWindows()