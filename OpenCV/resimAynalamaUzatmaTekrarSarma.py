import cv2 

resim  = cv2.imread("images/piano.jpg")

aynali = cv2.copyMakeBorder(resim,75,75,100,100,cv2.BORDER_REFLECT) # Aynalama

uzatilan = cv2.copyMakeBorder(resim,75,75,100,100,cv2.BORDER_REPLICATE) # Uzatma

tekrarli =  cv2.copyMakeBorder(resim,150,150,100,100,cv2.BORDER_WRAP) # Tekrarli

sarilan = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,255)) # Sarma



cv2.imshow("Piano1",aynali)

cv2.imshow("Piano2",uzatilan)

cv2.imshow("Piano3",tekrarli)

cv2.imshow("Piano4",sarilan)






cv2.waitKey(0)

cv2.destroyAllWindows()