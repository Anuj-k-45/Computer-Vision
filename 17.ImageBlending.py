import cv2
import numpy as np

img1 = cv2.imread("./assets/roi_opr.jpg")
img2 = cv2.imread("./assets/bro_thor.jpg")

img1 = cv2.resize(img1, (500,700))
cv2.imshow("img1", img1)

img2 = cv2.resize(img2, (500,700))
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

result = img1 + img2
cv2.imshow("Addition", result)

cv2.waitKey(0)
cv2.destroyAllWindows() 

result = cv2.add(img1, img2)
cv2.imshow("Blend", result)
cv2.waitKey(0)
cv2.destroyAllWindows() 

result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow("Blend manually", result)

cv2.waitKey(0)
cv2.destroyAllWindows() 