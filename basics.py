import cv2

my_image=cv2.imread("pop-corn.png",cv2.IMREAD_COLOR)
#print(my_image)

cv2.imshow("popcorn",my_image)

r=cv2.waitKey(0)
print(r)

cv2.destroyAllWindows()

image2=cv2.imread("pop-corn.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("popcorn",image2)

d=cv2.waitKey(0)
print(d)

cv2.imwrite("grey_scale pop-corn.png",image2)

#split in blue, green, red

b,g,r=cv2.split(my_image)
print(r)