import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('opencv-feature-matching-image.jpg',0)

#ovo je detektor koji ćemo koristiti
orb = cv2.ORB_create()

#pronalazimo ključne tačke i njihove deskriptore pomoću detektora orb
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#ovo je BFMatcher objekat
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#Ovde kreiramo podudarnosti deskriptora,
#a zatim ih sortiramo na osnovu njihove udaljenosti.
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

# iscrtvamo prvih 10 mečeva
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
