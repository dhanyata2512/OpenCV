import cv2

my_image=cv2.imread("valantine image.webp",cv2.IMREAD_COLOR)
#print(my_image)

cv2.imshow("valantine",my_image)

r=cv2.waitKey(0)

cv2.destroyAllWindows()

my_image=cv2.imread("good-night.png",cv2.IMREAD_COLOR)
#print(my_image)

cv2.imshow("gn",my_image)

s=cv2.waitKey(0)

cv2.destroyAllWindows()

