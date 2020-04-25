'''
@File    :   查找兄弟单词.py
@Time    :   2020/04/22 16:06:07
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

from collections import OrderedDict
h = 0
while h == 0:
    try:
        f = open('data.txt','r')
        instr,mydict = f.readline().split(),OrderedDict()
        f.close()
        N            = int(instr[0])
        search       = instr[N+1]
        index        = int(instr[N+2])
        N            = N+1
        strlist      = instr[1:N+1]

        for i in strlist:
            mydict[i] = []
        for i in range(N):
            a = list(strlist[i])
            c = strlist[i]
            for j in range(len(strlist)):
                b = list(strlist[j])
                e = strlist[j]
                if len(a) == len(b):
                    for k in a:
                        if k in b:
                            b.remove(k)
                if len(b)==0 and c != e:
                    mydict[c].append(e)
        for i,j in mydict.items():
            mydict[i] = sorted(j)
        x = len(mydict[search])
        print(x)
        if index <= x:
            print(mydict[search][index-1])
        h = 2
    except:
        break 
