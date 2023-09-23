import cv2
import numpy as np
image=cv2.imread("aa.jpg")
print(image.shape)
cv2.imshow("image_1",image)
resized_image=cv2.resize(image,(600,300))
croped=image[0:256,0:256]
gray=cv2.cvtColor(croped,cv2.COLOR_BGR2GRAY)
num,thrshold2=cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
#cv2.imshow("gray",gray)
#cv2.imshow("resized",resized_image)
#cv2.imshow("croped",croped)
#cv2.imwrite("resized.jpg",resized_image)
#cv2.imwrite("croped.jpg",croped)
thrshold=np.zeros(gray.shape)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i,j]<128:
            thrshold[i,j]=0
        else:
            thrshold[i,j]=1
cv2.imshow("thrshold",thrshold)
cv2.imshow("thrshold_2",thrshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()
