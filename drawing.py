import cv2 as r

flower=r.imread("flower.jpg",r.IMREAD_COLOR)

r.imshow("i",flower)
r.waitKey(0)
r.destroyAllWindows()

#drawing a line

r.line(flower,(13,12),(30,30),(250, 230, 230),3)
r.imshow("i",flower)
r.waitKey(0)

#drawing a rectangle

r.rectangle(flower,(100,114),(85,96),(255,0,157),3)
r.imshow("i",flower)
r.waitKey(0)

#drawing a fliied rectangle

r.rectangle(flower,(90,100),(400,60),(203, 192, 255),-10)
r.imshow("i",flower)
r.waitKey(0)

#drawing a circle
r.circle(flower,(155,100),15,(230, 216, 137),2)
r.imshow("i",flower)
r.waitKey(0)

#drawing a filled circle

r.circle(flower,(50,20),13,(200, 213, 48),-1)
r.imshow("i",flower)
r.waitKey(0)

#putting text on the image

r.putText(flower,"Dhanyata",(80,150),r.FONT_ITALIC,0.5,(132,98,193))
r.imshow("i",flower)
r.waitKey(0)