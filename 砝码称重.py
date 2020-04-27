'''
@File    :   砝码称重.py
@Time    :   2020/04/27 15:49:15
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
            mylist.append((int(weight[i]), int(num[i])))
        totalw = [0]
        t = 0
        addlist = []
        for i,j in mylist:
            for k in totalw:
                for h in range(j+1):
                    t = k + h*i
                    if t not in totalw:
                        addlist.append(t)
            for k in addlist:
                totalw.append(k)
            addlist.clear()
        print(len(totalw))

    except:
        break