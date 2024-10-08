import cv2

camera = "http://192.168.100.31:8080/video"
clip = cv2.VideoCapture(0)
clip.open(camera)
print(clip)

while True:
    ret, frame = clip.read()

    if ret==True:
        frame = cv2.resize(frame, (820,450))
        cv2.imshow("frame", frame)

        k = cv2.waitKey(1)
        if k == ord("q"):
            break

clip.release()
cv2.destroyAllWindows()