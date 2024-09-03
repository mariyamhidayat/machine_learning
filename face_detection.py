import cv2
import numpy as np
cap=cv2.VideoCapture(0)
'''  A Haar Cascade is basically a classifier which is used to
  detect the object for which it has been trained for, from the source. 
''' 
# haar cascade classifer which is used to superviesd learning 
 
face=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
while True:
    ret,frame=cap.read()
     #convert image into gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # use detectmultiscale function for detection 
    faces=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        #r=cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
         #We pass slice instead of index like this: [start:end].
       # roi_gray=gray[y:y+h,x:x+w]
        #color=frame[y:y+h,x:x+w]


    cv2.imshow("face",frame)
    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

