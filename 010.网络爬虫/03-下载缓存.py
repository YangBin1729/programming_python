from urllib.parse import urlparse
import time
class Throttle():
    def __init__(self,delay):
        self.delay=delay
        self.domains={}
    def wait(self,url):
        domain=urlparse(url).netloc
        last_accessed=self.domains.get(domain)
        if self.delay>0 and last_accessed is not None:
            sleep_secs=self.delay-(time.time()-last_accessed)
            if sleep_secs>0:
                time.sleep(sleep_secs)
        self.domains[domain]=time.time()

from random import choice
import requests

class Downloader:
    def __init__(self,delay=5,user_agent='wswp',proxies=None,cache={}):
        self.throttle=Throttle(delay)
        self.user_agent=user_agent
        self.proxies=proxies
        self.num_retries=None
        self.cache=cache
    def __call__(self,url,num_retries=2):
        self.num_retries=num_retries
        try:
            result=self.cache[url]#有取值功能，__getitem__
            print('Loaded from cache:',url)
        except KeyError:
            result=None
        if result and self.num_retries and 500<=result['code']<600:
            result=None
        if result is None:#没有缓存时
            self.throttle.wait(url)
            proxies=choice(self.proxies) is self.proxies else None
            headers={'User-Agent':self.user_agent}
            result=download(url,headers,proxies)
            if self.cache:
                self.cache[url]=result
            #将下载结果保存到缓存中,有赋值功能，__setitem__
            return(result['html'])
    def download(self,url,headers,proxies,num_retries):
        print('Downloading:',url)
        try:
            resp=requests.get(url,headers=headers,proxies=proxies,timeout=self.timeout)
            #返回 <Response> object
            #headers和proxies前为什么没有self？？？跟函数调用接口__call__有关？？？
            html=resp.text
            #解码后的html文件
            if self.num_retries and 500<=resp.status_code<600:
                self.num_retries-=1
                return(self.download(url,headers,proxies))
        except requests.exceptions.RequestException as e:
            print('download error:',e)
            return({'html':None,'Code':500})
        return({'html':html,'code':resp.status_code})

#链接爬虫，支持缓存：
def link_crawler(...,num_retries=2,cache={}):
    crawl_queue=[seed_url]
    seen={seed_url:0}
    rp=get_robots(seed_url)
    D=Downloader(delay=delay,user_agent=user_agent,proxies=proxies,cache=cache)
    while crawl_queue:
        url=crawl_queue.pop()
        if rp.can_fetch(user_agent,url):
            depth=seen.get(url,0)
            if depth=max_depth:
                continue
            html=D(url,num_retries=num_retries)
            if not html:
                continue

#磁盘缓存
import os
import re
from urllib.parse import urlsplit
import jason

class DiskCache:
    def __init__(self,cache_dir='cache',max_len=255):
        self.cache_dir=cache_dir
        #存放缓存文件的文件夹，D:\\000workspace\\cache
        self.max_len=max_len
    def url_to_path(self,url):
        #处理系统导致的命名限制
        #创建完整的文件地址及名字
        components=urlsplit(url)
        path=components.path
        if not path:
            path='/index.html'
        elif path.endswith('/'):
            path+='index.html'
        filename=components.netloc+path+components.query
        filename=re.sub('[^/0-9a-zA-z\-.,;_]','_',filename)
        filename='/'.join(sef[:self.max_len] for seg in filename.split('/'))
        #最终的文件名中包含 / 符号，所以最终的文件名是最后一个/后的字符串
        return(os.path.join(self.cache_dir,filename))
    def __getitem__(self,url):
        path=self.url_to_path(url)
        if os.path.exists(path):
            return(json.load(path))
        else:
            raise(KeyError(url+'does not exist'))
    def __setitem__(self,url,result):
        path=self.url_to_path(url)
        #path为完整的路径，包含文件名index.html
        folder=os.path.dirname(path)
        #返回path所包含的嵌套文件夹，不包含path中的文件名
        if not os.path.exists(folder):
            os.makedirs(folder)
        json.dump(result,path)


import re
from urllib import robotparser
from urllib.parse import urljoin
from chp3.downloader import downloader

def get_robots_parser(robots_url):
    rp=robotparser.RobotFileParser()
    #This class provides a set of methods to read, parse and answer questions about a single robots.txt file.
    rp.set_url(robots_url)
    #Sets the URL referring to a robots.txt file.
    rp.read()
    #Reads the robots.txt URL and feeds it to the parser.
    return(rp)

def get_links(html):
    webpage_regx=re.compile('''<a[^>]+href=["'](.*?)["']''',re.IGNORECASE)
    return(webpage_regx.findall(html))

def link_crawler(start_url,link_regx,robots_url=None,user_agent='wswp',proxies=None,delay=3,max_depth=4,num_retries=2,cache={},scraper_callback=None):
    crawl_queue=[start_url]
    seen={}
    if not robots_url:
        robots_url='{}/robots.txt'.format(start_url)
    rp=get_robots_parser(robots_url)
    D=Downloader(delay=delay,user_agent=user_agent,proxies=proxies,cache=cache)
    while crawl_queue:
        url=crawl_queue.pop()
        if rp.can_fetch(user_agent,url):
            #using the parsed robots.txt decide if useragent can fetch url
            depth=seen.get(url,0)
            if depth=max_depth:
                print('Skipping %s due to depth'%url)
                continue
            html=D(url,num_retries=num_retries)
            if not html:
                continue
            if scraper_callback:
                links=scraper_callback(url,html) or []
            else:
                links=[]
            for link in get_links(html) + links:
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt:', url)
