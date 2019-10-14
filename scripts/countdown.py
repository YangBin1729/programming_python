#!python3
# countdown.py - A simple count down script.

import time
import subprocess



timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=',')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['start', 'Mad World.wav'], shell=True)