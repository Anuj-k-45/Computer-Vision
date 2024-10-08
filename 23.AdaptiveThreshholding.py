import cv2
import numpy as np

img = cv2.imread("./assets/page.jpg", 0)
img = cv2.resize(img, (400, 400))
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
# cv2.adaptiveThreshhold(image, max value, type of adaptive thresholding, x such that x*x block to consider as smallest region for mean, value of c(constant to minus))

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)


cv2.imshow("image", img)
cv2.imshow("img", th1)
cv2.imshow("adaptive Mean", th2)
cv2.imshow("adaptive Gaussian", th3)


cv2.waitKey(0)
cv2.destroyAllWindows()