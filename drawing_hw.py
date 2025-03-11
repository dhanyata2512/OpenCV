import cv2 as r

flower=r.imread("flower.jpg",r.IMREAD_COLOR)

r.imshow("i",flower)
r.waitKey(0)
r.destroyAllWindows()

#drawing a filled circle

r.circle(flower,(50,70),40,(200, 213, 48),-1)
r.imshow("i",flower)
r.waitKey(0)

r.circle(flower,(40,57),10,(0,0,0),-1)
r.imshow("i",flower)
r.waitKey(0)#

r.circle(flower,(70,57),10,(0,0,0),-1)
r.imshow("i",flower)
r.waitKey(0)

r.line(flower,(80,84),(30,80),(0,0,0),3)
r.imshow("i",flower)
r.waitKey(0)
