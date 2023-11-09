# Kenar Algılama
import cv2
import numpy as np

image = cv2.imread("OpenCV/images/kousei.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)

def autoCanny(blur,sigma=0.33):
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median)) 
    upper = int(min(255,(1.0+sigma)*median)) 
    canny = cv2.Canny(blur,lower,upper)
    return canny

wide = cv2.Canny(blur,10,220) # lower ile upper arasını geniş yaptım
tight = cv2.Canny(blur,200,230) # lower ile upper arasını dar yaptm farkı görebilmek için
auto = autoCanny(blur)

cv2.imshow("blur",blur)
cv2.imshow("edges",np.hstack([wide,tight,auto])) # Tüm resimlerimi tek resimmiş gibi yatay olarak sıralar

# canny = cv2.Canny(blur,50,150) # otoCanny den önce kullandım

cv2.waitKey(0)
cv2.destroyAllWindows()