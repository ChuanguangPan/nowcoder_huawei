'''
@File    :   砝码称重2.py
@Time    :   2020/04/27 16:15:20
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        N, weight, num = int(input()), input().split(), input().split()
        mylist = []
        for i in range(len(weight)):
            for j in range(int(num[i])):
                mylist.append(int(weight[i]))
        totalw = [0]
        t = 0
        newlist = []
        for k in mylist:
            newset = set(totalw)
            for h in newset:
                totalw.append(h+k)
        print(len(set(totalw)))

    except:
        break