import cv2
import numpy as np

img1 = cv2.imread("./assets/hero1.jpg")
img2 = cv2.imread("./assets/strom_breaker.jpg")

img1 = cv2.resize(img1, (1024, 650))
img2 = cv2.resize(img2, (600, 650))

r, c, ch = img2.shape

roi = img1[0:r, 0:c]

img_gry = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

res = cv2.add(img1_bg, img2_fg)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("res", res)

final = img1

final[0:r, 0:c] = res

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()