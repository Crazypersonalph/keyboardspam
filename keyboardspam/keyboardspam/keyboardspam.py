import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

time.sleep(5)
def spam():
    keyboard.type('why')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
while True:
    spam()
    time.sleep(0.10)
               
