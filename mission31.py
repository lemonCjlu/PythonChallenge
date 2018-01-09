from PIL import Image

url = 'http://www.pythonchallenge.com/pc/ring/grandpa.html'

#从csv文件中获取list形式的数据，该些数据是图片的像素值
with open('yankeedoodle.csv') as f:
    content = f.read()
    data = [float(i.strip()) for i in content.split(',')]
    length = len(data)
    print(data)

#根据width*height=length（7367）,获取图片的宽，高
width_height = [x for x in range(2, 7367) if 7367%x == 0]
width = width_height[0]
height = width_height[1]

#新建一个图像
# img = Image.new('L', (width,height))
# img.putdata(data,256) # pixel = value*scale + offset.即data中的元素为value,scale为256
# img2 = img.transpose(Image.ROTATE_90)
# img3 = img2.transpose(Image.FLIP_TOP_BOTTOM) #Transpose image (flip or rotate in 90 degree steps)
# img3.show()
# img3.close()


#根据上述图片显示的公式计算n=str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]，以下等同于res = [int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])]且data中元素为str类型，x是由三个str元素构成的元组，所以x[0][5]表示取第一个元素中第5个字符
res = list()
for index in range(0,length-3,3):
    # print(data[index], n)
    n = int(format(data[index], '.6f')[5] + format(data[index+1], '.6f')[5] + format(data[index+2], '.6f')[6])
    res.append(n)
print(res)
aaa = bytes(res)
print(aaa)
print(aaa.decode())
