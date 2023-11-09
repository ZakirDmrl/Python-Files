import cv2
import numpy as np

camera = cv2.VideoCapture(0) # burada 0 yazarsak bilgisayar kamerasından alır
                             # 1 yazarsak USB de tanımlı kamera
                             # 2 yazarsak da pc de açık olan bir videodan alır.

while True:
    ret,goruntu = camera.read()
    cv2.imshow("Deneme",goruntu)

    if cv2.waitKey(30) & 0xFF == ord("q"): # 30ms de bir foto çekecek ve q ya basılana kadar devam et
        break

camera.release() # Kamerayı serbest bırak

cv2.destroyAllWindows()