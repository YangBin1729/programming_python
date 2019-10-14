#!python3
# mtsleepF.py - 产生竞态条件(race condition)的情况


from atexit import register
from threading import Thread, current_thread
from time import ctime, sleep
from random import randrange


class CleanOutSet(set):
    def __str__(self):
        return ','.join(x for x in self)


loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutSet()


def loop(nsec):
    myname = current_thread().name
    remaining.add(myname)
    print(f'{ctime()} started {myname}')
    sleep(nsec)
    remaining.remove(myname)
    print(f'{ctime()} completed {myname} at {nsec}s')
    print('remaining:%s'%(remaining or 'None'))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('All done at:', ctime())

if __name__ == '__main__':
    _main()