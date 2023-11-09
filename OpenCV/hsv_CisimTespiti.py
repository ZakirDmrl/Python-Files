import cv2 
import numpy as np
def hicbirsey(x):
    pass

img = cv2.imread('OpenCV/images/roadster.jpg')
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",650,300)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, hicbirsey)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, hicbirsey)
cv2.createTrackbar("Satur Min", "Trackbars", 0, 255, hicbirsey)
cv2.createTrackbar("Satur Max", "Trackbars", 255, 255, hicbirsey)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, hicbirsey)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, hicbirsey)

while True:
    img = cv2.imread('OpenCV/images/roadster.jpg')
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Satur Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Satur Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Value Max", "Trackbars")
    print(h_min,s_min,v_min)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)


    result = cv2.bitwise_and(img,img,mask=mask)
    horStack = np.hstack((img,result))
    verStack = np.vstack((img,result))
    cv2.imshow("horStack",horStack)
    cv2.imshow("verStack",verStack)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



# cv2.imshow("Roadster",img)
# cv2.imshow("HSV",imgHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()