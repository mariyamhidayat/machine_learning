import cv2
from ultralytics import YOLO
cap=cv2.VideoCapture(0)
model=YOLO('yolov8n-seg.pt')
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        # run detection
        result=model(frame)
        #visualization 
        an_result=result[0].plot()
        #display
        cv2.imshow('frame',an_result)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()