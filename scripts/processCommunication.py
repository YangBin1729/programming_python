#!python3
# processCommunication.py - 测试进程间的通信

import os
import time
import random
from multiprocessing import Pool, Process, Queue
from simpleTimer import fn_timer


def write(q):
    for value in ['A','B','C']:
        print(f'Put value:{value} to queue')
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get(True)
        print(f'Get value:{value} from queue')


def test_communication():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


def main():
    test_communication()

if __name__ == '__main__':
    main()