#!python3
# candy.py - 利用锁和信号量来模拟糖果机。该糖果机有5个可用的卡槽保存糖果，所有的槽满了，就不能添加糖果；都空了，就不能买到糖果

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
max = 5
candytray = BoundedSemaphore(max)


def refill():
    lock.acquire()
    print('Refilling candy...')
    try:
        candytray.release()
    except ValueError:
        print('full,skipping')
    else:
        print('OK')
    lock.release()


def buy():
    lock.acquire()
    print('Buying candy...')
    if candytray.acquire(False):
        print('OK')
    else:
        print('empty,skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('THE Candy Machine (full with %d bars!)' % max)
    Thread(target=consumer, args=(randrange(nloops, nloops+max+2),)).start()
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print('All done at:', ctime())


if __name__ == '__main__':
    _main()

