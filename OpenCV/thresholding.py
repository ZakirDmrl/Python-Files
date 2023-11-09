# Simple Thresholding 
import cv2

image = cv2.imread("images/parmakizi.jpg",0) # Thresholding kullanmak için 0 olmalı
 
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret2,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret3,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret4,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret5,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()