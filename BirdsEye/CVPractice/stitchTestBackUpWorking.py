#Aman Penmetcha
#Written for AVATRINA,  Feb 2022
#Code to generate 360 Birds eye of TRINA surrounding using 4 usb cameras

import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import io
import imutils
cv2.ocl.setUseOpenCL(False)

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
    takePicture('frontCamDesired.png', 3) 
    takePicture('frontCamActual.png', 3) 
    #takePicture('rightCamDesired.png', 3) 
    #takePicture('rightCamActual.png', 3) 
    takePicture('leftCamDesired.png', 1)
    takePicture('leftCamActual.png', 1)
    #takePicture('backCamDesired.png', 5)
    #takePicture('backCamDesired.png', 5)

    takePicture('frontStitchingImage.png', 3)
    #takePicture('rightStitchingImage.png', 3)
    takePicture('leftStitchingImage.png', 1)
    #takePicture('backStitchingImage.png', 5)
#################

#functions for stitching below
def detectAndDescribe(image, method=None):
    """
    Compute key points and feature descriptors using an specific method
    """
    
    assert method is not None, "You need to define a feature detection method. Values are: 'sift', 'surf'"
    
    # detect and extract features from the image
    if method == 'sift':
        descriptor = cv2.xfeatures2d.SIFT_create()
    elif method == 'surf':
        descriptor = cv2.xfeatures2d.SURF_create()
    elif method == 'brisk':
        descriptor = cv2.BRISK_create()
    elif method == 'orb':
        descriptor = cv2.ORB_create()
        
    # get keypoints and descriptors
    (kps, features) = descriptor.detectAndCompute(image, None)
    
    return (kps, features)

def createMatcher(method,crossCheck):
    "Create and return a Matcher Object"
    
    if method == 'sift' or method == 'surf':
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=crossCheck)
    elif method == 'orb' or method == 'brisk':
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=crossCheck)
    return bf

def matchKeyPointsBF(featuresA, featuresB, method):
    bf = createMatcher(method, crossCheck=True)
        
    # Match descriptors.
    best_matches = bf.match(featuresA,featuresB)
    
    # Sort the features in order of distance.
    # The points with small distance (more similarity) are ordered first in the vector
    rawMatches = sorted(best_matches, key = lambda x:x.distance)
    print("Raw matches (Brute force):", len(rawMatches))
    return rawMatches

def matchKeyPointsKNN(featuresA, featuresB, ratio, method):
    bf = createMatcher(method, crossCheck=False)
    # compute the raw matches and initialize the list of actual matches
    rawMatches = bf.knnMatch(featuresA, featuresB, 2)
    print("Raw matches (knn):", len(rawMatches))
    matches = []

    # loop over the raw matches
    for m,n in rawMatches:
        # ensure the distance is within a certain ratio of each
        # other (i.e. Lowe's ratio test)
        if m.distance < n.distance * ratio:
            matches.append(m)
    return matches

def getHomography(kpsA, kpsB, featuresA, featuresB, matches, reprojThresh):
    # convert the keypoints to numpy arrays
    kpsA = np.float32([kp.pt for kp in kpsA])
    kpsB = np.float32([kp.pt for kp in kpsB])
    
    if len(matches) > 4:

        # construct the two sets of points
        ptsA = np.float32([kpsA[m.queryIdx] for m in matches])
        ptsB = np.float32([kpsB[m.trainIdx] for m in matches])
        
        # estimate the homography between the sets of points
        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
            reprojThresh)

        return (matches, H, status)
    else:
        return None

def get_img_from_fig(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

#comment out calibrate line below if you want to skip calibration 
#if not commented you can still skip taking pictures but you will have to press q 8 times

#calibrate()

pathFrontCamActual = r'C:\Users\Aman\Desktop\School\Python\frontCamActual.png'
pathFrontCamDesired = r'C:\Users\Aman\Desktop\School\Python\frontCamDesired.png'
#pathRightCamActual = r'C:\Users\Aman\Desktop\School\Python\rightCamActual.png'
#pathRightCamDesired = r'C:\Users\Aman\Desktop\School\Python\rightCamDesired.png'
pathLeftCamActual = r'C:\Users\Aman\Desktop\School\Python\leftCamActual.png'
pathLeftCamDesired = r'C:\Users\Aman\Desktop\School\Python\leftCamDesired.png'


frontActual = cv2.imread(pathFrontCamActual)
frontDesired = cv2.imread(pathFrontCamDesired)
#rightActual = cv2.imread(pathRightCamActual)
#rightDesired = cv2.imread(pathRightCamDesired)
leftActual = cv2.imread(pathLeftCamActual)
leftDesired = cv2.imread(pathLeftCamDesired)

t = time.time()

#patternSize stores the size of the chessboard you are looking for
patternSize = (8,6)


retFA, cornersFrontActual = cv2.findChessboardCorners(frontActual, patternSize)
retFD, cornersFrontDesired = cv2.findChessboardCorners(frontDesired, patternSize)
#retRA, cornersRightActual = cv2.findChessboardCorners(rightActual, patternSize)
#retRD, cornersRightDesired = cv2.findChessboardCorners(rightDesired, patternSize)
retLA, cornersLeftActual = cv2.findChessboardCorners(leftActual, patternSize)
retLD, cornersLeftDesired = cv2.findChessboardCorners(leftDesired, patternSize)

Hfront, _1 = cv2.findHomography(cornersFrontActual, cornersFrontDesired)
#Hright, _2 = cv2.findHomography(cornersRightActual, cornersRightDesired)
Hleft, _3 = cv2.findHomography(cornersLeftActual, cornersLeftDesired)

# imgTemp1 = cv2.warpPerspective(cv2.imread(r'C:\Users\Aman\Desktop\School\Python\frontStitchingImage.png'), Hfront, (frontActual.shape[1], frontActual.shape[0]))
# cv2.imwrite('frontStitchingImageWarped.png', imgTemp1)
# imgTemp2 = cv2.warpPerspective(cv2.imread(r'C:\Users\Aman\Desktop\School\Python\leftStitchingImage.png'), Hleft, (frontActual.shape[1], frontActual.shape[0]))
# cv2.imwrite('leftStitchingImageWarped.png', imgTemp2)
# print("Done")
# cv2.imshow('Front Cam Warped', frontCam_warp)
# cv2.imshow('Right Cam Warped', rightCam_warp)
# cv2.imshow('Left Cam Warped', leftCam_warp)

#stitching starts here
feature_extractor = 'orb' # one of 'sift', 'surf', 'brisk', 'orb'
feature_matching = 'bf'

frontStitchImage = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\panoTest1.png')
#frontStitchImage_gray = cv2.cvtColor(frontStitchImage, cv2.COLOR_RGB2GRAY)

leftStitchImage = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\panoTest2.png')
#leftStitchImage_gray = cv2.cvtColor(leftStitchImage, cv2.COLOR_RGB2GRAY)


#frontCam_warp = cv2.warpPerspective(frontStitchImage, Hfront, (frontActual.shape[1], frontActual.shape[0]))
#rightCam_warp = cv2.warpPerspective(rightActual, Hright, (rightActual.shape[1], rightActual.shape[0]))
#leftCam_warp = cv2.warpPerspective(leftStitchImage, Hleft, (leftActual.shape[1], leftActual.shape[0]))

#circumvents top down homography for debugging
frontCam_warp = frontStitchImage
leftCam_warp = leftStitchImage

frontCam_warp_gray = cv2.cvtColor(frontCam_warp, cv2.COLOR_RGB2GRAY)
leftCam_warp_gray = cv2.cvtColor(leftCam_warp, cv2.COLOR_RGB2GRAY)



#rightStitchImg = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\rightStitchingImage.png')
#rightStitchImage = cv2.cvtColor(rightStitchImg, cv2.COLOR_RGB2GRAY)

# backStitchImg = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\backStitchingImage.png')
# backStitchImage = cv2.cvtColor(backStitchImg, cv2.COLOR_RGB2GRAY)

kpsA, featuresA = detectAndDescribe(frontCam_warp_gray, method=feature_extractor)
kpsB, featuresB = detectAndDescribe(leftCam_warp_gray, method=feature_extractor)

# display the keypoints and features detected on both images
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,8), constrained_layout=False)
ax1.imshow(cv2.drawKeypoints(frontCam_warp,kpsA,None,color=(0,255,0)))
ax1.set_xlabel("(a)", fontsize=14)
ax2.imshow(cv2.drawKeypoints(leftCam_warp,kpsB,None,color=(0,255,0)))
ax2.set_xlabel("(b)", fontsize=14)
plt.show()

if feature_matching == 'bf':
    matches = matchKeyPointsBF(featuresA, featuresB, method=feature_extractor)
    img3 = cv2.drawMatches(frontCam_warp,kpsA,leftCam_warp,kpsB,matches[:100],
                           None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
elif feature_matching == 'knn':
    matches = matchKeyPointsKNN(featuresA, featuresB, ratio=0.75, method=feature_extractor)
    img3 = cv2.drawMatches(frontCam_warp,kpsA,leftCam_warp,kpsB,np.random.choice(matches,100),
                           None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3)
plt.show()

M = getHomography(kpsA, kpsB, featuresA, featuresB, matches, reprojThresh=4)
if M is None:
    print("Error!")
(matches, H, status) = M

# Apply panorama correction
# width = frontCam_warp.shape[1] + leftCam_warp.shape[1]
# height = frontCam_warp.shape[0] + leftCam_warp.shape[0]


# #while loop will start here

# result = cv2.warpPerspective(frontCam_warp, H, (width, height))
# result[0:leftCam_warp.shape[0], 0:leftCam_warp.shape[1]] = leftCam_warp

width = frontCam_warp.shape[1] + leftCam_warp.shape[1]
height = frontCam_warp.shape[0] + leftCam_warp.shape[0]

# t1 = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\stitch2.png')

# t2 = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\stitch1.png')




#while loop will start here

# cTime = time.time()
# fps = 1/(cTime - pTime)
# pTime = cTime

#frontCam_warp = cv2.warpPerspective(frontStitchImage, Hfront, (frontActual.shape[1], frontActual.shape[0]))
#rightCam_warp = cv2.warpPerspective(rightActual, Hright, (rightActual.shape[1], rightActual.shape[0]))
#leftCam_warp = cv2.warpPerspective(leftStitchImage, Hleft, (leftActual.shape[1], leftActual.shape[0]))

#
def warpTwoImages(img1, img2, H):
    '''warp img2 to img1 with homograph H'''
    h1,w1 = img1.shape[:2]
    h2,w2 = img2.shape[:2]
    pts1 = np.float32([[0,0],[0,h1],[w1,h1],[w1,0]]).reshape(-1,1,2)
    pts2 = np.float32([[0,0],[0,h2],[w2,h2],[w2,0]]).reshape(-1,1,2)
    pts2_ = cv2.perspectiveTransform(pts2, H)
    pts = np.concatenate((pts1, pts2_), axis=0)
    [xmin, ymin] = np.int32(pts.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(pts.max(axis=0).ravel() + 0.5)
    t = [-xmin,-ymin]
    Ht = np.array([[1,0,t[0]],[0,1,t[1]],[0,0,1]]) # translate

    result = cv2.warpPerspective(img2, Ht.dot(H), (xmax-xmin, ymax-ymin))
    result[t[1]:h1+t[1],t[0]:w1+t[0]] = img1
    return result

dst_pts = np.float32([np.kp1[m.queryIdx].pt for m in np.good]).reshape(-1,1,2)
src_pts = np.float32([np.kp2[m.trainIdx].pt for m in np.good]).reshape(-1,1,2)
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

result = warpTwoImages(img1_color, img2_color, M)

result = cv2.warpPerspective(frontCam_warp, H, (width, height))
result[0:leftCam_warp.shape[0], 0:leftCam_warp.shape[1]] = leftCam_warp

#print(type(result))
#print(result.shape)
cv2.imshow('',result)

cv2.waitKey(0)
cv2.destroyAllWindows()









# if cv2.waitKey(1) == ord('q'):
#     #print(fps)
#     cv2.destroyAllWindows()
#     break

# # transform the panorama image to grayscale and threshold it 
# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

# # Finds contours from the binary image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)

# # get the maximum contour area
# c = max(cnts, key=cv2.contourArea)

# # get a bbox from the contour area
# (x, y, w, h) = cv2.boundingRect(c)

# # crop the image to the bbox coordinates
# result = result[y:y + h, x:x + w]

# # show the cropped image
# plt.figure(figsize=(20,10))
# plt.imshow(result)

# canvas = plt.gca().figure.canvas
# canvas.draw()
# data = np.frombuffer(canvas.tostring_rgb(), dtype=np.uint8)
# image = data.reshape(canvas.get_width_height()[::-1] + (3,))
# cv2.imshow('benin', image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



