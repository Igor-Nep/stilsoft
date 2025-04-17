import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.getBuildInformation())
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print('video = cv2.VideoCapture(i)')
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print('video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)')

video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
print('video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)')

video.set(cv2.CAP_PROP_FOURCC, 0x32595559)
print('video.set(cv2.CAP_PROP_FOURCC, 0x32595559)')

video.set(cv2.CAP_PROP_FPS, 25)
print('video.set(cv2.CAP_PROP_FPS, 25)')

if not video.isOpened():
    raise IOError("Cannot open WEBCAM")

while True:
    print('while True:')
    ret, frame = video.read()
    print('ret, frame = video.read()')
    print(f'ret is: {ret}')
    
    if ret:
        print(' if ret:')
        cv2.imwrite("c:/work/cv2/newimage.png", frame)
        #cv2.imshow('video feed', frame)
        #plt.imshow(frame)
        #plt.title('Image')
        #plt.show()
        cv2.waitKey(10)
        
    elif cv2.waitKey(1) == 27: 
        break    

    if not ret:
        break

video.release()
cv2.destroyAllWindows()