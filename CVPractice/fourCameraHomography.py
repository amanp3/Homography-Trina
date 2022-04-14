#Aman Penmetcha
#Written for AVATRINA,  Feb 2022
#Code to generate 360 Birds eye of TRINA surrounding using 4 usb cameras

import numpy as np
import cv2
import time

##########
#this function takes the file name as a string eg: rightCamDesired.png and which camera: 1, 3, 5, or 7 and
#stores a image to later calculate homography with
def takePicture(fileName, camNumber):
    cap = cv2.VideoCapture(camNumber) #choose which camera
    while(True):
        ret, frame = cap.read() # return a single frame in variable `frame`
        cv2.imshow('Take Picture for: ' + fileName + '||| y for take picture q for dont take picture', frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv2.imwrite(fileName, frame)
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(1) == ord('q'): #dont save the picture on pressing 'q'
            print('No picture taken')
            cv2.destroyAllWindows()
            break

    cap.release()
#######################################

def calibrate():
    #taking pics for the gram 
    takePicture('frontCamDesired.png', 0) 
    takePicture('frontCamActual.png', 0) 
    takePicture('rightCamDesired.png', 3) 
    takePicture('rightCamActual.png', 3) 
    takePicture('leftCamDesired.png', 1)
    takePicture('leftCamActual.png', 1)
    #takePicture('backCamDesired.png', 5)
    #takePicture('backCamDesired.png', 5)
#################


#comment out calibrate line below if you want to skip calibration 
#if not commented you can still skip taking pictures but you will have to press q 8 times
calibrate()

pathFrontCamActual = r'C:\Users\Aman\Desktop\School\Python\frontCamActual.png'
pathFrontCamDesired = r'C:\Users\Aman\Desktop\School\Python\frontCamDesired.png'
pathRightCamActual = r'C:\Users\Aman\Desktop\School\Python\rightCamActual.png'
pathRightCamDesired = r'C:\Users\Aman\Desktop\School\Python\rightCamDesired.png'
pathLeftCamActual = r'C:\Users\Aman\Desktop\School\Python\leftCamActual.png'
pathLeftCamDesired = r'C:\Users\Aman\Desktop\School\Python\leftCamDesired.png'


frontActual = cv2.imread(pathFrontCamActual)
frontDesired = cv2.imread(pathFrontCamDesired)
rightActual = cv2.imread(pathRightCamActual)
rightDesired = cv2.imread(pathRightCamDesired)
leftActual = cv2.imread(pathLeftCamActual)
leftDesired = cv2.imread(pathLeftCamDesired)

t = time.time()

#patternSize stores the size of the chessboard you are looking for
patternSize = (8,6)


retFA, cornersFrontActual = cv2.findChessboardCorners(frontActual, patternSize)
retFD, cornersFrontDesired = cv2.findChessboardCorners(frontDesired, patternSize)
retRA, cornersRightActual = cv2.findChessboardCorners(rightActual, patternSize)
retRD, cornersRightDesired = cv2.findChessboardCorners(rightDesired, patternSize)
retLA, cornersLeftActual = cv2.findChessboardCorners(leftActual, patternSize)
retLD, cornersLeftDesired = cv2.findChessboardCorners(leftDesired, patternSize)

Hfront, _1 = cv2.findHomography(cornersFrontActual, cornersFrontDesired)
Hright, _2 = cv2.findHomography(cornersRightActual, cornersRightDesired)
Hleft, _3 = cv2.findHomography(cornersLeftActual, cornersLeftDesired)

capFront = cv2.VideoCapture(0)
capRight = cv2.VideoCapture(3)
capLeft = cv2.VideoCapture(1)

pTime = 0
while True:
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    ret, frameFront = capFront.read()
    frontCam_warp = cv2.warpPerspective(frameFront, Hfront, (frontActual.shape[1], frontActual.shape[0]))
    cv2.putText(frontCam_warp, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    #cv2.imshow('Front Cam Warped | q for exit', frontCam_warp)
    cv2.resize(frontCam_warp, (0,0), fx=0.5, fy =0.5)

    ret, frameRight = capRight.read()
    rightCam_warp = cv2.warpPerspective(frameRight, Hright, (rightActual.shape[1], rightActual.shape[0]))
    cv2.putText(rightCam_warp, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    #cv2.imshow('Right Cam Warped | q for exit', rightCam_warp)
    cv2.resize(rightCam_warp, (0,0), fx=0.5, fy =0.5)

    ret, frameLeft = capLeft.read()
    leftCam_warp = cv2.warpPerspective(frameLeft, Hleft, (leftActual.shape[1], leftActual.shape[0]))
    cv2.putText(leftCam_warp, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    #cv2.imshow('Left Cam Warped | q for exit', leftCam_warp)
    cv2.resize(leftCam_warp, (0,0), fx=0.5, fy =0.5)

    #np.concatenate()

    if cv2.waitKey(1) == ord('q'):
        print(fps)
        cv2.destroyAllWindows()
        break