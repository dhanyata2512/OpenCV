import cv2 as r
import numpy as np

# red=np.uint8([[[0,0,225]]])
# hsv=r.cvtColor(red,r.COLOR_BGR2HSV)
# print(hsv)

v=r.VideoCapture("video.mp4")
for i in range(60):
    s,bg=v.read()
    if s is False:
        continue

l_bound=np.array([150,50,50])
u_bound=np.array([180,255,255])

while v.isOpened():
    yn,frame=v.read()
    if yn is False:
        break
    hsv_frame=r.cvtColor(frame,r.COLOR_BGR2HSV)
    mask1=r.inRange(hsv_frame,l_bound,u_bound)    
    mask1=r.morphologyEx(mask1,r.MORPH_OPEN,np.ones((5,5)))
    mask2=r.bitwise_not(mask1)
    r1=r.bitwise_and(bg,bg,mask=mask1)
    r2=r.bitwise_and(frame,frame,mask=mask2)
    fr=r.add(r1,r2)
    rotated=r.rotate(fr,r.ROTATE_90_COUNTERCLOCKWISE)
    r.imshow("hi",rotated)
    key=r.waitKey(4)
    if key == 27:
        break

    

