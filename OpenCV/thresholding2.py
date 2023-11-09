import cv2

image = cv2.imread("images/parmakizi.jpg",0)
#Simple Thresholing
rec,thresh1 = cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#Adaptive Thresholding
thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                               cv2.THRESH_BINARY,11,2)
thresh3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                               cv2.THRESH_BINARY,11,2)

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()