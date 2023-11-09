import numpy as np
import cv2 # OpenCV lib

resim = cv2.imread("logo.jpg") # resim okuma ilk parametre hangi resim 2. ise renk

# resim[:,:,0] = 255 #blue
# resim[:,:,1] = 255 #green # Değişik komp. ile genel efektler yapılabilir.
# resim[:,:,2] = 255  #red

resim[150:200,300:400,0] = 255
resim[100:200,200:400,1] = 255
resim[80:200,100:400,2] = 255
cv2.imshow("Logo",resim) # resim gösterme


cv2.waitKey(0) # Pencerenin kapanması için herhangi bir tuşa basmamızı bekleyen fonk.

cv2.destroyAllWindows() # OpenCV ile ilgili tüm pencereleri kapamak için