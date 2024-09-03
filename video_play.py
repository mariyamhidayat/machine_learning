import cv2
from ffpyplayer.player import MediaPlayer# this library use add sound

cap=cv2.VideoCapture('C:\\Users\\Swan Computers\\.vscode\\extensions\\video.mp4')
# also add the sound in video
player=MediaPlayer('C:\\Users\\Swan Computers\\.vscode\\extensions\\video.mp4')
if(cap.isOpened==False):
    print("video cannot open please check the error ")
while(cap.isOpened):
    ret,frame=cap.read()
    audio_frame,val=player.get_frame()
    if ret==True:
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(25)==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()




