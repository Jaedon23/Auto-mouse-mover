from tracemalloc import stop
from unittest import result
import pyautogui
import time
import random

seconds= input("How often (seconds) would you like the mouse to move?: ")
seconds = int(seconds)
movements = []

while True in range(0, 500):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y)
    z = (str(x) + "," + str(y))

    localtime = time.localtime()
    result = time.strftime("%I:%M:$S %p", localtime)

    print('Moved at ' + str(result) + ' (' + str(x) + ',' + str(y) + ')')
    movements.append(str(z))

    time.sleep(seconds)
