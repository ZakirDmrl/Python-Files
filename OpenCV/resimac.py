import numpy as np
import cv2 # OpenCV lib

resim = cv2.imread("images/logo.jpg",0) # resim okuma ilk parametre hangi resim 2. ise renk

cv2.imshow("Logo",resim) # resim gösterme

cv2.imwrite("yeniresim.jpg",resim) # Oluşturulan resmi kaydetmek için

cv2.waitKey(0) # Pencerenin kapanması için herhangi bir tuşa basmamızı bekleyen fonk.

cv2.destroyAllWindows() # OpenCV ile ilgili tüm pencereleri kapamak için