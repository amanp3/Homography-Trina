#from:
#https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

#adated for:
#360 birds eye camera calibration by Aman Penmetcha
# #Calibrate the intrinsics of a camera using a chess board.

import numpy as np
import cv2
import glob
import time

#EDIT LINE 22 FOR THE PROPER FILE PATH DEPENDING ON WHERE IMAGES ARE STORED

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob(r'C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\BackCamera\*.png')
#type(cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\BackCamera\*.png'))
print(len(images), images)
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (8,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (8,6), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(100)
        print(img.shape)
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

#img = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\TRINA\rightStitchingImage.png')
print(img.shape)
img = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\BackCamera\distortedImg5.png')
h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

print(mtx)
print(dist)
print(newcameramtx)
print(roi)
# np.save(r'C:\Users\Aman\Desktop\School\Python\TRINA\IntrinsicsData\backMtx', mtx)
# np.save(r'C:\Users\Aman\Desktop\School\Python\TRINA\IntrinsicsData\backDist', dist)
# np.save(r'C:\Users\Aman\Desktop\School\Python\TRINA\IntrinsicsData\backNewCameraMatrix', newcameramtx)
# np.save(r'C:\Users\Aman\Desktop\School\Python\TRINA\IntrinsicsData\backROI', roi)
#left, front, right, back
t = time.time()


# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
t2 = time.time()
print("RUNTIME to UNDISTORT: ", t2-t)

cv2.imshow('og image', img)
cv2.imshow('calibration result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

