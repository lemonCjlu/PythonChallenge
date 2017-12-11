from PIL import Image
url = 'http://www.pythonchallenge.com/pc/return/cat.html'

im = Image.open('wire.png')
new_im = Image.new('RGB',(100,100), (255,255,255)) #建立一个100*100的图片
x,y,p = -1, 0, 0
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
d = 200
#从左到右绘制第一条边，然后接着最右边点从上到下绘制第二条边，再接着该点从右到左绘制第三条边，最后接着该终点从下到上绘制第四条边，从而形成一个正方形。从头开始循环绘制第二个正方形
while d//2 > 0:        #可以循环绘制一个正方形的次数，即总像素点为100，每次画完一个正方形，减去2个像素点
    for v in delta:
        for i in range(d//2): #每次画一条边，可循环的像素点数（100， 99， 99， 98，98，97，97，96）
            x = x + v[0]
            y = y + v[1]
            new_im.putpixel((x, y), im.getpixel((p, 0)))
            p = p + 1
        d = d - 1

new_im.show()

#从左到右绘制第一条边
# for i in range(100):
#     x = x + 1
#     y = y + 0
#     new_im.putpixel((x,y), im.getpixel((p,0)))
#     p = p + 1
#
#最右边点从上到下绘制第二条边
# for i in range(100-1):
#     x = x + 0
#     y = y + 1
#     new_im.putpixel((x,y), im.getpixel((p,0)))
#     p = p + 1
#
#该点从右到左绘制第三条边
# for i in range(100-1):
#     x = x - 1
#     y = y + 0
#     new_im.putpixel((x,y), im.getpixel((p,0)))
#     p = p + 1
#
#最后接着该终点从下到上绘制第四条边
# for i in range(100-2):
#     y = y - 1
#     new_im.putpixel((x,y), im.getpixel((p,0)))
#     p = p + 1
