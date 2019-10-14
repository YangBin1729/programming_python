#1.urlretrieve
import os
from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup
downloadedDir='downloaded'
baseUrl='http://pythonscraping.com'
def getAbsUrl(baseUrl,source):
    if source.startswith('http://www.'):
        url='http://'+source[11:]
    if source.startswith('http://'):
        url=source
    elif source.startswith('www.'):
        url='http://'+source[4:]
    else:
        url=baseUrl+'/'+source
    if baseUrl not in url:
        return(None)
    return(url)
def getDownload(baseUrl,absoluteUrl,downloadedDir):
    path=absoluteUrl.replace('www.','')
    path=path.replace(baseUrl,'')
    path=downloadedDir+path
    directory=os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return(path)
html=urlopen('http://www.pythonscraping.com')
bsObj=BeautifulSoup(html,'html.parser')
downloadList=bsObj.findAll(src=True)
for download in downloadList:
    fileUrl=getAbsUrl(baseUrl,download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownload(baseUrl,fileUrl,downloadedDir))

#2.CSV:Comma-Seperated Values,逗号分隔值
import csv
csvFile=open('D:\\000workspace\\test.csv','w+')
try:
    writer=csv.writer(csvFile)
    writer.writerow(('No','No+2','No*2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()

url='https://en.wikipedia.org/wiki/Comparison_of_text_editors'
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen(url)
bsObj=BeautifulSoup(html,'html.parser')
table=bsObj.findAll('table',{'class':'wikitale'})[0]
#该语句搜索条件存在问题？？？？？？？？？
rows=table.findAll('tr')
csvFile=open('D:\\000workspace\\editors.csv','wt',newline=' ',encoding='utf-8')
writer=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()


#3.MySQL
