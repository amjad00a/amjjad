import cv2
import numpy as np
image_1=cv2.imread("ss.jpg")
cv2.imshow("image",image_1)
image=cv2.cvtColor(image_1,cv2.COLOR_BGR2RGB)
Sobel_x=cv2.Sobel(image,-1,1,0,ksize=3)
cv2.imshow("sobel_x",Sobel_x)
Sobel_y=cv2.Sobel(image,-1,0,1,ksize=3)
cv2.imshow("sobel_y",Sobel_y)
final_image=np.abs(Sobel_x)+np.abs(Sobel_y)
cv2.imshow("final_image",final_image)
Canny_edge=cv2.Canny(image_1,threshold1=150,threshold2=250)
cv2.imshow("Canny_edge",Canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()