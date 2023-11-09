import cv2
import numpy as np

resim = cv2.imread("images/tititi.jpg")

ikiKatB = cv2.pyrUp(resim)

ikiKatK = cv2.pyrDown(resim)

cv2.imshow("original resim",resim)

cv2.imshow("iki kat büyük resim",ikiKatB)

cv2.imshow("iki kat küçük resim",ikiKatK)

cv2.waitKey(0)

cv2.destroyAllWindows()