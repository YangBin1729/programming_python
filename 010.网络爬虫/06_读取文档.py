#1.纯文本
编码类型


#2.CSV
from urllib.request import urlopen
from io import StringIO
import csv
data=urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii','ignore')
dataFile=StringIO(data)
#1.列表形式
csvReader=csv.reader(dataFile)
for row in csvReader:
    print(row)
#2.dict形式
dictReader=csv.DictReader(dataFile)
print(dictReader.fieldnames)#键组成的列表
for row in dictReader:
    print(row)

#3.PDF
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConvert
from pdfminer.layout import LAParams
from io import StringIO,open

def readPDF(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConvert(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return(content)

pdfFile=urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString=readPDF(pdfFile)
print(outputString)
pdfFile.close()




#4.WORD
