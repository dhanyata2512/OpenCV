import cv2
import numpy as np

img = cv2.imread('car.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

l_yellow = np.array([13,50,180])
u_yellow = np.array([40,255,255])

mask = cv2.inRange(hsv, l_yellow, u_yellow)

results = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Masked image',results)
cv2.waitKey(0)
cv2.destroyAllWindows()