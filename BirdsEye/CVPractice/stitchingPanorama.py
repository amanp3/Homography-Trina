import cv2
import numpy as np
import matplotlib.pyplot as plt
#import imageio
import io
import imutils

import matplotlib
matplotlib.use('TkAgg')

cv2.ocl.setUseOpenCL(False)

#pathFrontCamDesired = r'C:\Users\Aman\Desktop\School\Python\frontCamDesired.png'
#pathRightCamDesired = r'C:\Users\Aman\Desktop\School\Python\rightCamDesired.png'
#pathLeftCamDesired = r'C:\Users\Aman\Desktop\School\Python\leftCamDesired.png'


# select the image id (valid values 1,2,3, or 4)
feature_extractor = 'orb' # one of 'sift', 'surf', 'brisk', 'orb'
feature_matching = 'bf'

# read images and transform them to grayscale
# Make sure that the train image is the image that will be transformed
#trainImg = imageio.imread('http://www.ic.unicamp.br/~helio/imagens_registro/foto1A.jpg')
#trainImg_gray = cv2.cvtColor(trainImg, cv2.COLOR_RGB2GRAY)

#uncomment this 4 lines
trainImg = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\TrinaLab180Test1.png')
trainImg_gray = cv2.cvtColor(trainImg, cv2.COLOR_RGB2GRAY)
queryImg = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\TrinaLab180Test2.png')
queryImg_gray = cv2.cvtColor(queryImg, cv2.COLOR_RGB2GRAY)

#queryImg = imageio.imread('http://www.ic.unicamp.br/~helio/imagens_registro/foto1B.jpg')

# Opencv defines the color channel in the order BGR. 
# Transform it to RGB to be compatible to matplotlib
#queryImg_gray = cv2.cvtColor(queryImg, cv2.COLOR_RGB2GRAY)


# trainImg = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\train.png')
# queryImg = cv2.imread(r'C:\Users\Aman\Desktop\School\Python\query.png')
# trainImg_gray = cv2.cvtColor(trainImg, cv2.COLOR_RGB2GRAY)
# queryImg_gray = cv2.cvtColor(queryImg, cv2.COLOR_RGB2GRAY)


t1 = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\panoTest1.png')
t1 = cv2.cvtColor(t1, cv2.COLOR_RGB2GRAY)
t2 = cv2.imread(r'C:\Users\Aman\Desktop\TRINA\OPENCV\panoTest2.png')
t2 = cv2.cvtColor(t2, cv2.COLOR_RGB2GRAY)

t1 = trainImg
t2 = queryImg

# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, constrained_layout=False, figsize=(16,9))
# ax1.imshow(queryImg, cmap="gray")
# ax1.set_xlabel("Query image", fontsize=14)

# ax2.imshow(trainImg, cmap="gray")
# ax2.set_xlabel("Train image (Image to be transformed)", fontsize=14)

# plt.show()

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

kpsA, featuresA = detectAndDescribe(trainImg_gray, method=feature_extractor)
kpsB, featuresB = detectAndDescribe(queryImg_gray, method=feature_extractor)

# display the keypoints and features detected on both images
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,8), constrained_layout=False)
ax1.imshow(cv2.drawKeypoints(trainImg_gray,kpsA,None,color=(0,255,0)))
ax1.set_xlabel("(a)", fontsize=14)
ax2.imshow(cv2.drawKeypoints(queryImg_gray,kpsB,None,color=(0,255,0)))
ax2.set_xlabel("(b)", fontsize=14)

plt.show()


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


print("Using: {} feature matcher".format(feature_matching))

# fig = plt.figure(figsize=(20,8))

if feature_matching == 'bf':
    matches = matchKeyPointsBF(featuresA, featuresB, method=feature_extractor)
    img3 = cv2.drawMatches(trainImg,kpsA,queryImg,kpsB,matches[:100],
                           None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
elif feature_matching == 'knn':
    matches = matchKeyPointsKNN(featuresA, featuresB, ratio=0.75, method=feature_extractor)
    img3 = cv2.drawMatches(trainImg,kpsA,queryImg,kpsB,np.random.choice(matches,100),
                           None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    

plt.imshow(img3)
plt.show()

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

M = getHomography(kpsA, kpsB, featuresA, featuresB, matches, reprojThresh=4)
if M is None:
    print("Error!")
(matches, H, status) = M
#print(matches)
print(H)

# define a function which returns an image as numpy array from figure
def get_img_from_fig(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

# Apply panorama correction
width = trainImg.shape[1] + queryImg.shape[1]
height = trainImg.shape[0] + queryImg.shape[0]


result = cv2.warpPerspective(t1, H, (width, height))

plt.figure(figsize=(20,10))
plt.imshow(result)

plt.axis('off')


plt.show()


result[0:t2.shape[0], 0:t2.shape[1]] = t2

#cv2.imshow('',result)
plt.figure(figsize=(20,10))
plt.imshow(result)

plt.axis('off')


plt.show()

# width = stitch1.shape[1] + stitch2.shape[1]
# height = stitch1.shape[0] + stitch2.shape[0]

# result = cv2.warpPerspective(stitch1, H, (width, height))


# result[0:stitch2.shape[0], 0:stitch2.shape[1]] = stitch2

#plot_img_np = get_img_from_fig(result)
# convert canvas to image
# img = np.fromstring(result.canvas.tostring_rgb(), dtype=np.uint8,
#         sep='')
# img  = img.reshape(result.canvas.get_width_height()[::-1] + (3,))

# img is rgb, convert to opencv's default bgr
#img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

#cv2.imshow(plot_img_np)



# plt.figure(figsize=(20,10))
# plt.imshow(result)

# plt.axis('off')


# plt.show()






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
cv2.waitKey(0)
cv2.destroyAllWindows()