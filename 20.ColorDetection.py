import cv2
import numpy as np

frame = cv2.imread("./assets/color_balls.jpg")

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    u_v = np.array([130, 235, 235])
    l_v = np.array([110, 60, 60])

    mask = cv2.inRange(hsv, l_v, u_v)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
