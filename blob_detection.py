import cv2 as r
import numpy as np

blob=r.imread("blob.jpg",r.IMREAD_COLOR)

params=r.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=90
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=True
params.minConvexity=0.8
params.filterByInertia=True
params.minInertiaRatio=0.7

detector=r.SimpleBlobDetector_create(params)
key_points=detector.detect(blob)
print(key_points)
result=r.drawKeypoints(blob,key_points,np.zeros((1,1)),(208,224,64),r.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
length=len(key_points)
r.putText(result,"Number of Circles:"+ str(length),(20,500),r.FONT_ITALIC,1,(240,32,160))
r.imshow("HI",result)
r.waitKey(0)




