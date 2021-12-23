import pyautogui
import time
import keyboard
import random
import win32api,win32con
def bam(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(425,885)[0] == 0:
        bam(425,885)
    if pyautogui.pixel(550,885)[0] == 0:
        bam(550,885)
    if pyautogui.pixel(675,885)[0] == 0:
        bam(675,885)
    if pyautogui.pixel(800,885)[0] == 0:
        bam(800,885)
# (425,830) 
# (550,830)  
# (675,830)  
# (800,830) 
