import cv2
import numpy as np

# resim olustur
img = np.zeros((512, 512, 3), np.uint8) # siyah bir resim
print(img.shape)
#cv2.imshow("Siyah", img)


# cizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (150, 150), (300, 300), (0, 255, 0), 10) # BGR Yeşil İçin = (0, 255, 0)
#cv2.imshow("Cizgi", img)

# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.rectangle(img, (0, 0), (100,100), (255, 0, 0), 5)
#cv2.imshow("Dikdortgen", img)

# (resim, daire merkez konumu, yarıçap boyutu, renk, kalınlık)
cv2.circle(img, (350, 350), 50, (0, 0, 255), 10,)
#cv2.imshow("Sekil", img)

# resim, yazı, baslangıc noktası, yazı tipi, yazı boyutu, yazı rengi
cv2.putText(img, "Mervem", (330, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.imshow("Sekil", img)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
    
