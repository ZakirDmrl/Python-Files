import cv2 
import numpy as np 

camera = cv2.VideoCapture(0)

while True:
    ret,goruntu = camera.read()
    cv2.rectangle(goruntu,(100,100),(200,200),(100,23,10),3)
    cv2.line(goruntu,(0,0),(100,100),color=(0,0,255),thickness=3)

    cv2.circle(goruntu,(150,150),25,color=(255,0,0),thickness=2)

    cv2.putText(goruntu,"Zakir Abim",(50,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),thickness=5)

    cv2.imshow("Canli",goruntu)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()