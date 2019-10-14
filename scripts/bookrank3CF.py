#!python3
# bookrank3CF.py - 利用 concurrent.futures模块的图书排名


from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen

regex = compile('#([\d,]+) in Books')
amzn = 'http://amazon.com/dp/'
isbns = {'0132269937': 'Core Python Programming',
         '0132356139': 'Python Web Development with Django',
         '0137143419': 'Python Fundamentals'}


def get_ranking(isbn):
    with urlopen('%s%s' % (amzn, isbn)) as page:
        return str(regex.findall(page)[0], 'utf-8')


def _main():
    print('At ', ctime(), ' on Amazon...')
    with ThreadPoolExecutor(3) as excutor:
        for isbn, ranking in zip(isbns, excutor.map(get_ranking, isbns)):
            print('- %r ranked %s' % (isbns[isbn], ranking))
    print('all Done at:', ctime())


if __name__ == '__main__':
    _main()
