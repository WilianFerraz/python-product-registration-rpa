import time
import pyautogui

# Wait 5 seconds to position the mouse cursor over the target field
time.sleep(5)
print(pyautogui.position())

# Test scroll direction and intensity on the page
pyautogui.scroll(200)
