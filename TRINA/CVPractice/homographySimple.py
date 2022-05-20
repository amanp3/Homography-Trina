#working
import numpy as np
import cv2
import time

# path1 = r'C:\Users\Aman\Desktop\TRINA\OPENCV\source.jpg'
# path2 = r'C:\Users\Aman\Desktop\TRINA\OPENCV\desired.jpg'
path1 = r'C:\Users\Aman\Desktop\School\Python\TRINA\frontCamActual.png'
path2 = r'C:\Users\Aman\Desktop\School\Python\TRINA\frontCamDesired.png'


t = time.time()
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


#patternSize stores the size of the chessboard you are looking for
patternSize = (8,6)

ret1, corners1 = cv2.findChessboardCorners(img1, patternSize)
ret2, corners2 = cv2.findChessboardCorners(img2, patternSize)



H, _ = cv2.findHomography(corners1, corners2)

print(H)
print("This took {:.9f} seconds".format(time.time() - t))

#t = time.time()

# img1_warp = cv2.warpPerspective(img1, H, (img1.shape[1], img1.shape[0]))
def warpSingleImage(img,H):
    h,w = img.shape[:2]
    print(h,w)
    pts = np.float32([[0,0],[0,h],[w,h],[w,0]]).reshape(-1,1,2)
    pts_ = cv2.perspectiveTransform(pts,H)
    print(pts)
    [xmin, ymin] = np.int32(pts_.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(pts_.max(axis=0).ravel() + 0.5)
#     template = np.zeros((xmax-xmin,ymax-ymin,3))
    t = [-xmin,-ymin]
    print(t,xmax,ymax)
    Ht = np.array([[1,0,t[0]],[0,1,t[1]],[0,0,1]]) # translate
    result = cv2.warpPerspective(img, Ht.dot(H), (xmax-xmin, ymax-ymin))
    result = cv2.resize(result,(480,720))
    print(result.shape)
#     template[t[1]:h+t[1],t[0]:w+t[0]] = result
    return result
img1_warp = warpSingleImage(img1,H)

#print("This took {:.9f} seconds".format(time.time() - t))


cv2.imshow('Original', img1)
cv2.imshow('Window', img1_warp)
cv2.waitKey(0)
cv2.destroyAllWindows()