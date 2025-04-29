import cv2 as r
import numpy

classifier=r.CascadeClassifier("cars.xml")
car=r.VideoCapture("video.avi")


while car.isOpened():
    tf,img=car.read()
    gry_img=r.cvtColor(img,r.COLOR_BGR2GRAY)
    vehicles=classifier.detectMultiScale(gry_img,1.3,1)
    for x,y,w,h in vehicles:
        rectagle=r.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2,r.LINE_8)

    r.imshow("CAR DETECTION",img)
    key=r.waitKey(30)
    if key == 27:
        break        

