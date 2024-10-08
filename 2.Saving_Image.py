import cv2

path = input("Enter the path of the image : ")
img1 = cv2.imread(path,0)
img1 = cv2.resize(img1, (1280,750))

cv2.imshow("The image", img1)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("./assets/saved_gray_scale.png", img1)

else:
    cv2.destroyAllWindows()