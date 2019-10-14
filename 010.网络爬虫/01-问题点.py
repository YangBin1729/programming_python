#1.json.dump(result,path):
#Serialize result as a JSON formatted stream to path (a.write()-supporting file-like object).
#urlopen(url).read(),Object of type 'bytes' is not JSON serializable
#urlopen(url).read().decode('utf-8'),'str' object也不能用于dump函数！！！
#result到底何种形式的结果才行？？？？？？

#2.file-like interface??????
