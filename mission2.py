#! /user/bin/python
'''
Author:lemon
Date:2017/9/19
Method: translate string according to a letters into a letter, for example: abc into cde
'''
import string

# string.ascii_lowercase
# print(ord('a'))
#ss = {ord(i):i for i in string.ascii_lowercase}

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

def translate(x):
    if x not in string.ascii_lowercase:
        return x
    else:
        return chr((ord(x)-97)%25+ 1 + 97)


s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr
q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
# a = ''.join(list(map(encode, list(s))))
# print(a)
#
# raw_url = '''map'''
# b = ''.join(list(map(encode, list(raw_url))))
# print(b)
print(translate('y'))






