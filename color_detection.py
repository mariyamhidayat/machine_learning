import cv2
import numpy as np
cp=cv2.VideoCapture(0)
while True:
    rat,frame=cp.read()
    widt=int(cp.get(5))
    height=int(cp.get(6))
    #cvt function convrt the color BGRtoHSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower=np.array([89,50,50])
    higher=np.array([110,204,255])
    mask=cv2.inRange(hsv,lower,higher)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',result)
    if cv2.waitKey(1)==ord('q'):
        break
cp.release()
cv2.destroyAllWindows()
