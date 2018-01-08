from PIL import Image

url = 'http://www.pythonchallenge.com/pc/ring/guido.html'
img = Image.open('bell.png')
green = [i[1] for i in img.getdata()] #获取像素值即RGB中的G
differ = [abs(a-b) for a , b in zip(green[::2], green[1::2])]#比较相邻两列的不同，构成新的新的列表
res = filter(lambda x:x!=42, differ)
print(green)
print(differ)
a = bytes(list(res))
print(a.decode())