import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),color=(0,0,255),thickness=3)

cv2.circle(resim,(150,150),25,color=(255,0,0),thickness=2)

cv2.putText(resim,"Zakir Abim",(50,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),thickness=5)

cv2.imshow("denem-line",resim)

cv2.waitKey()

cv2.destroyAllWindows()