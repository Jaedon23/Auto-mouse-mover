from tracemalloc import stop
from unittest import result
import pyautogui
import time 
import random
while True in range (0,500):
    x = random.randint(0,500)
    y = random.randint(0,500)
    pyautogui.moveTo(x,y)

    localtime = time.localtime()
    result = time.strftime("%I:%M:$S %p", localtime)

    print ('Moveed at ' + str(result) + ' (' + str(x) + ',' + str(y) + ')')
    time.sleep(20)
    