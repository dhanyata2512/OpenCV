import cv2 as s

bird=s.imread("bird.jpg",s.IMREAD_COLOR)
#change coloured image to greyscale

g=s.cvtColor(bird,s.COLOR_BGR2GRAY)

s.imshow("wn",g)

s.waitKey(0)

s.destroyAllWindows()

#rotate image

print(bird.shape)

m=s.getRotationMatrix2D((350,350),90,0.5)

d=s.warpAffine(bird,m,bird.shape[0:2])

s.imshow("r",d)

s.waitKey(0)

s.destroyAllWindows()

image=s.imread("image1.jpg",s.IMREAD_COLOR)

e=s.Canny(image,100,200)

s.imshow("r",e)

s.waitKey(0)

s.destroyAllWindows()

#blurring image

b=s.GaussianBlur(image,(99,99),0)

s.imshow("bi",b)

s.waitKey(0)

s.destroyAllWindows()

m=s.medianBlur(image,15)

s.imshow("bi",m)

s.waitKey(0)

s.destroyAllWindows()

y=s.bilateralFilter(image,6,100,90)

s.imshow("bi",y)

s.waitKey(0)
