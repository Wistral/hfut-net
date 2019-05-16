import requests
from info_parse import *
from bs4 import BeautifulSoup


ac, psw = login()
raw_headers = """POST /0.htm HTTP/1.1
Host: 172.18.2.2
Connection: kep-alive
Content-Length: 67
Pragma: no-cache
Cache-Control: no-cache
Origin: http://172.18.3.3
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://172.18.3.3/0.htm
Accept-Encoding: gzip, deflate
Accept-Language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en;q=0.6,ja;q=0.5
"""

raw_data = """
DDDDD: {}
upass: {}
0MKKey: %B5%C7+%C2%BC%A1%A1Login
v6ip: 
""".format(ac, psw)

headers = parse_headers(raw_headers)
data = parse_headers(raw_data)
html = requests.post('http://172.18.3.3/0.htm', headers=headers, data=data)
res = BeautifulSoup(html.text, 'lxml')
msg = res.title.string
if msg == '登录成功':
    print(msg)
else:
    print('登录失败')
    with open('info.txt', 'w') as f:
        f.close()
# print(res.title.string)


