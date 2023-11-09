import cv2
import numpy as np

img = cv2.imread("OpenCV/images/ucgen.png")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gri, 75, 100, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result_img = np.zeros_like(img)

cv2.drawContours(result_img, contours, -1, (255, 0, 0), 3)

convex_hulls = []

for contour in contours:
    hull = cv2.convexHull(contour)
    convex_hulls.append(hull)

cv2.drawContours(result_img, convex_hulls, -1, (0, 255, 0), 1)

cv2.imshow("resim", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
