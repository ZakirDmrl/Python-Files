import cv2
import numpy as np

image = cv2.imread("images/umbrella2.jpg")

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(image,kernel,iterations=1) # Genişleme işlemi yapar

erosion = cv2.erode(image,kernel,iterations=1) # Aşındırma işlemi yapar

dilation2 = cv2.dilate(erosion,kernel,iterations=1) # Genellikle önce erosion ile gürülütü giderilir sonrasında dilation işlemi yapılır.

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel) # diltion 2 işlemini tek seferde yapar yani erosion sonra dilation işlemlerini uygular.(Ön Plandaki görsele ulaşmak için)

closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel) # birleştirmeli kopuk görsellerde kulanılır.dilation sonra erosion işlemlerini uygular.

gradyan = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel) # diltion halinden original resmi çıkardığımız zamanki durumu

tophat = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel) # Original resim ile opening arasındaki fark ( Arka Plandaki görsele ulaşmak için)

blackhat = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel) # Original resim ile closing arasındaki fark 


cv2.imshow("original",image)

cv2.imshow("dilation",dilation)

cv2.imshow("erosion",erosion)

cv2.imshow("dilation2",dilation2)

cv2.imshow("opening",opening)

cv2.imshow("closing",closing)

cv2.imshow("gradyan",gradyan)

cv2.imshow("tophat",tophat)

cv2.imshow("blackhat",blackhat)


cv2.waitKey(0)

cv2.destroyAllWindows()