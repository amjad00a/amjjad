import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("ss.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("i",image)
hist=cv2.calcHist([image],[0],None,[300],ranges=[0,300])
image_2=cv2.equalizeHist(image)
hist=cv2.calcHist([image],[0],None,[300],ranges=[0,300])
cv2.imshow("figure",image_2)
cv2.imshow("figure_1",image)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
