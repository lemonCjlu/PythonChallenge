#! /user/bin/python
'''
Author:lemon
Date:2017/9/19
Method: translate string according to a letters into a letter, for example: abc into cde
'''
import string

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
        return chr((ord(x)-97+2)%26+ 97)

if __name__ == '__main__':
    decryption_before = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr
q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    decryption_after = ''.join(list(map(translate, list(decryption_before))))
    print(decryption_after + '\n')

    decryption_before = '''map'''
    decryption_after= ''.join(list(map(encode, list(decryption_before))))
    print(decryption_after)
# print(b)










