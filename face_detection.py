import cv2 as r
import os

mainfolder="pictures"
subfolder="Dhanyata"
path=os.path.join(mainfolder,subfolder)
if not os.path.isdir(path):
    os.makedirs(path)
    print("folder created")   

WIDTH=130
HEIGHT=120
classifier=r.CascadeClassifier("haarcascade_frontalface_default.xml")
video=r.VideoCapture(0)
# If any external webcam use 1

pic_count=0
while pic_count < 30:
    tf,img=video.read()
    grey_img=r.cvtColor(img,r.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(grey_img,1.3,5)
    print(faces)
    for x,y,w,h in faces:
        face=grey_img[y:y+h,x:x+w]
        resized_img=r.resize(face,(WIDTH,HEIGHT))
        r.imwrite(path+str(pic_count)+".png",resized_img)
        r.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        pic_count=pic_count+1
    r.imshow("face detection",img)
    key=r.waitKey(30)
    if key == 27:
        break


