import cv2
import os

cap = cv2.VideoCapture(0)

path = r"C:\Users\Aman\Desktop\TRINA\OPENCV\DistortionImages"
i=0
while(True):
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
    

cap.release()