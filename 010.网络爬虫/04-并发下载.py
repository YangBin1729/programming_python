import csv
from zipfile import zipFile
from io import BytesIO,TextIOWrapper
import requests

resp=requests.get('http://s3.amazonaws.com/alexa-static/top-lm.csv.zip',stream=True)
urls=[]
with ZipFile(BytesIO(resp.content)) as zf:
    csv_filename=zf.namelist()[0]
    with zf.open(csv_filename) as csv_file:
        for _,website in csv.reader(TextIOWrapper(csv_file)):
            urls.append('http://'+website)

from urllib import robotparser
def get_robots_parser(robots_url):
    try:
        rp=robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return(rp)
    except Exception as e:
        print('Error finding robots_url:',robots_url,e)

import re
def get_links(html):
    webpage_regx=re.compile('''<a[^>]+href["'](.*?)["']''',re.IGNORECASE)
    return(webpage_regx.findall(html))

def threaded_crawler(start_url,link_regex,user_agent='wswp',proxies=None,delay=3,max_depth=4,num_retries=2,cache={},max_threads=10,scraper_callback=None):
    if isinstance(start_url,list):
        crawl_queue=start_url
    else:
        crawl_queue=[start_url]
    seen,robots={},{}
    D=Downloader(delay=delay,user_agent=user_agent,proxies=proxies,cache=cahce)
    def process_queue():
        while crawl_queue:
            url=crawl_queue.pop()
            no_robots=False
            if not url or 'http' not in url:
                continue
            domain='{}://{}'.format(urlparse(url).scheme,urlparse(url).netloc)
            rp=robots.get(domain)
            if not rp and domain not in robots:
                robots_url='{}/robots.txt'.format(domain)
                rp=get_robots_parser(start_url)
                if not rp:
                    no_robots=True
                robots[domain]=rp
            elif domain in robts:
                no_robots=True
            if no_robots or rp.can_fetch(user_agent,url):
                depth=seen.get(url,0)
                if depth==max_depth:
                    print('skipping %s due to depth'%url)
                    continue
                html=D(url,num_retries=num_retries)
                if not html:
                    continue
                if scraper_callback:
                    links=scraper_callback(url,html) or []
                else:
                    links=[]
                for link in get_links(html)+links:
                    if re.match(link_regex, link):
                        if 'http' not in link:
                            if link.startswith('//'):
                                link = '{}:{}'.format(urlparse(url).scheme, link)
                            elif link.startswith('://'):
                                link = '{}{}'.format(urlparse(url).scheme, link)
                            else:
                                link = urljoin(domain, link)
                        if link not in seen:
                            seen[link] = depth + 1
                            crawl_queue.append(link)
            else:
                print('Blocked by robots.txt:', url)
    threads=[]
    print(max_threads)
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads)<max_threads and crawl_queue:
            thread=threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        print(threads)
        for thread in threads:
            thread.join()
        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    from chp4.alexa_callback import AlexaCallback
    from chp3.rediscache import RedisCache
    import argparse

    parser = argparse.ArgumentParser(description='Threaded link crawler')
    parser.add_argument('max_threads', type=int, help='maximum number of threads',
                        nargs='?', default=5)
    parser.add_argument('url_pattern', type=str, help='regex pattern for url matching',
                        nargs='?', default='$^')
    par_args = parser.parse_args()
    AC = AlexaCallback()
    AC()
    start_time = time.time()
    threaded_crawler(AC.urls, par_args.url_pattern, cache=RedisCache(),
                     max_threads=par_args.max_threads)
    print('Total time: %ss' % (time.time() - start_time))
