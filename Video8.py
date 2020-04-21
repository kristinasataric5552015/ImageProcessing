import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv hue sat vrednost
    lower_red = np.array([100,100,40])
    upper_red = np.array ([200,255,100])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask = mask)

    #averaging
    #225 je jer je 15 x 15 = 225
    #15 po 15 piksela
    kernel = np.ones((15,15),np.float32)/225
    
    smoothed = cv2.filter2D(res,-1,kernel)
    cv2.imshow('Averaging',smoothed)
    
    blur = cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow('Gaussian Blurring',blur)
    
    median = cv2.medianBlur(res,15)
    cv2.imshow('Median Blur',median)
    
    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral Blur',bilateral)
  
    cv2.imshow('Original',frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
