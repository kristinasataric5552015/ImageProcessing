# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:08:46 2020

@author: krist
"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
#0 znaci da ce biti prva video kamera u sistem

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter ('output.avi', fourcc, 20.0,(640,480))

while True: #beskonacna petlja
    ret, frame = cap.read()
    
    #2.deo, prebacujemo u sivo
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #3.deo za cuvanje snimka
    out.write(frame)
    
    cv2.imshow('prozorce', frame)
    cv2.imshow('gray', gray)
    
    
    #kako bi izasli iz beskonacne petlje
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
    
cap.release()
out.release()#za cuvanje snimka
cv2.destroyAllWindows()
