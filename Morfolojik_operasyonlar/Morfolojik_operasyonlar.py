import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar

img = cv2.imread("datai_team.jpg")
plt.figure(1), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("orjinal")


# erozyon
kernel = np.ones((1, 1), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

plt.figure(2), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")
    