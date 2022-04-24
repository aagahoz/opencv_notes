import cv2 # opencv kütüphanesini içe aktaralım
import matplotlib.pyplot as plt # matplotlib kütüphanesini içe aktaralım

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("odev1.jpg", 1)

# resmi çizdirelim
cv2.imshow("Orjinal", img)

# resmin boyutuna bakalım
print(img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
küçültme_orani = 4/5
height = int(img.shape[0] * küçültme_orani)
width = int(img.shape[1] * küçültme_orani)
dim = (width, height)
img_resized = cv2.resize(img, dim)
cv2.imshow("Resized", img_resized)

img_resized_and_coloured = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

plt.figure(1), plt.imshow(img_resized_and_coloured), plt.show()

# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
img_texted = cv2.putText(img_resized_and_coloured, "At", (165, 51), cv2.FONT_HERSHEY_SIMPLEX, 1, (55, 150, 43))
img_texted = cv2.putText(img_resized_and_coloured, "Kopek", (344, 69), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 43))
img_texted = cv2.putText(img_resized_and_coloured, "Kedi", (500, 110), cv2.FONT_HERSHEY_PLAIN, 1, (120, 80, 120))
plt.figure(2), plt.imshow(img_texted), plt.show()



# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
cv2.imshow("image t123hresholded", img)
_, img_thresholded1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("image thresholded", img_thresholded1)
_, img_thresholded2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("image thresholded Inv", img_thresholded2)


# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gaussion_blurred = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)
cv2.imshow("Gaussion Blurred2", gaussion_blurred)

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img, ddepth = 30)
cv2.imshow("laplacian_image", laplacian)


# orijinal resmin histogramını çizdirelim
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure(3), plt.plot(hist, color='b'), plt.show()


k = cv2.waitKey(1)
if k == ord("q"):
    cv2.destroyAllWindows()
    
