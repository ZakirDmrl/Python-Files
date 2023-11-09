import cv2

image = cv2.imread("images/umbrella2.jpg")

meanFilter = cv2.blur(image,(5,5)) # 5 e 5 lik pixellerin ort. alıp rengi ona göre veriyor
                                   # Bu sayede de daha yumuşak bir görüntü oluyor.
medianFilter = cv2.medianBlur(image,5) 

gaussFilter = cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("Original",image)

cv2.imshow("MeanFilter",meanFilter)

cv2.imshow("MedianFilter",medianFilter)

cv2.imshow("GaussFilter",gaussFilter)

cv2.waitKey(0)

cv2.destroyAllWindows()