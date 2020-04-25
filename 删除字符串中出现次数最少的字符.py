'''
@File    :   删除字符串中出现次数最少的字符.py
@Time    :   2020/04/22 10:48:10
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        instr     = input()
        countdict = dict()
        for i in instr:
            countdict[i] = instr.count(i)
        sortedlist = sorted(countdict.items(),key = lambda x: x[1])
        choice = sortedlist[0][1]
        for i in sortedlist:
            if i[1]==choice:
                instr = instr.replace(i[0],'')
            else:
                break
        print(''.join(instr))                               

    except:
        break
