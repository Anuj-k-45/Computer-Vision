import cv2
import numpy as np

img = cv2.imread("./assets/pikachu.jpg")
img = cv2.resize(img, (480, 800))

print(img.shape)
print(img.size)
print(type(img))
print(img.dtype)

b, g, r = cv2.split(img)

cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
