import cv2
import numpy as np

img = cv2.imread("./assets/noisy.jpg")
img = cv2.resize(img, (600, 400))
kernal = np.ones((5, 5), np.float32)/25

h_filter = cv2.filter2D(img, -1, kernal)    #homogenous filter/highpass filter
cv2.imshow("homogenous", h_filter)


blur = cv2.blur(img, (8,8))    
cv2.imshow("blur", blur)

gauss = cv2.GaussianBlur(img, (5,5), 0)   
cv2.imshow("gauss", gauss)

median = cv2.medianBlur(img, 5)   #works best for salt and pepper noise
cv2.imshow("median", median)

bilat = cv2.bilateralFilter(img, 9, 75, 75)     #best among all
cv2.imshow("bilat", bilat)

cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

