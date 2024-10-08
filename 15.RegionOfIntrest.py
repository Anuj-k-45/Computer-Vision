import cv2
import numpy as np

img = cv2.imread("./assets/roi_opr.jpg")
img = cv2.resize(img, (800, 800))

#ROI : (320, 50) (440, 205)
# [(y1, y2), (x1, x2)]
x1 = 320
x2 = 440
y1 = 50
y2 = 205

roi = img[y1:y2, x1:x2] #numpy array slicing

img[y1:y2, x2:(x2+x2-x1)] = roi
img[y1:y2, x1-(x2-x1):x1] = roi


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()