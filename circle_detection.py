import cv2 as r
import numpy as np

circle=r.imread("eye.jpg",r.IMREAD_COLOR)

g_image=r.cvtColor(circle,r.COLOR_BGR2GRAY)
m_blur=r.medianBlur(g_image,3)
hc=r.HoughCircles(m_blur,r.HOUGH_GRADIENT,1,13,param1=50,param2=25 ,minRadius=20,maxRadius=30)
print(hc)

if hc is not None:   
    result=np.uint(np.round(hc))
    for x,y,ra in result[0]:
        print(x,y,ra)
        r.circle((circle),(x,y),ra,(240,32,160),6)
        r.imshow("hi",circle)
        r.waitKey(0)