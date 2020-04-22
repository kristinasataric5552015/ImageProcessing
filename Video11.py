import cv2
import numpy as np

#velika slika
img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#mala
template = cv2.imread('opencv-template-for-matching.jpg',0)

#način da uzmemo shape 
w, h = template.shape[::-1]

#rezultati, ccoeff_normed nam daje poklapanja
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#80%
#ukoliko smanjimo prag, bice vise detekcija, nece biti toliko precizan
threshold = 0.9

#lokacija je gde je rezultat podudaranja >= od praga 
loc = np.where( res >= threshold)

#oznaka na delove gde imamo poklapanja
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 3)

cv2.imshow('Pronadjeno',img_rgb)
