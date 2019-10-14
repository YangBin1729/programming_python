#a multithreaded crawler

import threading
'''
threading.Thread
--->>> A class that represents a thread of control.

__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
--->>>*target* is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.

is_alive(self)
--->>>Return whether the thread is alive

isDaemon(self)

start(self)
--->>>Start the thread's activity.It must be called at most once per thread object
join(self, timeout=None)
--->>>Wait until the thread terminates.
run(self)
--->>>Method representing the thread's activity.
'''

    threads = []
    print(max_threads)
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)#删除不活动的线程
        while len(threads) < max_threads and crawl_queue:
            thread = threading.Thread(target=process_queue)#创建线程对象，目标可调用对象
            thread.setDaemon(True)#设为主线程
            thread.start()#启动线程
            threads.append(thread)
        print(threads)
        for thread in threads:
            thread.join()#等待线程终结

#a multiprocessing crawler
from redis import StrictRedis
'''
StrictRedis()
--->>>Implementation of the Redis protocol.

__init__(self, host='localhost', port=6379, db=0, password=None,...)

llen(self, name)
--->>>Return the length of the list ``name``

lpush(self, name, *values)
--->>>Push ``values`` onto the head of the list ``name``

 sadd(self, name, *values)
--->>>Add ``value(s)`` to set ``name``
