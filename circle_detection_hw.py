import cv2 as r
import numpy as np

ghost=r.imread("ghost.png",r.IMREAD_COLOR)

g_image=r.cvtColor(ghost,r.COLOR_BGR2GRAY)
m_blur=r.medianBlur(g_image,3)
hci=r.HoughCircles(m_blur,r.HOUGH_GRADIENT,1,5,param1=80,param2=45 ,minRadius=10,maxRadius=50)
print(hci)

if hci is not None:   
    result=np.uint(np.round(hci))
    for x,y,ra in result[0]:
        print(x,y,ra)
        r.circle((ghost),(x,y),ra,(240,32,160),7)
        r.imshow("hii",ghost)
        r.waitKey(0)