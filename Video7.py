import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
#HSV, Hue Saturation Value
#Hue range is [0,179],
#Saturation range is [0,255]
#Value range is [0,255].
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([100,100,40])
    upper_red = np.array ([200,255,100])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    
