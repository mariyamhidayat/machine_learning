import cv2
from ultralytics import YOLO
cap=cv2.VideoCapture("C:\\Users\\Swan Computers\\.vscode\extensions\\vehicle.MP4")
model = YOLO('yolov8n-seg.pt')## Load your model
if cap.isOpened==False:
    print("erre")
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        #run detection
        result=model(frame)
        #visubale result on the frame 
        an_frame=result[0].plot()# which create the rectangle in object and show in list
        #display frame
        cv2.imshow('real_object',an_frame)
        if cv2.waitKey(1)==ord('q'):

            break
    else:
        break
cap.release()
cv2.destroyAllWindows()