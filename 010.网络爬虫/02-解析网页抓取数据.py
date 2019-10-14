1-re:
import re
from chp1.advanced_link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Aland-Islands-2'
html = download(url)
#type(html)为<class 'str'>
#urlopen(url).read()得到的是bytes-like object,正则表达式的string模式不适用该对象
#urlopen(url).read().decode('utf-8')即为<class 'str'>，可用正则表达式匹配

print(re.findall(r'<td class="w2p_fw">(.*?)</td>', html))
print(re.findall('<td class="w2p_fw">(.*?)</td>', html)[1])
print(re.findall('<tr id="places_area__row"><td class="w2p_fl"><label id="places_area__label" class="readonly" for="places_area" >Area: </label></td><td class="w2p_fw">(.*?)</td>', html))
print(re.findall('''<tr id="places_area__row">.*?<td\s*class=["']w2p_fw["']>(.*?)</td>''', html))


2——BeautifulSoup
from bs4 import BeautifulSoup
from pprint import pprint
import html5lib
broken_html='<ul class=country><li>Area<li>Population</ul>'
soup=BeautifulSoup(broken_html,'html.parser')
#<ul class="country"><li>Area<li>Population</li></li></ul>;代码闭合，但<li>标签嵌套
soup=BeautifulSoup(broken_html,'html5lib')#两种编译器的区别：html.parser,html5lib
#<html><head></head><body><ul class="country"><li>Area</li><li>Population</li></ul></body></html>
#更完整，更正确
soup.li#标签li内的内容
soup.body#标签body类的内容

soup.find('ul',attrs={'class':'country'})
soup.find(attrs={'class':'country'})#<ul class="country"><li>Area</li><li>Population</li></ul>

soup.find('li')#<li>Area</li>
soup.find_all('li')#[<li>Area</li>, <li>Population</li>]
#find,及find_all方法都是针对HTML标签的，即<>内部的标签，其它文本无效

soup.find('li').text#返回<li>标签内的文本

3——Lxml
from lxml.html import fromstring,tostring
broken_html='<ul class=country><li>Area<li>Population</ul>'
tree=fromstring(broken_html)#tree为<Element ul at 0x1d87e8c8598>,fromstring参数为文本
good_html=tostring(tree,pretty_print=True)
print(good_html)#b'<ul class="country">\n<li>Area</li>\n<li>Population</li>\n</ul>\n'

from urllib.request import urlopen
html=urlopen('http://example.webscraping.com').read()
tree=fromstring(html)#fromstring参数为一文件
td=tree.cssselect('tr')#cssselect的选取规则
#[<Element tr at 0x1f2d2d53318>, <Element tr at 0x1f2d2d1bef8>, <Element tr at 0x1f2d2ea0458>, <Element tr at 0x1f2d2ec51d8>, <Element tr at 0x1f2d2ec53b8>]
country=td[0].text_content()#文本内容

cssselect的选取规则！！！！！！！！！！！！！！

xpath,与cssselect类似，但不同的选取规则！！！！！

HTML标签的Family Trees：
td[0].getchildren()
td[0].getparent()
td[0].getprevious()
td[0].getnext()


性能比较：
FIELDS=('area','population','iso','country','capital','continent','tld','currency_code','currency_name','phone','postal_code-format','postal_code_regex','languages','neighbours')
import re
def re_scraper(html):
    results={}
    for field in FIELDS:
        results[field]=re.search('<tr id="places_%s_row">.*?<td class="w2p_fw">(.*?)</td>'%field,html).groups()[0]
    return(results)

from bs4 import BeautifulSoup
def bs_scraper(html):
    soup=BeautifulSoup(html,'html.parser')
    results={}
    for field in FIELDS:
        results[field]=soup.find('table').find('tr',id='places_%s_row'%field).find('td',class_='w2p_fw').text_content()
    return(results)

from lxml.html import fromstring
def lxml_scraper(html):
    tree=fromstring(html)
    results={}
    for field in FIELDS:
        results[field]=tree.cssselect('table>tr#places_%s_row>td.w2p_fw'%field)[0].text_content()
    return(results)

def lxml_xpath_scraper(html):
    tree=fromstring(html)
    results={}
    for field in FIELDS:
        results[field]=tree.xpath('//tr[@id="places_%s_row"]/td[@class="w2p_fw"]'%field)[0].text_content()
    return(results)

import time
import re
import urllib.request
def download(url):
    return(urllib.request.urlopen(url).read())

NUM_ITERATIONS=1000
html=download('http://example.webscraping.com/places/default/view/United-Kingdom-239')
scrapers=[('Regular expressions',re_scraper),('BeautifulSoup',bs_scraper),('Lxml',lxml_scraper),('Xpath',lxml_xpath_scraper)]
for name,scraper in scrapers:
    start=time.time()
    for i in range(NUM_ITERATIONS):
        if scraper==re_scraper:#re模块会缓存搜索，需清除以公平比较
            re.purge()
        result=scraper(html)
        assert result['area']=='244,820 square kilometres'
    end=time.time()
    print('%s:%.2f seconds'%(name,end-start))

为链接爬虫添加抓取回调！！！！！！！！！！！！？？？？？？？？？？？？
