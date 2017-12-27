import  urllib.request as request
import re
from urllib.parse import unquote_plus, unquote_to_bytes, quote_plus  #The URL quoting functions focus on taking program data and making it safe for use as URL components by quoting special characters and appropriately encoding non-ASCII text.
import bz2
import xmlrpc.client

url = 'http://www.pythonchallenge.com/pc/return/balloons.html'
init_val = '12345'
info = ''
#循环获取所有网页的cookie的内容
while True:
    init_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+ init_val
    response_obj = request.urlopen(init_url)
    content = str(response_obj.read(), encoding='utf-8')
    cookie = response_obj.info().get('Set-Cookie')
    print(response_obj.getheaders())
    print(content)


    m = re.search('info=(.*?);', cookie) #利用正则获取info中cookie内容
    if m:
     info = info + m.group(1)
    else:
        pass

    m = re.search('and the next busynothing is (\d+)', content)#利用正则获取url
    if m:
        init_val = m.group(1)
    else:
        break

#获取并解析cookie的bz格式数据
res = unquote_to_bytes(info.replace("+", " ")) #获取bz数据
res_decode = bz2.decompress(res)
print(res_decode)

#使用xmlrpc.client.ServerProxy
server_proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(server_proxy.phone('Leopold'))

#发送请求并设置info中的cookie
phone_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
request_obj = request.Request(phone_url, headers={'Cookie':'info='+ quote_plus(msg)})
print(str(request.urlopen(request_obj).read(), encoding='utf-8'))




