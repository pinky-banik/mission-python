from platform import python_branch
import pyautogui
import time 
pyautogui.alert('This is an alert box')
time.sleep(3)
for i in range(1,5):
  pyautogui.write('I love python ', interval=0.25)
  pyautogui.press('enter')
