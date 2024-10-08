import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (150, 100), (200, 250), (255, 255, 255), -1)

img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2, (10, 10), (170, 190), (255, 255, 255), -1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Bitwise And
bitAnd = cv2.bitwise_and(img1, img2)
cv2.imshow("BitAnd", bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Bitwise Or
bitOr = cv2.bitwise_or(img1, img2)
cv2.imshow("BitOr", bitOr)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Bitwise Not
bitNot = cv2.bitwise_not(img1)
cv2.imshow("BitNot", bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Bitwise Xor
bitXor = cv2.bitwise_xor(img1, img2)
cv2.imshow("BitXor", bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()


