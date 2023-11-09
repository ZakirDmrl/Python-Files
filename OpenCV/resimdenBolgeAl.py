import cv2
import numpy as np
bresim = cv2.imread("images/logo.jpg")

kresim = bresim[50:150,300:400] # ilk koordinant y 2.side x koordinantı
bresim[:,:,1] = 100

bresim[:,:,0] = 105

kresim[:,:,0] = 30


bresim[0:100,0:100] = kresim


cv2.imshow("Logo",bresim)

cv2.waitKey(0)

cv2.destroyAllWindows()