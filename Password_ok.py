'''
@File    :   Password_ok.py
@Time    :   2020/04/21 21:26:40
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

import re

while 1:
    try:
        inp,li = input(),[]
        a,b = 0,True
        if len(inp)<9:
            print('NG')
        else:
            if re.search(r'[a-z]+.*',inp):
                a += 1
            if re.search(r'[A-Z]+.*',inp):
                a += 1
            if re.search(r'[0-9]',inp):
                a += 1
            if not inp.isalnum():
                a += 1
            for i in range(len(inp)-2):
                li.append(inp[i:i+3])
            len1 = len(li)
            len2 = len(set(li))
            # newlist = li.copy()
            # for j in newlist:
            #     li.remove(j)
            #     if j in li:
            #         b = False
            #         break
            if a > 2 and len1==len2:
                print('OK')
            else:
                print('NG')

    except:
        break