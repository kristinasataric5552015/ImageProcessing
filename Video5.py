import numpy as np
import cv2

# 500 x 250, iste su velicine
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#add = img1 + img2

#dodati su svi pikseli sa obe slike
#(155,211,79) + (50, 170, 200) = 205, 381, 279...prevedeni u
#(205, 255,255)
#add = cv2.add(img1,img2)


#1. parametar je slika
#2. parametar je tezina
#3. parametar je druga slika
#4. parametar je ta tezina
#5. parametar je gamma, sto je mera svetlosti,
#ostavljamo je na 0 za sada
#weighted = cv2.addWeighted(img1,0.6, img2, 0.4, 0)

#cv2.imshow('add',add)
#cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
