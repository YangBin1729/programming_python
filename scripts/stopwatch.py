#!python3
# stopwatch.py - A simple stopwatch program.

import time
print('Press ENTER to begin.Afterwards,press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()       # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime, 3)
        totalTime = round(time.time()-startTime, 3)
        print('Lap #%s:%s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:       # Handle the Ctrl-C exception
    print('\nDone')
