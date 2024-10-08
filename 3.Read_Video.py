import cv2

clip = cv2.VideoCapture("./assets/video.mp4")
print(clip)

while True:
    ret, frame = clip.read()

    frame = cv2.resize(frame, (820,450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #to convert video into gray scale

    cv2.imshow("frame", frame)
    cv2.imshow("Gray Scale", gray)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

clip.release()
cv2.destroyAllWindows()