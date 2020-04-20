import numpy as np
import cv2

img = cv2.imread ('satic.jpg', cv2.IMREAD_COLOR)

#odredjeni pisel na fotki
px = img [55,55]
#print(px)

#izmena piksela
img[55,55] = [255,255,255]
print(px)

#Region Of Image
##roi = img[100:155, 100:150]
##print(roi)

#deo slike pretvaramo u belo
img[100:155, 100:150] = [255,255,255]

#oblast slike, roi
watch_face = img[37:111, 107:194]
#111 - 37 = 74 , 194 - 107 = 87

#uzeo je piksele od watch_face
img[0:74, 0:87] = watch_face


cv2.imshow ('Fotka', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
