import cv2

img = cv2.imread("lenna.png", 1) # 1 parametresi renkli okunmasını sağlar

print("Resim boyutu: ", img.shape)
cv2.imshow("Orjinal1", img)


# resized
imgResized = cv2.resize(img, (400, 400))
print("Yeniden Boyutlandırılmıs Resim boyutu: ", imgResized.shape)
cv2.imshow("Orjinal2", imgResized)


# kırp
imgCropped = img[:200, :300]
cv2.imshow("Orjinal3", imgCropped)

k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
    
