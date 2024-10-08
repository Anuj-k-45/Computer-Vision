import cv2
import numpy as np

img = cv2.imread("./assets/col_balls.jpg", 0)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((2, 2), np.uint8)
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
c = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)


cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("kernal", kernal)
cv2.imshow("opening", o)
cv2.imshow("closing", c)

cv2.waitKey(0)
cv2.destroyAllWindows()

x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)   #diff b/w mask and opening
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal)  
cv2.imshow("TopHat",x1) 
cv2.imshow("Gradient",x2) 
cv2.imshow("BlackHat",x3) 
cv2.waitKey(0)
cv2.destroyAllWindows()
