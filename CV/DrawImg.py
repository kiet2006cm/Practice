import cv2 as cv
import numpy as np
from random import randint


def shocngang(img,khoangcach=10):
    i=0
    h,w,c=img.shape
    while i <= h:
        img[i:i+1,:w]= randint(0,255),randint(0,255),randint(0,255)
            #rbg hoặc gbr gì đó
        i=i+khoangcach

def socngangchaytrenmanhinh(img,khoangcach=10,thoigianmoisoc=50,consolename="TV_90s",loop=False):
    i=0
    h,w,c=img.shape
    if loop==False:
        while i <= h:
            img[i:i+1,:w]= randint(0,255),randint(0,255),randint(0,255)
            i=i+khoangcach
            cv.imshow(f"{consolename}",img)
            cv.waitKey(thoigianmoisoc)
    elif loop==True:
        while True:
            if i >=h:
                i=0
            img[i:i+1,:w]= randint(0,255),randint(0,255),randint(0,255)
            i=i+khoangcach
            cv.imshow(f"{consolename}",img)
            cv.waitKey(thoigianmoisoc)

def daux(img,thickness=5,color=(0,255,255)):
    h,w,c=img.shape
    cv.line(img,(0,0),(w,h),color,thickness)
    cv.line(img,(w,0),(0,h),color,thickness)

def penis(img,color=(0,0,0),thickness=cv.FILLED,cudai=200,curong=50,r=40):
    h,w,c=img.shape
    x1=int(w/2)-int(curong/2)
    y1=int(h/2)-int(cudai/2*1.5)
    x2=int(w/2)+int(curong/2)
    y2=int(h/2)+int(cudai/2/1.5)
    img=cv.rectangle(img,(x1,y1),(x2,y2),color,thickness)
    img=cv.circle(img,(int(w/2-r+1),y2+int(r/5)),r,color,thickness)
    img=cv.circle(img,(int(w/2+r-1),y2+int(r/5)),r,color,thickness)

def showhinh(img,name="Picture"):
    cv.imshow(f"{name}",img)
    cv.waitKey(0)

if __name__=="__main__":
    bgrngaunhien=(randint(0,255),randint(0,255),randint(0,255))
    img=cv.imread("cutegirl.jpg")
    img=cv.resize(img,(400,400))

    cv.putText(img,"Fuck this shit",(30,30),cv.FONT_HERSHEY_COMPLEX,1,bgrngaunhien,2)
                                                         #FONTSCALE: độ mờ

    daux(img)
    penis(img,color=bgrngaunhien)
    showhinh(img,"Random Girl")

