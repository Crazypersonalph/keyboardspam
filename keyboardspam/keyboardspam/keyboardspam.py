import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

x = input('type what you want to spam')
time.sleep(5)
def spam():
    keyboard.type(x)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
while True:
    spam()
    time.sleep(0.10)
               
