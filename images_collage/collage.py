import cv2 as r
import os

path="C:\\Users\\Bhulku\\Desktop\\jetlearn\\OpenCV\\images_collage"
os.chdir(path)
total_width=0
total_height=0
number_image=0
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") :
        number_image=number_image+1
print(number_image)

width=1200
height=800

mc="mycollage.avi"
video=r.VideoWriter(mc,0,0.5,(width,height))


for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") :
        image=r.imread(file)
        my_image=r.resize(image,(width,height))
        video.write(my_image)
        
        