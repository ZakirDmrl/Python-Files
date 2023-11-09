import cv2 
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8")

resim2 = np.zeros((300,300,3),dtype="uint8")

resim[0:150,:,0] = 255
resim[0:150,:,1] = 255
resim[0:150,:,2] = 255

resim2[:,0:150,0] = 255
resim2[:,0:150,1] = 255
resim2[:,0:150,2] = 255

bit_And = cv2.bitwise_and(resim,resim2)
bit_Or = cv2.bitwise_or(resim,resim2)
bit_Xor = cv2.bitwise_xor(resim,resim2)
bit_Not = cv2.bitwise_not(resim,resim2)

cv2.imshow("Resim",resim)
cv2.imshow("Resim2",resim2)
cv2.imshow("Result",bit_And)
cv2.imshow("Result2",bit_Or)
cv2.imshow("Result3",bit_Xor)
cv2.imshow("Result4",bit_Not)

cv2.waitKey(0)

cv2.destroyAllWindows()