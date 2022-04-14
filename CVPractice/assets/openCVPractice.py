import numpy as np
import cv2

# path
#path = r'C:\Users\Aman\Desktop\TRINA\OPENCV\sampleAVMimage.png'
path = r'C:\Users\Aman\Desktop\TRINA\OPENCV\cameraImage.png'
  
# Using cv2.imread() method
img = cv2.imread(path)

cv2.imshow('Window', img)
cv2.waitKey(0)
cv2.destoryAllWindows()