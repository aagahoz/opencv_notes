import cv2
import matplotlib.pyplot as plt

# resimleri okuma
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# plt.figure()
# plt.imshow(img1)
# plt.figure()
# plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

print(img1.shape)
print(img2.shape)

# plt.figure()
# plt.imshow(img1)
# plt.figure()
# plt.imshow(img2)

# karıstırılmıs resim
# resim = alpha * resim1  + beta * resim2

blended = cv2.addWeighted(img1, 0.3, img2, 0.5, 150)

plt.figure()
plt.imshow(blended)