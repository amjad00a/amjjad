import cv2
image=cv2.imread("ss.jpg")
image_2=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("image_1",image)
cv2.imshow("image_2",image_2)
cv2.imwrite("image_2.jpg",image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()