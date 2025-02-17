import cv2
import pyautogui as p
import numpy as np

rs = p.size()
fn = input("Please enter the path to save : ")
fps=60.0
fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter(fn, fourcc, fps, rs)

cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording", (600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording", f)
    if cv2.waitKey(1) == ord("q"):
        break
output.release()
cv2.destroyAllWindows()