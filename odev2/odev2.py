import cv2
import numpy as np

# Kamera bağlantısını açın
cap = cv2.VideoCapture(0)

while True:
    # Giriş görüntüsünü oku
    ret, frame = cap.read()

    # Giriş görüntüsünü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin HSV aralığını belirleyin
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # HSV görüntüsünü belirlenen renk aralığına göre maskeleyin
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # İlk kare ve maskeleme sonucunu birleştirin
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonucu göster
    cv2.imshow('Original', frame)

    cv2.imshow('Result', result)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırakın ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()
