'''
@File    :   字典加密.py
@Time    :   2020/04/27 14:35:07
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

from collections import OrderedDict
while 1:
    try:
        key, data = list(input()),list(input())
        mydict = OrderedDict()
        for i in key:
            mydict[i] = 0
        key = list(mydict.keys())
        mydict.clear()
        for j in range(97,123,1):
            if chr(j) not in key:
                key.append(chr(j))
        for k in range(26):
            mydict[chr(97+k)] = key[k]
        out = []
        for h in data:
            if h.islower():
                out.append(mydict[h])
            else:
                s = str(mydict[h.lower()])
                out.append(s.upper())
        print(''.join(out))

    except:
        break
    

