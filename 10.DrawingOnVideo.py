import cv2
import datetime

clip = cv2.VideoCapture("./assets/video.mp4")

while(clip.isOpened()):
    ret, frame = clip.read()
    if ret==True:
        frame = cv2.resize(frame, (1400,800))
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = "Height : " + str(clip.get(4)) + "Width : " + str(clip.get(3))

        frame=cv2.line(frame, (0,0), (700,400), (34,34,124), 20)
        
        date_data = "Date : " + str(datetime.datetime.now())
        frame=cv2.putText(frame, date_data, (10,50), font, 1, (100,255,255), 1, cv2.LINE_AA)

        frame=cv2.putText(frame, text, (10,20), font, 1, (0,155,255), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break

clip.release()
cv2.destroyAllWindows()