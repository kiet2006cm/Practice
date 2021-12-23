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
# (450,270,1015,665) # Screen

# cần biết x địch x ta => chuyển x ta đến x địch
yta=742 # RBG: (72,75,97) (giao động tầm 4 đơn vị mỗi màu)
xta=941
# xta lúc đầu là 941 sau mỗi đợt di chuyển sẽ là thành [xdich-1]
# xdich =  pyautogui.center(dich.png)


imgdich = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\dich.png") 
imgdich = np.array(imgdich)

imgta = cv2.imread("C:\\Users\\HP\Downloads\Documents\\Kiet\\py\\PhagameBim\\ta.png") 
imgta = np.array(imgta)

def choemgananhthemchutnua(phim,x):
    global yta
    r=0
    b=0
    g=0
    while (r not in range(65,80)) and (b not in range(68,82)) and (g not in range(90,105)):

        huhihuhi=pyautogui.pixel(x+40,yta+40)
        r=int(huhihuhi[0])
        b=int(huhihuhi[1])
        g=int(huhihuhi[2])
        pyautogui.keyDown(phim)
    pyautogui.click()    
    pyautogui.keyUp(phim)

while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen(imgdich, region= (450,270,1015,665), confidence=0.5) != None:
        bruhbruhbruhlmao= list(pyautogui.locateOnScreen(imgdich, region= (450,270,1015,665), confidence=0.5))
        xdich= int(bruhbruhbruhlmao[0]+45)
        if xdich < xta:
            choemgananhthemchutnua(x=xdich,phim='left')
        elif xdich > xta:
            choemgananhthemchutnua(x=xdich,phim='right')
        else:
            pyautogui.click()
        xta = xdich

    