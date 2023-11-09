import cv2
import numpy as np
resim = cv2.imread("images/tititi.jpg")

# resim[20:100,70:130,0] = 255

cv2.rectangle(resim,(100,20),(130,70),[255,0,0],4)
cv2.imshow("Logo",resim)

cv2.waitKey(0)

cv2.destroyAllWindows()