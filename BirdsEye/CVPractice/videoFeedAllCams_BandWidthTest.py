import numpy as np
import cv2
import time

frontIndex = 0
leftIndex = 3
backIndex = 2
rightIndex = 1

capFront = cv2.VideoCapture(frontIndex)
capLeft = cv2.VideoCapture(leftIndex)
capBack = cv2.VideoCapture(backIndex)
capRight = cv2.VideoCapture(rightIndex)


pTime = 0
i = 0
fpsAvg = 0
while True:
    
    i+=1

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    ret, frame = capBack.read()
    x = capFront.read()
    # time.sleep(0.1)
    y = capRight.read()
    z = capLeft.read()
    # time.sleep(0.1)
    print(x[0], y[0], z[0])
    
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    cv2.imshow('Live Feed of Cam#: ' + str(backIndex), frame)
    
    fpsAvg += fps
    if cv2.waitKey(1) == ord('q'):
        print(int(fpsAvg/i))
        break