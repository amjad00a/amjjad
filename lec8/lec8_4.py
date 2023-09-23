import cv2
cam=cv2.VideoCapture(0)
classifair=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classifair_1=cv2.CascadeClassifier("haarcascade_eye.xml")
while True:
    _,frame=cam.read()
    eye = classifair_1.detectMultiScale(frame)
    faces=classifair.detectMultiScale(frame)
    for (x, y, h, w) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    for (x, y, h, w) in eye:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv2.imshow("image_", frame)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()