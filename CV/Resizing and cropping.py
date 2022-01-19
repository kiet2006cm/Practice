from ctypes import resize
import cv2 as cv

img= cv.imread('nhanngu.jpg')
resizeimg= cv.resize(img,(200,600))
cropimg= resizeimg[450:600,10:130]

# cv.imshow('Nhân thường',img)
# cv.imshow('Nhân kéo chân',resizeimg)
cv.imshow('Cắt chân nhân ngu',cropimg)
cv.waitKey(0)
