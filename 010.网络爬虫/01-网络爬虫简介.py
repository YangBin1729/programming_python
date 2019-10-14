#1.1 robots.txt
#https://www.douban.com/robots.txt
#1.2 网站地图
#1.3 网站大小
#1.4 识别网站所用技术
#？？？？？？？
#1.5 寻找网站所有者
import whois

#2.1 下载网页
from urllib.request import urlopen
def download(url):#url必须为完整的网址，如http不可缺少！！！
    html=urlopen(url)
    return(html.read())#html文件调用read()方法后，html为空文件了
捕获错误
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError
def download(url):
    try:
        html=urllib.request.urlopen(url).read()
    except (URLError,HTTPError,ContentTooShortError) as e:#as语法的本质
        print('Download error:',e.reason)
        html=None
    return(html)
特定错误的特定处理,5xx错误重新下载指定次数：
def download(url,num_retries=3):
    print('Downloading:',url)
    try:
        html=urllib.request.urlopen(url).read()
    except (URLError,HTTPError,ContentTooShortError) as e:#e是什么对象，都有些什么属性
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return(download(url,num_retries-1))
    return(html)
设置用户代理：
def download(url,user_agent='wswp',num_retries=2):
    print('Downloading:',url)
    request=urllib.request.Request(url)
    #Request对象，URL request的抽象
    request.add_header('User-agent',user_agent)
    #添加header到Request对象，只有HTTP handlers会处理headers
    try:
        html=urllib.request.urlopen(request).read()
    except (URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return(download(url,num_retries-1))
        return(html)
#2.2 网站地图爬虫
import re
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError
def download(url,user_agent='wswp',num_retries=2,charset='utf-8'):
    print('Downloading:',url)
    request=urllib.request.Request(url)
    request.add_header('User-agent:',user_agent)#运行时会出现：Invalid header name b'User-Agent。header里key名称特定？？？？
    try:
        resp=urllib.request.urlopen(request)#<class 'http.client.HTTPResponse'>
        cs=resp.headers.get_content_charset()#返回‘utf-8’及其它编码格式，resp.headers：<http.client.HTTPMessage object>，
        if not cs:
            cs=charset
        html=resp.read().decode(cs)#按‘utf-8’格式解码下载的网页
    except (URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return(download(url,num_retries-1))
    return(html)
def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)#不同的网站地图，不同的正则表达式规则！！！！！
    for link in links:
        html=download(link)
crawl_sitemap('http://example.webscraping.com/sitemap.xml')#该网站已经失效？？？？？？？？？？


#2.3 ID遍历爬虫
#http://example.webscraping.com/places/default/view/Afghanistan-1
#与 http://example.webscraping.com/places/default/view/-1 等价，最后面数字即为该网页ID
import itertools
def crawl_site(url):
    for page in itertools.count(1):
        pg_url='{}{}'.format(url,page)
        html=download(pg_url)
        if html is None:
            break
        else:
            pass
数据库ID不连续，发生错误多次即退出
def crawl_site(url,max_errors=5):
    for page in itertools.count(1):
        pg_url='{}{}'.format(url,page)
        html=download(pg_url)
        if html is None:
            num_errors+=1
            if num_errors==max_errors:
                break
            else:
                num_errors = 0


#2.4 链接爬虫
import re
def link_crawler(start_url,link_regex):
    crawl_queue=[start_url]
    while crawl_queue:
        #该函数有问题：
        #首先下载初始链接 1,crawl_queue=[]，找出其中所有符合link_regex格式的链接[11,12,13]，
        #再下载链接13，crawl_queue=[11,12]，在13中再找出其中所有符合link_regex格式的链接[131,132,133]，crawl_queue=[11,12，131,132,133]，
        #再下载133，，crawl_queue=[11,12，131,132]，在133中再找出其中所有符合link_regex格式的链接[1331,1332,1333]，
        #再下载1333，crawl_queue=[11,12，131,132,1331,1332]，......
        url=crawl_queue.pop()
        html=download(url)
        if not html:
            continue
#找出所有链接中符合link_regex格式的链接
        for link in get_links(html):
            if re.match(link_regex,link):
                crawl_queue.append(link)
                #更改为crawl_queue.insert(0,link)
#找出所有链接
def get_links(html):
    webpage_regex=re.compile("""<a[^>]+href=["'](.*?)["']""",re.IGNORECASE)#包含链接的格式：<a href="/places/default/view/Afghanistan-1">
    return(webpage_regex.findall(html))

def link_crawl(start_url,link_regex):
    #只下载start_url中的所有链接，链接网页中的网页不下载
    html=download(start_url)
    for link in get_link(html):
        if re.match(link_regex,link):
            download(link)
def get_link(html):
    webpage_regx=re.compile("""<a[^>]+href=["'](.*?)["']""",re.IGNORECASE)
    return(webpage_regx.findall(html))

link_crawl('http://example.webscraping.com/places/default/index/0','.*?/(index|view)/')

下载的链接都是相对链接，不是绝对链接
from urllib.parse import urljoin
def link_crawl(start_url,link_regx):
    crawl_queue=[start_url]
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        if html is not None:#满足该条件时，会不断返回执行while循环
            continue####这个if语句有问题！！！！！！！！！！！！！
        for link in get_links(html):
            if re.match(link_regex,link):
                abs_link=urljoin(start_url,link)
                crawl_queue.append(abs_link)


link_crawl('http://example.webscraping.com/places/default/index/0','.*?/(view)/')#下载所有国家页面

防止重复下载：
def link_crawl(start_url,link_regx):
    crawl_queue=[start_url]
    seen=set(crawl_queue)
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        if html is not None:
            continue
        for link in get_links(html):
            if re.match(link_regex,link):
                abs_link=urljoin(start_url,link)
                if abs_link not in seen:
                    seen.add(abs_link)
                    crawl_queue.append(abs_link)


高级功能：
1.解析robots.txt,避免下载禁止爬取的URL
from urllib import robotparser
def get_robots_parser(robots_url):
    rp=robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return(rp)
def link_crawler(start_url,link_regex,robots_url=None,user_agent='wswp'):
    if not robots_url:
        robots_url='{}/robots.txt'.format(start_url)
    rp=get_robots_parser(robots_url)
    crawl_queue=[start_url]
    while crawl_queue:
        url=crawl_queue.pop()
        if rp.can_fetch(user_agent,url):
            html=download(url,user_agent=user_agent)
            if html is not None:
                continue
            for link in get_links(html):
                if re.match(link_regex,link):
                    crawl_queue.append(link)
        else:
            print('Blocked by robots.txt:',url)

2.支持网络代理，代理服务器。和用户代理的区别
proxy='http:\\myproxy.net:1234'
proxy_support=urllib.request.ProxyHandler({'http':proxy})
opener=urllib.request.build_opener(proxy_support)
#Create an opener object from a list of handlers.
#The opener will use several default handlers, including support for HTTP, FTP and when applicable HTTPS.
urllib.request.install_opener(opener)
???????????????
def download(url,user_agent='wswp',num_retries=2,charset='utf-8',proxy=None):
    print('Downloading:',url)
    request=urllib.request.Request(url)
    request.add_header('user_agent',user_agent)
    try:
        if proxy:
            proxy_support=urllib.request.ProxyHandler({'http':proxy})
            opener=urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            resp=urllib.request.urlopen(request)
            cs=resp.headers.get_content_charset()
            if not cs:
                cs=charset
            html=resp.read().decode(cs)
    except (URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return(download(url,num_retries-1))
    return(html)







3.下载限速，
from urllib.parse import urlparse
import time
class Throttle():
    def __init__(self,delay):
        self.delay=delay
        self.domains={}
    def wait(self,url):
        domain=urlparse(url).netloc
        #urlparse(url)将一个URL解析成六个部分：<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        #urlparse('https://www.douban.com/robots.txt')->ParseResult(scheme='https', netloc='www.douban.com', path='/robots.txt', params='', query='', fragment='')
        last_accessed=self.domains.get(domain)
        if self.delay>0 and last_accessed is not None:
            sleep_secs=self.delay-(time.time()-last_accessed)
            #time.time()现在时间，last_accessed下载上一个网页的时间，距离下载上一个网页过去的时间(time.time()-last_accessed)
            #下载下一个网页时间last_accessed+delay,所以还需等待delay-(time.time()-last_accessed)长时间
            if sleep_secs>0:
                time.sleep(sleep_secs)#休眠sleep_secs长时间
        self.domains[domain]=time.time()#当前时间

throttle=Throttle(5)#创建延迟下载类实例，下载完一个网页后延迟5s下载另一个
throttle.wait(url_1)#下载第一个网页，即时下载
throttle.wait(url_2)#下载第二个网页，休眠一段时间。
#用于for循环中！！！！

html = download(url, user_agent=user_agent, num_retries=num_retries,proxy=proxy,charset=charset)

将其嵌入到有多次下载的程序中，下载完一个链接，等待一段时间，再下载下一个链接！！！！

4.避免爬虫陷阱：
def link_crawler(...,max_depth=4):
    seen={}
    if rp.can_fetch(useragent,url):
        depth=seen.get(url,0)
        if depth==max_depth:
            print('skipping %s due to depth'%url)
            continue
        for link in get_links(link_regx,html):
            if re.match(link_regex,link):
                abs_link=urljoin(start_url,link)
                if abs_link not in seen:
                    seen[abs_link]=depth+1
                    crawl_queue.append(abs_link)

requests版本的下载爬虫：
import requests
def download(url,user_agent='wswp',num_retries=2,proxies=None):
    print('Downloading:',url)
    headers={'User-Agent:',user_agent}
    try:
        resp=requests.get(url,headers=headers,proxies=proxies)
        #将之前需自己定义的user_agent,proxies集成进该函数了
        #Sends a GET request,return <Response> object
        html=resp.text
        #same as:html=urlopen(url).read().decode('utf-8')
        if resp.status_code>=400:
            print('Download Error:',resp.text)
            html=None
            if num_retries and 500<=resp.status_code<600:
                return(download(url,num_retries-1))
    except requests.exceptions.RequestException as e:
        print('Download error:',e.reason)
        html=None

#resp-><Response> object
#resp.content->Content of the response, in bytes.
#resp.text->Content of the response, in unicode.
.......
