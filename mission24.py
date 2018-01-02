import this, string

url = 'http://www.pythonchallenge.com/pc/hex/ambiguity.html'

bef = string.ascii_lowercase
aft = [bef[i-13] for i in range(len(bef))]
table = str.maketrans(bef, ''.join(aft))
s = 'va gur snpr bs jung?'
s_aft = s.translate(table)
print(s_aft)


#method2:
print("method2:")
import this
s = 'va gur snpr bs jung?'
res = ''.join([this.d.get(c,c)for c in s]) #this.d是一个字典
print(res)

