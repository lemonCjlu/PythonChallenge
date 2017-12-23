from PIL import Image

img = Image.open('mozart.gif')
high = img.size[1]
width = img.size[0]

#因为粉色像素在每行都有，所以粉色像素的个数必定能整除高度值，从而得到粉色像素值为195
red_counts = [count for count in img.histogram() if count%high == 0 and count != 0]   #Image.histogram(mask=None, extrema=None):Returns a histogram for the image. The histogram is returned as a list of pixel counts, one for each pixel value in the source image
print(img.histogram().index(2400)) #像素值范围为0-255，计算每个像素值含有的像素个数。即索引位置即为像素值

# new_img = Image.frombytes('P',img.size, bytes([195]*(high*width))) #颜色受色板影响
# new_img.show()

# new_img = img.copy()
# new_img.frombytes(bytes([195]*(high*width)))
# new_img.show()

#method0:
# new_img = img.copy()
# #将平移所有每行紫色所在像素后的所有像素值到首位如原来是[a,b,b,c]->平移后为[b,b,c,a]
# for y in range(high):
#     row = list()
#     new_row = list()
#     for x in range(width):
#         row.append(img.getpixel((x,y)))
#     new_row1 = row[row.index(195):] + row[:row.index(195)]
#
#     new_row2 = [195]*5 + row[:row.index(195)] + row[row.index(195)+5:]
#     # print('1:%row' ,row)
#     # print('2:%row' ,new_row1)
#     # print('3:%row', new_row2)
#
#     for x in range(width):
#         new_img.putpixel((x,y), new_row1[x])
#
# new_img.show()
# img.close()

#method1:
print('method1:')
from PIL import Image, ImageChops
img = Image.open('mozart.gif')
hight = img.size[1]
width = img.size[0]

new_img = img.copy()
for y in range(hight):
    box = (0,y,width,y+1)
    row_img = img.crop(box)
    index = row_img.tobytes().index(195) #计算195像素值所在的索引位置
    new_row = ImageChops.offset(row_img, -index) #Returns a copy of the image where data has been offset by the given distances,[a,b,c]，b的索引为1，那各元素平移后的索引应为-1.0，1即[b,c,a]
    new_img.paste(new_row, box) #pastes another image into this image.
new_img.show()
img.close()


