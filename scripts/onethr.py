#!python3
# onethr.py - 不利用多线程的示例

from time import sleep, ctime


def loop0():
    print(f'start loop 0 at:{ctime()}')
    sleep(4)
    print(f'loop 0 done at:{ctime()}')


def loop1():
    print(f'start loop 1 at:{ctime()}')
    sleep(2)
    print(f'loop 1 done at:{ctime()}')


def main():
    print(f'starting at:{ctime()}')
    loop0()
    loop1()
    print(f'all done at:{ctime()}')


if __name__ == '__main__':
    main()