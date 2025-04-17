import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 25)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    ret, img = cap.read()
    if ret:
        cv2.imshow('Image', img)
        cv2.waitKey(100)
   
    elif cv2.waitKey(10) == 27: 
        break
    else:
        print('Failed to capture image')

cap.release()
cv2.destroyAllWindows() 