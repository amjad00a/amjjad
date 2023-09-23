import cv2
image=cv2.imread("ss.jpg")
line=cv2.line(image,(100,100),(100,200),(0,0,250),3)
rectangle=cv2.rectangle(image,(100,100),(220,280),(0,255,0),1)
circle=cv2.circle(image,(150,150),70,(255,255,0),2)
cv2.imshow("line",line)
cv2.imshow("circle",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()
