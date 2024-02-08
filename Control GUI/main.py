import pyautogui
import time
import keyboard
import threading
import sys

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

def background_killer():
    pyautogui.hotkey('win')
    pyautogui.typewrite('Teams work', interval=0.1)
    pyautogui.hotkey('enter')
    while True:
        pyautogui.moveTo(500, 500, 0.3, pyautogui.easeInQuad)
        pyautogui.moveTo(700, 500, 0.3, pyautogui.easeInQuad)
        pyautogui.moveTo(700, 700, 0.3, pyautogui.easeInQuad)
        pyautogui.moveTo(500, 700, 0.3, pyautogui.easeInQuad)

background_thread=threading.Thread(target=background_killer)
background_thread.daemon=True
background_thread.start()

print("Press 'esc' to stop the program")
while True:
    if keyboard.is_pressed('esc'):
        sys.exit(0)
