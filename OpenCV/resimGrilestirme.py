import cv2
import numpy as np

resim = cv2.imread("images/logo.jpg")
resimGri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

cv2.imshow("original",resim)
cv2.imshow("Gri",resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()