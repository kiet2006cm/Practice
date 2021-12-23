import time
import win32api,win32con,win32ui,win32gui
import numpy as np
import os
import cv2 as cv
import pyautogui


def bam():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    #(450,270)(450,935) to (1465,270)(1465,935)
    # x(450) y(270) xe(1465) ye(935)
    # (450,270,1015,665) # Screen

# def lwn():
#     def l(hwnd,ctx):
#         if win32gui.IsWindowVisible(hwnd):
#             print(hex(hwnd),win32gui.GetWindowText(hwnd))
#     win32gui.EnumWindows(l,None)
# lwn()                         #Lấy tên app

def screenshot():
    w = 0 #điền
    h = 0  #điền

    hwnd = win32gui.FindWindow(None) # ,windowname 
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj,w,h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img= np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h,w,4)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd,wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img[...,:3]
    img=np.ascontiguousarray(img)
    return img

os.chdir(os.path.dirname(os.path.abspath(__file__)))


while True:
    ss=screenshot()

    cv.imshow('Hi',ss)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


