import numpy as np
import cv2

def calibration():
    path1 = r'C:\Users\Aman\Desktop\TRINA\OPENCV\source.jpg'
    path2 = r'C:\Users\Aman\Desktop\TRINA\OPENCV\desired.jpg'

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #patternSize stores the size of the chessboard you are looking for
    patternSize = (9,6)

    ret1, corners1 = cv2.findChessboardCorners(img1, patternSize)
    ret2, corners2 = cv2.findChessboardCorners(img2, patternSize)

    H, _ = cv2.findHomography(corners1, corners2)
    return H
    #print(H)





#img1_warp = cv2.warpPerspective(img1, H, (img1.shape[1], img1.shape[0]))




#cv2.imshow('Original', img1)
#cv2.imshow('Window', img1_warp)
#cv2.waitKey(0)
#cv2.destroyAllWindows()