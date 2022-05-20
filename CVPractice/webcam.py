import numpy as np
import cv2


#calibration
def calibration(saveName):
    cap = cv2.VideoCapture(1)


    while(True):
        ret, frame = cap.read() # return a single frame in variable `frame`
        cv2.imshow('img1', frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv2.imwrite(saveName, frame)
            cv2.destroyAllWindows()
            break

    cap.release()




cap = cv2.VideoCapture(1)

calibration('defaultView')
calibration('desiredView')

while True:
    ret, frame = cap.read()
    cv2.imshow('Input', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
