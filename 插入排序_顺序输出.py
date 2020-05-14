'''
@File    :   插入排序_顺序输出.py
@Time    :   2020/05/11 19:50:45
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        N, flag = int(input()), input()
        mylist  = []
        for i in range(N):
            inlist = input().split()
            j = 0
            for k in range(len(mylist)):
                if flag == '0':
                    if int(inlist[1]) > int(mylist[k][1]):
                        j = 1
                        mylist.insert(k,inlist)
                        break
                else:
                    if int(inlist[1]) < int(mylist[k][1]):
                        j = 1
                        mylist.insert(k,inlist)
                        break
            if j == 0:
                mylist.append(inlist)
        for i in mylist:
            print(' '.join(i))
    except:
        break

