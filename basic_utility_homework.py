import cv2
import numpy as np 

fox=cv2.imread("fox.jpg",cv2.IMREAD_COLOR)

cv2.imshow("resize",fox)

cv2.waitKey(0)

resized=cv2.resize(fox,(300,700))

cv2.imshow("rsd",resized)
 
cv2.waitKey(0)

cv2.destroyAllWindows()

#Erosion

watermelon=cv2.imread("watermelon.jpg",cv2.IMREAD_COLOR)

d=np.ones((13,12))

s=cv2.erode(watermelon,d)

cv2.imshow("w screen",s)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Adding border

d=cv2.copyMakeBorder(watermelon,70,70,60,60,cv2.BORDER_CONSTANT,value=(150,253,253))

cv2.imshow("s",d)

cv2.waitKey(0)

#differnt kind of border

d=cv2.copyMakeBorder(watermelon,30,30,60,60,cv2.BORDER_REFLECT,value=(150,253,253))

cv2.imshow("s",d)

cv2.waitKey(0)

