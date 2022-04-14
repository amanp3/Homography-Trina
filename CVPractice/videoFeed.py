import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
#cap2 = cv2.VideoCapture(3)

pTime = 0
while True:
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    ret, frame = cap.read()
    
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    cv2.imshow('Warped Image', frame)


    if cv2.waitKey(1) == ord('q'):
        print(fps)
        break