import cv2

image = cv2.imread("images/parmakizi.jpg",0)
#Simple Thresholing
rec,thresh1 = cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#Otsu Thresholding
rec2,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 0,255 aralığında verip otsu kullandık ve işlemi oto olarak yaptı

cv2.imshow("original",image)
cv2.imshow("Simple",thresh1)
cv2.imshow("Otsu",thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()