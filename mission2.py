#! /user/bin/python

import string

# string.ascii_lowercase
# print(ord('a'))
ss = {ord(i):i for i in string.ascii_lowercase}

s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr
q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

def encode(x):
    if x not in string.ascii_lowercase:
        return x
    i = ord(x)
    res = 0
    if i in range(97,121):
        res = i + 2
    elif i == 121:
        res = 97
    elif i == 122:
        res = 98
    else:
        pass
    return chr(res)



# a = ''.join(list(map(encode, list(s))))
# print(a)
#
# raw_url = '''map'''
# b = ''.join(list(map(encode, list(raw_url))))
# print(b)






