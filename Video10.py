import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    #uzmi svaki okvir
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Laplasov gradijent
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)

    #Sobel
    #k size = kernel size
    #horizontalni gradijent
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #vertikalni gradijent
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    #detektor ivica
    edges = cv2.Canny(frame,100,200)
    
    cv2.imshow('Edges',edges)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
