import pyautogui
from randompass import randompassword
import time

# print(pyautogui.displayMousePosition())

pyautogui.click(1547,982)
for i in range(15):
    r = randompassword()
    pyautogui.write(r)
    pyautogui.press('enter')
