import cv2 as r
import os
import numpy as np

main_folder="pictures"

images=[]
names={}
labels=[]
counter=0

for root,folders,files in list(os.walk(main_folder)):
    for folder in folders:
        names[counter]=folder
        path=os.path.join(main_folder,folder)
        for file in os.listdir(path):
            images.append(r.imread(os.path.join(path,file),r.IMREAD_GRAYSCALE))
            labels.append(counter)
        counter=counter + 1 
print(labels)
images=np.array(images)
labels=np.array(labels)
model=r.face.LBPHFaceRecognizer_create()
model.train(images,labels)

WIDTH=130
HEIGHT=120

classifier=r.CascadeClassifier("haarcascade_frontalface_default.xml")
video=r.VideoCapture(0)

while True:
    tf,img=video.read()
    if tf == False:
        continue
    grey_img=r.cvtColor(img,r.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(grey_img,1.3,5)
    for x,y,w,h in faces:
        face=grey_img[y:y+h,x:x+w]
        resized_img=r.resize(face,(WIDTH,HEIGHT))
        r.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        prediction=model.predict(resized_img)
        r.putText(img,names[prediction[0]],(x,y-20),r.FONT_HERSHEY_PLAIN,1,(0,255,0))
    r.imshow("face detection",img)
    key=r.waitKey(30)
    if key == 27:
        break
