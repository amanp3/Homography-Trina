import numpy as np
import cv2
import time

camIndex = 3

cap = cv2.VideoCapture(camIndex)


pTime = 0
i = 0
fpsAvg = 0
while True:
    i+=1

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    ret, frame = cap.read()
    
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    cv2.imshow('Live Feed of Cam#: ' + str(camIndex), frame)
    
    fpsAvg += fps
    if cv2.waitKey(1) == ord('q'):
        print(int(fpsAvg/i))
        break