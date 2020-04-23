import numpy as np
import cv2
#razlicite cascade se nalaze se na linku:
#https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#mozemo kameru da aktiviramo sa 0, cv2.VideoCapture(0)
cap = cv2.VideoCapture('mr_bean.jpg')

#funkciju detectMultiScale pronalazi lice 
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
#pronalazimo lica, njihove veličine, crtamo pravougaonika i  ROI. 
    for (x,y,w,h) in faces:
        #rectangle(izvor-slika), pocetne koordinate, krajnje, boja, debljina)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
#ako oci pronađemo, napravit ćemo još pravougaonika.  
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

    cv2.imshow('Detekcija lica i ociju',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
