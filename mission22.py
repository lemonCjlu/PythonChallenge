import  zlib, bz2

url = 'http://www.pythonchallenge.com/pc/hex/copper.html'
with open('package.pack', 'rb') as f:
    data = f.read()

#首先解压pack数据，得到结果仍是zlib压缩数据，重复解压，发现有bz数据存在，重复解压zlib数据和bz数据，发现有以b'\x9cx'结尾的zlib数据，所以需要再次以zlib解压,
# 最后得到解密数据：b'sgol ruoy ta kool'-》look at your logs即打印
result = ''
while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        result = result + ' '
    elif data.startswith(b'BZ'):
        data = bz2.decompress(data)
        result = result + '#'
    elif data.endswith(b'\x9cx'):
        data = zlib.decompress(data[::-1])
        result = result + '\n'
    else:
        print(data)
        break
print(result)
