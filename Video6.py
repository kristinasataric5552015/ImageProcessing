import numpy as np
import cv2

img = cv2.imread('book.jpg')


#cv.threshold koristi se za primenu praga.
##1. argument je izvorna slika, koja bi trebala biti slika u sivim
##tonovima
##2. argument je vrednost praga koja se koristi za klasifikaciju
##vrednosti piksela.
##3. argument je maksimalna vrednost koja se dodeljuje
##vrednostima piksela većim od praga.
##4. argument tip praga
retval, threshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('orginalna',img)
cv2.imshow('treshold', threshold)
cv2.imshow('treshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()





