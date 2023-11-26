import cv2
import numpy as np

# Görüntüyü oku
image = cv2.imread('pirinc.png')

# Gri seviyeye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşikleme yap
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler uygula (istenmeyen arka planları temizle)
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Nesne etiketleme yap
_, labels, stats, centroids = cv2.connectedComponentsWithStats(morph)

# Toplam pirinç sayısını bul
rice_count = len(stats) - 1  # İlk etiket (arka plan) hariç diğer etiketleri say

# Eşiklenmiş görüntüyü göster
cv2.imshow("gerçek resim", image)
cv2.imshow('Thresholded Image', morph)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Pirinç sayısını ekrana yazdır
print('Pirinç Sayısı:', rice_count)
