import cv2
#import numpy as np
image=cv2.imread("ss.jpg",cv2.IMREAD_GRAYSCALE)
edge=cv2.Canny(image,threshold1=100,threshold2=80)
cv2.imshow("image",image)
cv2.imshow("edge",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()