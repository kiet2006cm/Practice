from tkinter import E
import cv2 as cv
import numpy as np

img= cv.imread('cutegirl.jpg')
kernel= np.ones((3,3),np.uint8)
# ma trận càng lớn nét càng đậm

grayimg= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blurimg= cv.GaussianBlur(grayimg,(7,7),0)
                                #hiểu nôm na cái () này là độ mờ theo trục x,y bắt buộc là số lẻ
cannyimg= cv.Canny(img,180,180)
                        #theo quan sát thì có lẽ số càng nhỏ nét vẽ càng dày đặc
dialationimg= cv.dilate(cannyimg,kernel,iterations=1)
# giãn nở 
erosionimg= cv.erode(dialationimg,kernel,iterations=1)
# xói mòn 


cv.imshow('gray',grayimg)
cv.imshow("NANIIIIIII",blurimg)
cv.imshow("canny",cannyimg)
cv.imshow("Dialation img",dialationimg)
cv.imshow('eroded img',erosionimg)

cv.waitKey(0)