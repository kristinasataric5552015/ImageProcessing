import numpy as np
import cv2
img = cv2.imread('satic.jpg', cv2.IMREAD_COLOR)

#za iscrtavanje linije preko slike
#prvi argument je fotka,
#drugi parametar je gde pocinje linija,
#treci argument gde se zavrsava
#cetvrti je boja bgr, 255 255 255 je bela
#peti je opcionalan, debljina linije
cv2.line(img, (0,0),(150, 150), (255, 255,255), 15)

##crtanje trougla
##1. argument na cemu crtamao
##2. argument je gde pocinje, pocetna ta;ka
##3. argument je zavrsna tacka
##4. boja bgr
##5. debljina linije
cv2.rectangle(img, (150, 150),(600,400), (0,255,0), 5)

#krug
##1. argument na cemu crtamo
##2. je centar kruga
##3. radius tj poluprecnik
##4. je boja
##5. debljina linije ili ako stavimo -1 obojice ceo krug
cv2.circle(img, (495,321), 77, (0,0,255),-1 )

#points tacke
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
##pts = pts.reshape((-1,1,2))

#poligon
##1. argument na cemu crtamo
##2. drugi argument niz tacaka
##3. argument True znaci da hocemo da povezemo prvu tacku sa poslednjom
##4. boja bgr
##5. argument debljina linie
cv2.polylines(img, [pts], True, (0,255,255),3)

font= cv2.FONT_HERSHEY_SIMPLEX
#pisanje teksta
##1. argument na cemu pisemo
##2. argument tekst
##3. argument je tacka gde se pocinje
##4. font
##5. velicina
##6. boja
##7. Debljina slova
cv2.putText(img, 'OpenCV la la', (0,130), font, 1,(255,0,255), 5 , cv2.LINE_AA)

cv2.imshow('Video3RezultatFotka',  img)
cv2.waitKey(0)
cv2.destroyAllWindows()





