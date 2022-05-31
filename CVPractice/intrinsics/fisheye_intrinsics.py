"""fisheye_intrinsics.py
Calibrate the intrinsics of a fisheye camera using the chess board poster.
Based on the code available at
https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html

Fisheye specific documentation at
https://docs.opencv.org/3.4/db/d58/group__calib3d__fisheye.html

Typically, to calibrate camera intrinsics, collect a set of images using
the sensor module and logger with the chess board poster in lab. A pdf of
such a board is available at
http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration?action=AttachFile&do=view&target=check-108.pdf
"""
#Patrick Naughton

import argparse
import numpy as np
import cv2 as cv
import glob
import json
import pickle
import math
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Calibrate the intrinsics of a "
    + "camera using the chess board poster")
parser.add_argument("path", type=str, help="directory containing the "
    + "calibration images")
parser.add_argument("--width", type=int, default=8, help="width of the chess "
    + "board, number of lattice points inside the border of outer squares")
parser.add_argument("--height", type=int, default=6, help="height of the chess "
    + "board, counted same way as width")
parser.add_argument("-m", type=int, default=300, help="maximum number of "
    + "images to use for calibration")
parser.add_argument("-o", type=str, default="fisheye_intrinsics.json",
    help="name of output file")
parser.add_argument("-s", type=int, default=0, help="index of image in "
    + "directory to start with")
parser.add_argument("-d", action="store_true", help="debug mode, show "
    + "detected chess boards")
parser.add_argument("--skip", action="store_true", help="skip image "
    + "extraction, use cached data")
args = parser.parse_args()

cache_name = "tmp_data_fisheye.p"
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
width = args.width
height = args.height
max_imgs = args.m
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((width*height,3), np.float32)
objp[:,:2] = np.mgrid[0:width,0:height].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = sorted(glob.glob(f'{args.path}/*.jpg'))
size_img = cv.imread(images[0])
h, w, _ = size_img.shape
if not args.skip:
    for i, fname in tqdm(enumerate(images)):
        if i < args.s: continue
        if len(objpoints) >= max_imgs:
            break
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (width,height), None)
        # If found, add object points, image points (after refining them)
        if ret == True:
            print(fname)
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
            if args.d:
                # Draw and display the corners
                cv.drawChessboardCorners(img, (width, height), corners2, ret)
                cv.imshow('img', img)
                cv.waitKey(0)
    if args.d:
        cv.destroyAllWindows()
    print(f"Found {len(objpoints)} good images")
    with open(cache_name, "wb") as tmp_file:
        data = (objpoints, imgpoints)
        pickle.dump(data, tmp_file)

with open(cache_name, "rb") as tmp_file:
    data = pickle.load(tmp_file)
objpoints, imgpoints = data
# print(imgpoints[0][0])
# import sys
# sys.exit()
# print(len(imgpoints[0][0]), len(objpoints[0][0]))
objpoints = np.array(objpoints).reshape(-1, 1, args.width * args.height, 3)
imgpoints = np.array(imgpoints).reshape(-1, 1, args.width * args.height, 2)
# print("objpoints type: ", type(objpoints[0][0]), objpoints[0][0].dtype, len(objpoints))
# Need to provid initial guess or reprojection error tends to underflow and throw
# an exception when using a lot of images.
init_guess_k = np.array([
		[
			576.0743577139923,
			0.5931023625824208,
			717.844655777735
		],
		[
			0.0,
			574.131115448492,
			498.97429782817335
		],
		[
			0.0,
			0.0,
			1.0
		]
	])
init_guess_d = np.array([
		[
			0.015251217702431076
		],
		[
			-0.016425504507470053
		],
		[
			0.016744459318658807
		],
		[
			-0.0041324141773697925
		]
	])
print("starting calibration")
rms, mtx, dist, rvecs, tvecs = cv.fisheye.calibrate(objpoints, imgpoints,
    (w, h), init_guess_k, init_guess_d,
    flags=cv.fisheye.CALIB_RECOMPUTE_EXTRINSIC | cv.CALIB_USE_INTRINSIC_GUESS)
save = {"matrix": mtx.tolist(), "distortion": dist.tolist()}
save["rms"] = rms

mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.fisheye.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/imgpoints2.shape[1]
    mean_error += error
save["mean_error"] = mean_error / len(objpoints)

# FoV computations (found in radians)
fx = mtx[0,0]
fy = mtx[1,1]
fovx = 2 * math.atan(w / (2 * fx))
fovy = 2 * math.atan(h / (2 * fy))
save["fovx"] = fovx
save["fovy"] = fovy

print(save)
with open(args.o, "wb") as int_f:
    pickle.dump(save, int_f)
print("Ending calibration")
with open(args.o, "w") as int_f:
    json.dump(save, int_f, indent="\t")
