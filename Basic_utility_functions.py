import cv2
import numpy as np 

image=cv2.imread("image1.jpg",cv2.IMREAD_COLOR)

image1=cv2.imread("image2.jpg",cv2.IMREAD_COLOR)

#Adding images
added_image=cv2.add(image,image1)

cv2.imshow("my_image",added_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Weighted Addition

weighted=cv2.addWeighted(image,0.8,image1,0.3,0)

cv2.imshow("image",weighted)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Subtracting image

subtract=cv2.subtract(image,image1)

cv2.imshow("Sub",subtract)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Resizing image

pop_corn=cv2.imread("pop-corn.png",cv2.IMREAD_COLOR)

cv2.imshow("resize",pop_corn)

cv2.waitKey(0)

resized=cv2.resize(pop_corn,(300,600))

cv2.imshow("rsd",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Erosion

watermelon=cv2.imread("watermelon.jpg",cv2.IMREAD_COLOR)

d=np.ones((9,9))

s=cv2.erode(watermelon,d)

cv2.imshow("w screen",s)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Adding border

d=cv2.copyMakeBorder(watermelon,30,30,60,60,cv2.BORDER_CONSTANT,value=(150,253,253))

cv2.imshow("s",d)

cv2.waitKey(0)

#differnt kind of border

d=cv2.copyMakeBorder(watermelon,30,30,60,60,cv2.BORDER_REFLECT,value=(150,253,253))

cv2.imshow("s",d)

cv2.waitKey(0)