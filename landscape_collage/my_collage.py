import cv2 as r
import os
from PIL import Image

path="C:\\Users\\Bhulku\\Desktop\\jetlearn\\OpenCV\\landscape_collage"
os.chdir(path)
total_width=0
total_height=0
number_image=0
print()
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") :
        number_image=number_image+1
        info=Image.open(file)
        width,height=info.size
        total_height=total_height+height
        total_width=total_width+width
print(number_image)

mean_width=total_width//number_image
mean_height=total_height//number_image


mc="collage.avi"
video=r.VideoWriter(mc,0,0.5,(mean_width,mean_height))


for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") :
        image=r.imread(file)
        my_image=r.resize(image,(mean_width,mean_height))
        video.write(my_image)
        
        