import cv2 as cv
import numpy as np

def caro(img,img2,size=(400,400),loop=(4,4),consolename="Caro"):
    img=cv.resize(img,size)
    img2=cv.resize(img2,size)
    w,h=loop
    wl=[]
    wl2=[]
    hl=[]
    for i in range(1,w+1):
        if i%2==0:
            wl.append(img)
            wl2.append(img2)
        else:
            wl.append(img2)
            wl2.append(img)
    ngang= np.hstack(wl)
    ngang2= np.hstack(wl2)
    for i in range(1,h+1):
        if i%2==0:
            hl.append(ngang)
        else:
            hl.append(ngang2)
    doc= np.vstack(hl)
    cv.imshow(f"{consolename}",doc)
    cv.waitKey(0)

if __name__=="__main__":
    img= cv.imread("cutegirl.jpg")
    img2= cv.imread("nhanngu.jpg")
    caro(img,img2,size=(100,100),loop=(5,5))