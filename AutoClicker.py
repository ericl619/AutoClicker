import pyautogui
import time
import datetime

pyautogui.PAUSE = 0.01
clicks = input('Press enter to start')

position = 1600
try:
    while position > 500:
        position = pyautogui.position()[0]
        pyautogui.click(interval=0.01)

except:
    print('interrupted')