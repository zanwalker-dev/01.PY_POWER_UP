import pyautogui
import time
import pandas 

pyautogui.PAUSE = 0.5

# Access the company website: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Open Chrome
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
pyautogui.write("chrome")
pyautogui.press("return")
