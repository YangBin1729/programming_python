#!python3
# bookrank.py - 多线程下载图书排名信息调用

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen

regex = compile('#([\d,]+) in Books')
amzn = 'http://amazon.com/dp/'
isbns = {'0132269937': 'Core Python Programming',
         '0132356139': 'Python Web Development with Django',
         '0137143419': 'Python Fundamentals'}


def get_ranking(isbn):
    page = urlopen('%s%s'%(amzn, isbn))
    data = page.read()
    page.close()
    return regex.findall(data)[0]


def _show_ranking(isbn):
    print('- %r ranked %s'%(isbns[isbn], get_ranking(isbn)))


def _main():
    print('At ', ctime(), ' on Amazon...')
    for isbn in isbns:
        Thread(target=_show_ranking, args=(isbn,)).start()
        

@register()
def _atexit():
    print('all Done at:', ctime())


if __name__ == '__main__':
    _main()
