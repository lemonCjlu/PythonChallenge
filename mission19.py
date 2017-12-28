from PIL import Image
import gzip
import difflib

url = 'http://www.pythonchallenge.com/pc/hex/bin.html'
#deltas.gz是两列int数据
with gzip.open('deltas.gz') as f:
    file_content = f.read().decode()
print(file_content)


#读取每列数据，并以二进制形式保存，注意换行符'\n'
column1 = list()
column2 = list()
f = gzip.open('deltas.gz')
for line in f:
    column1.append(line[:53].decode() + '\n')
    column2.append(line[56:].decode())
f.close()

#对两列数据进行比较，得到比较结果是list，元素为str
#查看比较的结果，结果列表中元素类型是str,且有些元素前缀含‘+’，有些含‘-’，有些为空格
d = difflib.Differ()
result = list(d.compare(column1,column2))
print(result)

#分析比较结果，对每一行进行分析即分别提取元素前缀含‘+’，含‘-’，含空格的元素，对字符串转换为list且该元素为数字。对该含整数的list进行二进制转换
f1 = open('f1.png', 'wb')
f2 = open('f2.png', 'wb')
f3 = open('f3.png', 'wb')
for line in result:
    if line[0] == '-':
        bs = bytes([int(data,16) for data in line.strip('- ').strip().split(" ") if data])
        f1.write(bs)
    elif line[0] == '+':
        bs = bytes([int(data, 16) for data in line.strip('+ ').strip().split(" ") if data])
        f2.write(bs)
    else:
        bs = bytes([int(data, 16) for data in line.strip('  ').strip().split(" ") if data])
        f3.write(bs)
f1.close()
f2.close()
f3.close()

