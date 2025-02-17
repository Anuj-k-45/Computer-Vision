import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")

cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 180, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)

cv2.createTrackbar("Upper_H", "Color Adjustments", 180, 180, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")

    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")

    u_v = np.array([u_h, u_s, u_v])
    l_v = np.array([l_h, l_s, l_v])

    mask = cv2.inRange(hsv, l_v, u_v)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
