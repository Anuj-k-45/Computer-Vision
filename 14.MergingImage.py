import cv2
import numpy as np

img = cv2.imread("./assets/pikachu.jpg")
img = cv2.resize(img, (480, 800))

print(img.shape)
print(img.size)
print(type(img))
print(img.dtype)

b, g, r = cv2.split(img)

mr1 = cv2.merge((b, g, r))
cv2.imshow("rgb", mr1)

cv2.waitKey(0)
cv2.destroyAllWindows()
