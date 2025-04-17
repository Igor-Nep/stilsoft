import cv2
import numpy as np
from datetime import datetime
from time import sleep

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(3,600) 
cap.set(4,400)

target_num = 0
count = 0

ret, frame1 = cap.read()
ret, frame2 = cap.read()

def get_time():
  time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  return time


while cap.isOpened():
 
 
  diff = cv2.absdiff(frame1, frame2) 

  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

  blur = cv2.GaussianBlur(gray, (5, 5), 0) 
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
  dilated = cv2.dilate(thresh, None, iterations = 3) 
  сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
 
   
  for contour in сontours:
    (x, y, w, h) = cv2.boundingRect(contour)
   
  
    print(cv2.contourArea(contour))
   
    if cv2.contourArea(contour) < 200: 
      continue
    cv2.rectangle(frame1, (x, y), (x+w, y+h), (55, 55, 200), 1)
    cv2.putText(frame1, '* REC', (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame1, get_time(), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
   
  if (diff>80).any():
    target_num += 1
    count+=300
    cv2.imshow("frame1", frame1)
    cap.set(1, count)
    cv2.imwrite(f'c:/work/cv2/target_{target_num}.jpg',frame1,[cv2.IMWRITE_JPEG_QUALITY,38]) #cv2.IMWRITE_JPEG_QUALITY (0-100) #cv2.IMWRITE_PNG_COMPRESSION (0-9)

  else:
    
    cv2.destroyAllWindows()  
  frame1 = frame2
  ret, frame2 = cap.read() 
 
  if cv2.waitKey(270) == 27:
    break
   
cap.release()
cv2.destroyAllWindows()