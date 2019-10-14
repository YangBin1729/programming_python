#!python3
# mtsleepE.py - Thread子类化，而不是直接对其实例化，定制线程对象

import threading
from time import sleep, ctime

loops = (4,2)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.name = name
        self.args = args

    def run(self):
        self.func(*args)


def loop(nloop, nsec):
    print(f'start loop {nloop} at:{ctime()}')
    sleep(nsec)
    print(f'loop {nloop} done at:{ctime()}')


def main():
    print(f'starting at:{ctime()}')
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print(f'all done at:{ctime()}')


if __name__ == '__main__':
    main()
