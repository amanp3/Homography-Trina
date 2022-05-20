#working
import numpy as np
import cv2
import time

path1 = r'C:\Users\Aman\Desktop\School\Python\defaultTest.png'
path2 = r'C:\Users\Aman\Desktop\School\Python\desiredTest.png'
t = time.time()
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)



#patternSize stores the size of the chessboard you are looking for
patternSize = (8,6)

ret1, corners1 = cv2.findChessboardCorners(img1, patternSize)
ret2, corners2 = cv2.findChessboardCorners(img2, patternSize)



H, _ = cv2.findHomography(corners1, corners2)

#print(H)
#print("This took {:.9f} seconds".format(time.time() - t))

#t = time.time()


#print("This took {:.9f} seconds".format(time.time() - t))

cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(3)

pTime = 0
while True:
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    ret, frame = cap.read()
    img1_warp = cv2.warpPerspective(frame, H, (img1.shape[1], img1.shape[0]))
    cv2.putText(img1_warp, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    cv2.imshow('Warped Image', img1_warp)


    if cv2.waitKey(1) == ord('q'):
        print(fps)
        break

