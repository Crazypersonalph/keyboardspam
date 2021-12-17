import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

time.sleep(5)
def spam():
    x = input('type what you want to spam')
    keyboard.type(x)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
while True:
    spam()
    time.sleep(0.10)
               
