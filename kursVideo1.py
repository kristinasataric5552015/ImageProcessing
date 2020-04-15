# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:53:45 2020

@author: krist
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('satic.jpg', cv2.IMREAD_GRAYSCALE)
#druga opcija 
#IMREAD_COLOR isto je ako stavimo samo 1
#za IMREAD_GRAYSCALE je dovoljno i samo 0
#IM_UNCHANGED isto je kao -1, tj. =-1


cv2.imshow('Prozorcic', img)
cv2.waitKey(0) #ceka da bilo koje dugme bude pritisnuto
cv2.destroyAllWindows() #cim bude pritisnuto unisti sve prozore

#DRUGI NACIN SA MATPLOTLIB
#plt.imshow (img, cmap= 'gray', interpolation='bicubic')
#plt.plot([50,100,], [80,100], 'c', linewidth=5)
#plt.show()
cv2.imwrite('satSIVI.jpg', img)