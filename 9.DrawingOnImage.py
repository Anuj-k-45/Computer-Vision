import numpy as np
import cv2

img = cv2.imread("./assets/image.jpg")
img = cv2.resize(img, (700,400))

img = cv2.line(img, (0,0), (700,400), (154,92,424), 10)  #(image, start(cordinate), end(cordinate), (B, G, R), thickness)
img = cv2.line(img, (350,0), (350,400), (154,0,67), 5)
img = cv2.line(img, (0,200), (700,200), (6,0,307), 1)

img = cv2.arrowedLine(img, (0,56), (105, 347), (9,18,109), 5) #same as line

img = cv2.rectangle(img, (150,150), (250,300), (100, 20, 30), 15) #same as line

img = cv2.rectangle(img, (550,250), (690,300), (1, 20, 200), -1) # negetive thinckness will fill the shape with the color

img = cv2.circle(img, (100,100), 100, (19, 300, 40), 3) #(image, center(cordinates), raidus, (B, G, R), thickness)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Avengers", (470, 380), font, 1, (0,125,255), 3, cv2.LINE_AA) #(image, "text", start(cordinate), font, size, (B, G, R), thickness, format)

img = cv2.ellipse(img, (400,300), (100,50), 0, 0, 360, 155, 20)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()