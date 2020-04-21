import numpy as np
import cv2

#ucitavanje slika
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

#stavljamo logo u gornji levi ugao, kreiramo ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# kreiranje maske loga 
#kreiranje sive verzije loga
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#dodavanje threshold, praga
##1.parametar gde dodaje treshold
##2.parametar je vrednost tresshold 
##3.je maksimalna vrednost
##4.ako je iznad 220 pretvorice je u 255, ako je ispod 220 pretvorice u crno
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#invertuje svaki bit u nizu
mask_inv = cv2.bitwise_not(mask)

#zatamljujemo oblast loga u ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#uzimamo samo regiju loga sa slike loga
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('Rezultat',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
