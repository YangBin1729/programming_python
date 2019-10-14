#!python3
# simpleTimer.py - 简单的计时器,比较多线程、线程池


import time
from functools import wraps
import threading
from multiprocessing.dummy import Pool




def fn_timer(func):
    @wraps(func)
    def func_timer(*args, **kwargs):
        t0 = time.time()
        results = func(*args, **kwargs)
        t1 = time.time()
        print(f'[finished function:{func.__name__} in {t1-t0}s]')
        return results
    return func_timer




def music(name):
    print(f"I'm listening to music {name}")
    time.sleep(1)


def movie(name):
    print(f"I'm watching movie {name}")
    time.sleep(5)


@fn_timer
def single_thread():
    for i in range(10):
        music(i)
    for i in range(2):
        movie(i)


@fn_timer
def multi_thread():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=music, args=(i,)))
    for i in range(2):
        threads.append(threading.Thread(target=movie, args=(i,)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()


@fn_timer
def use_pool():
    pool = Pool()
    pool.map(music, range(10))
    pool.map(movie, range(2))
    pool.close()
    pool.join()




if __name__ == '__main__':
    single_thread()
    multi_thread()
    use_pool()