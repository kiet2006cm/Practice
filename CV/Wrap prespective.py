import cv2 as cv
import numpy as np

def ex1():
    w,h=250,350
    img=cv.imread("bai.jpg")
    pots=np.float32([[194,54],[240,123],[94,114],[133,189]])
                    #lấy trong paint
    pots2=np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix= cv.getPerspectiveTransform(pots,pots2)
    newimg= cv.warpPerspective(img,matrix,(w,h))

    cv.imshow("Tach bai",img)
    cv.imshow("card",newimg)
    cv.waitKey(0)
def ex2():
    #815x600
    w,h=300,400
    img=cv.imread("iron_pickaxe.png")
    pots=np.float32([[300,40],[673,40],[100,565],[673,565]])
                    #lấy trong paint
    pots2=np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix= cv.getPerspectiveTransform(pots,pots2)
    newimg= cv.warpPerspective(img,matrix,(w,h))

    cv.imshow("first",img)
    cv.imshow("pickaxe",newimg)
    cv.waitKey(0)
