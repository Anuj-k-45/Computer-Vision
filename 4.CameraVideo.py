import cv2

clip = cv2.VideoCapture(0)
print(clip)

# Saving a video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("./assets/output.avi", fourcc, 20.0, (640,480), 0)
#4 parameters named : name, codec, fps, resolution, if grascale then pass 0 else not at the end

while clip.isOpened():
    ret, frame = clip.read()
    if ret==True:
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera", frame)
        cv2.imshow("Gray", gray)
        output.write(gray)
        k = cv2.waitKey(1)
        
        if k==ord("q"):
            break

clip.release()
output.release()
cv2.destroyAllWindows()
