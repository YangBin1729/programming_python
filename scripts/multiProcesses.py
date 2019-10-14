#!python3
# multiProcesses.py - 多进程及进程池的使用

import os
import time
import random
from multiprocessing import Process, Pool, Queue
from simpleTimer import fn_timer


@fn_timer
def do_sample_task(name):
    print(f'Run child process {os.getpid()},task name is {name}')
    time.sleep(1.2)
    return(name)


@fn_timer
def test_simple_multi_process():
    p1 = Process(target=do_sample_task, args=('task1',))
    p2 = Process(target=do_sample_task, args=('task2',))
    print('Process will start')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Process end')


@fn_timer
def test_process_pool():
    pool = Pool()
    results = []
    task_name = []
    for i in range(7):
        task_name.append(f'task{i}')
    results = pool.map_async(do_sample_task, task_name)
    print('Many Process will start...')
    pool.close()
    pool.join()
    print(f'All processes end,results is:{results.get()}')


def main():
    test_simple_multi_process()
    print('\n\n\n')
    test_process_pool()

if __name__ == '__main__':
    main()