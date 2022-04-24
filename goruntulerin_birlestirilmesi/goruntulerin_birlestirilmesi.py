import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("Orjinal", img)


# yatay
hor = np.hstack((img, img))
cv2.imshow("Dikey Birlestirilmis", hor)

# dikey
ver = np.vstack((img, img))
cv2.imshow("Yatay Birlestirilmis", ver)

k = cv2.waitKey()
if k == ord("q"):
    cv2.destroyAllWindows()
    

    