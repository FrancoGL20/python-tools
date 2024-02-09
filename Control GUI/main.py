import pyautogui

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

pyautogui.moveTo(1500,500)

print("start slow, end fast")
pyautogui.moveTo(500, 500, 1, pyautogui.easeInQuad)     # start slow, end fast
print("start fast, end slow")
pyautogui.moveTo(1500, 500, 1, pyautogui.easeOutQuad)    # start fast, end slow
print("start and end fast, slow in middle")
pyautogui.moveTo(500, 500, 1, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
print("start and end slow, fast in middle")
pyautogui.moveTo(1500, 500, 1, pyautogui.easeInBounce)   # bounce at the end
print("start and end fast, slow in middle")
pyautogui.moveTo(500, 500, 1, pyautogui.easeInElastic)  # rubber band at the end
print("start and end slow, fast in middle")