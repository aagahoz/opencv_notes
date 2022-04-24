import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.figure(1), plt.imshow(img), plt.axis("off"), plt.title("Orjinal"), plt.show()

# blurring --> detayı azaltır ve gürültüyü engeller

# ortalama bulanıklaştırma yöntemi
dst1 = cv2.blur(img, ksize = (3, 3))
plt.figure(2), plt.imshow(dst1), plt.axis("off"), plt.title("Ortalama Blur"), plt.show()

# Gauss Blur bulanıklastırma yöntemi
dst2 = cv2.GaussianBlur(img, ksize = (3, 3), sigmaX = 7)
plt.figure(3), plt.imshow(dst2), plt.axis("off"), plt.title("Gauss Blur"), plt.show()

# Medyan bulanıklaştırma yöntemi, ortanca pixelin degeri
dst3 = cv2.medianBlur(img, ksize = 3)
plt.figure(4), plt.imshow(dst3), plt.axis("off"), plt.title("Medyan Blur"), plt.show()



def gaussionNoise(image):
    
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy

# ice aktar ve normalize et
img1 = cv2.imread("NYC.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) / 255 
plt.figure(5), plt.imshow(img1), plt.axis("off"), plt.title("Orjinal"), plt.show()


# noise ekle
GaussionNoiseResim = gaussionNoise(img1)
plt.figure(6), plt.imshow(GaussionNoiseResim), plt.axis("off"), plt.title("GaussionNoiseResim"), plt.show()

# noiselanmıs görüntüye gauss blur ekle
dst4 = cv2.GaussianBlur(GaussionNoiseResim, ksize = (3, 3), sigmaX = 7)
plt.figure(7), plt.imshow(dst4), plt.axis("off"), plt.title("Noiselanmıs Görüntünün Gauss Blur Uygulanmısı"), plt.show()


def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    # pepper siyah
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy
       
spImage = saltPepperNoise(img1)   
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Medyan Blur")







