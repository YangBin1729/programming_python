#!python3
# mtsleep_with_lock.py - 使用锁避免输出混乱


from atexit import register
from threading import Thread, current_thread, Lock
from time import ctime, sleep
from random import randrange


class CleanOutSet(set):
    def __str__(self):
        return ','.join(x for x in self)


loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutSet()
lock = Lock()


def loop(nsec):
    myname = current_thread().name

    lock.acquire()
    remaining.add(myname)
    print(f'{ctime()} started {myname}')
    lock.release()

    sleep(nsec)

    lock.acquire()
    remaining.remove(myname)
    print(f'{ctime()} completed {myname} at {nsec}s')
    print('remaining:%s'%(remaining or 'None'))
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('All done at:', ctime())

if __name__ == '__main__':
    _main()