import cv2
image=cv2.imread("ss.jpg")
classifair=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=classifair.detectMultiScale(image)
for (x,y,h,w) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv2.imshow("ff",image)
cv2.waitKey(0)
cv2.destroyAllWindows()