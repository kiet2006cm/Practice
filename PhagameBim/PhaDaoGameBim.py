from types import NoneType
import pyautogui
import keyboard
import cv2
import numpy as np
import time

#(450,270)(450,935) to (1465,270)(1465,935)
## Khung hình ##
x1=450        ##
y1=270        ##
x2=1465       ##
y2=935        ##
## Khung hình ##
# (450,270,1015,665) 

imgdich = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\dich.png") 
imgdich = np.array(imgdich)

imgmoinhu = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\moinhu.png") 
imgmoinhu = np.array(imgmoinhu)

imgta = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\ta.png") 
imgta = np.array(imgta)

hu1canh = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\hu1canh.png")
hu1canh = np.array(hu1canh)

hu2canh = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\hu2canh.png")
hu2canh = np.array(hu2canh)

##450,715 , 450 890 ## 1465,715 ##1465,890

def leftorright(xdich,xta):
    if xdich > xta:
        return "right"
    if xdich < xta:
        return "left"

def mylocation():
    if pyautogui.locateOnScreen(imgta, region= (450,715,1015,175), confidence=0.45,grayscale=True) != None:
        lmaolamo= list(pyautogui.locateOnScreen(imgta, region= (450,715,1015,175), confidence=0.45,grayscale=True))
    elif pyautogui.locateOnScreen(hu1canh, region= (450,715,1015,175), confidence=0.45,grayscale=True) != None:
        lmaolamo= list(pyautogui.locateOnScreen(hu1canh, region= (450,715,1015,175), confidence=0.45,grayscale=True))
    else:
        lmaolamo= list(pyautogui.locateOnScreen(hu2canh, region= (450,715,1015,175), confidence=0.45,grayscale=True))
    xta= int(lmaolamo[0])
    return(xta)
def enemylocation():
    if pyautogui.locateOnScreen(imgdich, region= (450,270,1015,665), confidence=0.6,grayscale=True) != None:
        bruhbruhbruhlmao= list(pyautogui.locateOnScreen(imgdich, region= (450,270,1015,665), confidence=0.6,grayscale=True))
    else:
        bruhbruhbruhlmao=pyautogui.locateOnScreen(imgmoinhu, region= (450,270,1015,665), confidence=0.50,grayscale=True)
    xdich=int(bruhbruhbruhlmao[0])
    return xdich
def choemgananhthemchutnua():
    xdich= enemylocation()
    xta=mylocation()
    while xta not in range(xdich,xdich+90):
        xta=mylocation()
        pyautogui.keyDown(leftorright(xdich,xta))
        if abs(xdich - xta) > 450:
            time.sleep(0.25)
        if abs(xdich-xta) >250 and abs(xdich-xta) < 450:
            time.sleep(0.15)
        if abs(xdich-xta) >100 and abs(xdich-xta) < 250:
            time.sleep(0.05)
        if abs(xdich-xta) <100:
            time.sleep(0.015)
        pyautogui.keyUp(leftorright(xdich,xta))
        pyautogui.click(interval=0.001)
        if xta in range(xdich,xdich+90):
            break

while keyboard.is_pressed('q') == False:
    if (pyautogui.locateOnScreen(imgdich, region= (450,270,1015,665), confidence=0.6,grayscale=True) !=None 
    or pyautogui.locateOnScreen(imgmoinhu, region= (450,270,1015,665), confidence=0.50,grayscale=True) != None):
        choemgananhthemchutnua()
