import numpy as np
import cv2 # OpenCV lib

resim = cv2.imread("images/logo.jpg") # resim okuma ilk parametre hangi resim 2. ise renk

print(resim[(118,66)])

cv2.imshow("Logo",resim) # resim gösterme

cv2.waitKey(0) # Pencerenin kapanması için herhangi bir tuşa basmamızı bekleyen fonk.

cv2.destroyAllWindows() # OpenCV ile ilgili tüm pencereleri kapamak için