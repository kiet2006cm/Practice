import cv2 as cv
import numpy as np

def contours(img,consolename="Contours"):
    img=cv.resize(img,(200,200))
    grayscaleimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blurimg=cv.GaussianBlur(img,(129,129),1)
    allimginone= np.hstack((img,blurimg))

    cv.imshow(f'{consolename}',allimginone)
    cv.imshow('GrayScale',grayscaleimg)
    cv.waitKey(0)

if __name__=="__main__":
    img=cv.imread("cutegirl.jpg")
    contours(img)