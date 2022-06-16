import cv2
import numpy as np
import os

# fileName = r'rightCamDesired.png'

# folder = r'C:/Users/Aman/Desktop/School/Python/TRINA/CalibrationImages720/'
# img = cv2.imread(os.path.join(folder, fileName))

# result = cv2.resize(img,(640,480))
# cv2.imwrite(fileName, result)

outPath = r"C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\LeftCamera"
path = r"C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\LeftCamera720"

# iterate through the names of contents of the folder
for image_path in os.listdir(path):

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    image_to_resize = cv2.imread(input_path)

    # rotate the image
    result = cv2.resize(image_to_resize,(640,480))

    # create full output path, 'example.jpg' 
    # becomes 'rotate_example.jpg', save the file to disk
    fullpath = os.path.join(outPath, image_path)
    cv2.imwrite(fullpath, result)