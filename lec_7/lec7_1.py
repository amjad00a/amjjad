import cv2
import numpy as np

filter=np.array([
    [-1,0,1],
    [-2,0,2],
    [-1, 0, 1],

])
filter_2=np.array([
    [-1,0,1],
    [-2,0,2],
    [-1, 0, 1],
])
image=cv2.imread("chess_bord.png")
filterd_image=cv2.filter2D(image,-1,filter)
filterd_image2=cv2.filter2D(image,-1,filter_2)
print(filterd_image.max(),filterd_image.min())
final_image=filterd_image+filterd_image2
cv2.imshow("image",image)
cv2.imshow("filterd_image",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()