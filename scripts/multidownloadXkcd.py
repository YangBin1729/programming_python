#!python3
# multidownloadXkcd.py - Download XKCD comics using multipile threads.

import requests
import os
import bs4
import threading


os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s...' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)
        comicElem = soup.select('#comic.image')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading images %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(1, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')