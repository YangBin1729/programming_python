#!python3
# multiThreads.py - 爬虫实例比较单线程与多线程


import threading
import time
from multiprocessing.dummy import Pool
import requests
from simpleTimer import fn_timer


urls = ['https://baike.baidu.com/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6',
        'https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80',
        'https://baike.baidu.com/item/%E5%9F%BA%E9%87%91%E4%BC%9A',
        'https://baike.baidu.com/item/%E5%88%9B%E6%96%B02.0',
        'https://baike.baidu.com/item/%E5%95%86%E4%B8%9A%E8%BD%AF%E4%BB%B6',
        'https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81',
        'https://baike.baidu.com/item/OpenBSD',
        'https://baike.baidu.com/item/%E8%A7%A3%E9%87%8A%E5%99%A8',
        'https://baike.baidu.com/item/%E7%A8%8B%E5%BA%8F/71525',
        'https://baike.baidu.com/item/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80',
        'https://baike.baidu.com/item/C%2B%2B',
        'https://baike.baidu.com/item/%E8%B7%A8%E5%B9%B3%E5%8F%B0',
        'https://baike.baidu.com/item/Web/150564',
        'https://baike.baidu.com/item/%E7%88%B1%E5%A5%BD%E8%80%85',
        'https://baike.baidu.com/item/%E6%95%99%E5%AD%A6',
        'https://baike.baidu.com/item/Unix%20shell',
        'https://baike.baidu.com/item/TIOBE',
        'https://baike.baidu.com/item/%E8%AF%BE%E7%A8%8B',
        'https://baike.baidu.com/item/MATLAB',
        'https://baike.baidu.com/item/Perl']



@fn_timer
def download_using_single_thread(urls):
    resps = []
    for url in urls:
        resp = requests.get(url, allow_redirects=False)
        resps.append(resp)
    return resps


@fn_timer
def download_using_multithread(urls):
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=requests.get, args=(url,), kwargs={'allow_redirects': False}))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    return threads


@fn_timer
def download_using_pool(urls):
    pool = Pool()
    reps = pool.map(requests.get, urls)
    pool.close()
    pool.join()
    return reps


def main():
    download_using_single_thread(urls)
    download_using_multithread(urls)



if __name__ == '__main__':
    main()