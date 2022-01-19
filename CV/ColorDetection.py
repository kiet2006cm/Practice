import cv2 as cv
import numpy as np

def Filter(img,consolename="Filter"):
    def hihi(a):
        pass
    cv.namedWindow("TrackBars")
    cv.resizeWindow("TrackBars",640,280)
    cv.createTrackbar("Hue Min","TrackBars",0,179,hihi)
    cv.createTrackbar("Hue Max","TrackBars",179,179,hihi)
    cv.createTrackbar("Sat Min","TrackBars",0,255,hihi)
    cv.createTrackbar("Sat Max","TrackBars",255,255,hihi)
    cv.createTrackbar("Val Min","TrackBars",0,255,hihi)
    cv.createTrackbar("Val Max","TrackBars",255,255,hihi)
    while True:
        hsvimg=cv.cvtColor(img,cv.COLOR_BGR2HSV)
        h_min=cv.getTrackbarPos("Hue Min","TrackBars")
        h_max=cv.getTrackbarPos("Hue Max","TrackBars")
        s_min=cv.getTrackbarPos("Sat Min","TrackBars")
        s_max=cv.getTrackbarPos("Sat Max","TrackBars")
        v_min=cv.getTrackbarPos("Val Min","TrackBars")
        v_max=cv.getTrackbarPos("Val Max","TrackBars")
        l=np.array([h_min,s_min,v_min])
        u=np.array([h_max,s_max,v_max])
        mask=cv.inRange(hsvimg,l,u)
        imgresult=cv.bitwise_and(img,img,mask=mask)
        cacimg= np.hstack([img,hsvimg,imgresult])
        cv.imshow(f"{consolename}",cacimg)
        cv.imshow('BackGround',mask)
        cv.waitKey(1)
if __name__=="__main__":
    img=cv.imread("cutegirl.jpg")
    img= cv.resize(img,(200,200))
    Filter(img)