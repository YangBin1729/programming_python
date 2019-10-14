#API:应用编程接口(Application Programming Interface)
#用HTTP协议向API发起请求以获取某种信息，API会用XML(extensible markup Language,可扩展标记语言)或JSON格式返回服务器响应的信息

#获取信息：
GET：浏览器输入网址
POST：填写账号、密码登陆
PUT：更新账号、密码
DELETE：
#验证：
token:令牌
token="<your api key>"
webRequest=urllib.request.Request('http://myapi.com',headers={'token':token})
html=urlopen(webRequest)
#服务器响应：
反馈JSON或XML格式的数据
