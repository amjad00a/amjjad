import cv2
import numpy as np
image=cv2.imread("ss.jpg",cv2.IMREAD_GRAYSCALE)
filter=np.ones((5,5))
filter=filter/np.sum(filter)
filterd_image=cv2.filter2D(image,-1,filter)
cv2.imshow("image",image)
cv2.imshow("filterd_image",filterd_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
