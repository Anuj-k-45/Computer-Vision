import cv2
import numpy as np

img = cv2.imread("./assets/lion.jpg")
img=cv2.resize(img, (800,450))
img = cv2.copyMakeBorder(img, 10, 10, 5, 5, cv2.BORDER_CONSTANT, value=[255, 0, 125] )
# cv2.copyMakeBorder(img, border_width(4 sides), border_type, value(color BGR))
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()