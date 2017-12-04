from PIL import Image
url = 'http://www.pythonchallenge.com/pc/return/evil.html'

with open('evil2.gfx', 'rb') as f:
    data = f.read()
print(len(data))

for i in range(5):
   with open('image%d.jpg'%i, 'wb') as f:   #%的用法
       f.write(data[i::5])                      #通过切片获取数据并进行写

