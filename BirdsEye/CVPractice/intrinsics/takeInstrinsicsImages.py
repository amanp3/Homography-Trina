import cv2
import os

cap = cv2.VideoCapture(3)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width1 = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height1 = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width1, height1)

path = r"C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages\LeftCamera"
i=0
run = True
while(run):
    ret, frame = cap.read() # return a single frame in variable `frame`
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite(os.path.join(path, 'distortedImg'+ str(i)+'.png'), frame)
        print('distortedImg'+ str(i)+'.png' + "saved to path")
        cv2.destroyAllWindows()
        i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    if i == 20:
        print("That is enough Images for this camera's intrinsic calibration")
        run = False
        
    

cap.release()