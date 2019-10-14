#!python3
# mtfacfib.py - 单线程与多线程分别执行斐波那契、阶乘与累加

from MyThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.05)
    if x < 2:
        return 1
    return fib(x-2)+fib(x-1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x*fac(x-1)


def my_sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x+my_sum(x-1)


func = [fib, fac, my_sum]
n = 120

def main():
    nfuncs = range(len(func))
    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('Starting ', func[i].__name__, 'at:', ctime())
        print(func[i](n))
        print(func[i].__name__, 'finished at:', ctime())

    print('\n***MULTIPILE THREADs')
    threads = []
    for i in nfuncs:
        t = MyThread(func[i], (n,), func[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    print('ALL DONE')


if __name__ == '__main__':
    main()