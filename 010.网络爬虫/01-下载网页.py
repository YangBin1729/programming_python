from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return(None)
    try:
        bsObj=BeautifulSoup(html.read(),'html.parser')
        title=bsObj.body.h1
    except AttributeError as e:
        return(None)
    retutn(title)

六度分隔理论：
#获取所有链接：
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj=BeautifulSoup(html,'html.parser')
for link in bsObj.findAll('a'):
    #findAll和findall的差别
    if 'href' in link.attrs:
        print(link.attrs['href'])

#选出词条链接：
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj=BeautifulSoup(html,'html.parser')
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

#链接爬虫,随机选择一个子链接：
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html=urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    return(bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')))
links=getLinks('/wiki/Kevin_Bacon')
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getLinks(newArticle)

#链接爬虫，获取所有子链接：
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll('a',href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

#链接爬虫，获取所有子链接，查找所需信息：
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面缺少一些属性！不用担心！')
    for link in bsObj.findAll('a',href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print('---------------\n',newPage)
                pages.add(newPage)
                getLinks(newPage)

#完整爬虫：
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
pages=set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includeUrl):
    includeUrl=urlparse(includeUrl).scheme+'://'+urlparse(includeUrl).netloc
    #为什么对链接进行如此处理？？？？？？
    internalLinks=[]
    for link in bsObj.findAll('a',href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(includeUrl+links.attrs['href'])
            else:
                internalLinks.append(links.attrs['href'])
    return(internalLinks)

def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    for link in bsObj.findAll('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(links.attrs['href'])
    return(externalLinks)

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,'html.parser')
    externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        print('No externalLins,looking around the site for one')
        domain=urlparse(startingPage).scheme+'://'+urlparse(startingPage).netloc
        internalLinks=getInternalLinks(bsObj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

#Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj,domain)
    externalLinks = getExternalLinks(bsObj,domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

followExternalOnly("http://oreilly.com")

allIntLinks.add("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")
