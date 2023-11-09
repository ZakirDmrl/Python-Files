import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread("images/sekiller3.jpg") 
font = cv2.FONT_HERSHEY_COMPLEX
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
a, thresh = cv2.threshold(gri, 200, 255, cv2.THRESH_BINARY)
kontur,b = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in kontur:
    e = 0.01*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,e,True)
    cv2.drawContours(img,[approx],0,5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(approx)
    print(len(approx))

    if(len(approx)==3):
        cv2.putText(img,"ucgen",(x,y),font,1,1,(0))
    elif(len(approx)==4):
        cv2.putText(img,"diktortgen",(x,y),font,1,1,(0))
    elif(len(approx)==5):
        cv2.putText(img,"besgen",(x,y),font,1,1,(0))
    elif(len(approx)==6):
        cv2.putText(img,"altigen",(x,y),font,1,1,(0))
    elif(len(approx)==7):
        cv2.putText(img,"yedigen",(x,y),font,1,1,(0))
    elif(len(approx)==8):
        cv2.putText(img,"sekizgen",(x,y),font,1,1,(0))
    elif(len(approx)==9):
        cv2.putText(img,"dokuzgen",(x,y),font,1,1,(0))
    elif(len(approx)==10):
        cv2.putText(img,"ongen",(x,y),font,1,1,(0))    
    elif(len(approx)==11):
        cv2.putText(img,"onbirgen",(x,y),font,1,1,(0))

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()