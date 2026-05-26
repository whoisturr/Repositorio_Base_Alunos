import pyautogui as at
import time

at.hotkey("win","r") #Essa função aperta duas teclas ao mesmo tempo.
time.sleep(1)

at.write("chrome", 0.2) #Essa função escreve
at.press("enter") #Essa função pressiona a tecla.

time.sleep(3)
at.write("https://www.youtube.com", interval=0.1)
at.press("enter")

time.sleep(5)

at.press("tab")

time.sleep(1)

at.write("curso de python", interval=0.1)
at.press("enter")

time.sleep(5)

at.press("tab")
time.sleep(1)

at.press("enter")