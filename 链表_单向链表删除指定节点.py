'''
@File    :   链表_单向链表删除指定节点.py
@Time    :   2020/05/04 17:01:15
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        N = int(input())
        mylist = []
        mylist.append(input())
        for i in range(N-1):
            indata = input().split()
            if indata[0] in mylist:
                continue
            else:
                mylist.insert(int(indata[1]),indata[0])
        j = input()
        mylist.remove(j)
        print(' '.join(mylist))
    except:
        break