import cv2
import numpy as np
resim = cv2.imread("images/kousei.jpg",0) # Asında buradaki 0 kanal sayısı oluyor(r,g,b) yok yani

cv2.imshow("kousei",resim)

print(resim) # piksellerin matrisel karşılığını görmek için
print(resim.size) # kaç pikselli ?
print(resim.dtype) # tipini görmek için uint8 genelde 
print(resim.shape) # Genişlik yükseklik ve kaç kanal kullanıyor(r,g,b)

cv2.waitKey(0)

cv2.destroyAllWindows()