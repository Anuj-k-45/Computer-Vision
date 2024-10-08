import cv2

img1 = cv2.imread("./assets/image.jpg",0)
img1 = cv2.resize(img1, (1280, 700))
print(f"Pixels of gray-scale image :\n{img1}")
cv2.imshow("Grey scale image", img1)
 
img2 = cv2.imread("./assets/image.jpg",1)     # 1 stands for 3 channel image, 0 stands for single channel image
img2 = cv2.resize(img2, (1280, 700))
print(f"Pixels of original image :\n{img2}")
cv2.imshow("Original image", img2)

img3 = cv2.imread("./assets/image.jpg",-1)    # -1 increases the saturation
img3 = cv2.resize(img3, (1280, 700))
print(f"Pixels of unchanged image:\n{img3}")
# cv2.flip(img1, -1)   #flips the image, values can be : (-1,0,1)
cv2.imshow("Unchanged image", img3)

cv2.waitKey(3000)   #wait for 3 seconds
cv2.destroyAllWindows()