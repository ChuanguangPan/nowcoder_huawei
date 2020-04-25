'''
@File    :   字符串排序.py
@Time    :   2020/04/22 13:29:05
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

from collections import OrderedDict

while 1:
    try:
        instr   = list(input())
        newlist = instr.copy()
        indict  = OrderedDict()
        lenstr  = len(instr)
        count   = 0
        for i in instr:
            indict[count] = i
            count += 1
            if not i.isalpha():
                newlist.remove(i)
        newlen = len(newlist)
        for i in range(newlen):
            for j in range(0,newlen-1-i,1):
                if newlist[j].lower() > newlist[j+1].lower():
                    newlist[j], newlist[j+1] = newlist[j+1], newlist[j]
        for i,j in indict.items():
            if not j.isalpha():
                newlist.insert(i,j)
        print(''.join(newlist))
    except:
        break
