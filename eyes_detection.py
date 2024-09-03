import cv2
cap=cv2.VideoCapture(0)
eye=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    #use detectmultiscale function
    eyes=eye.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('eyes_detection',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
