import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img1 = cv2.imread("img1.JPG")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img1, cmap = "gray")
plt.axis("off")
plt.show()


# treshold = eşikleme
_, thresh_img = cv2.threshold(img1, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thresh_img , cmap = "gray")
plt.axis("off")
plt.show()


thresh_img2 = cv2.adaptiveThreshold(img1, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType = cv2.THRESH_BINARY, blockSize = 11, C = 8)
plt.figure()
plt.imshow(thresh_img2 , cmap = "gray")
plt.axis("off")
plt.show()