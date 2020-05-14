'''
@File    :   链表_输出链表倒数第k个结点.py
@Time    :   2020/05/04 20:20:21
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while True:
    try:
        N, inlist, k = int(input()), input().split(), int(input())
        if k>N or k==0:
            print(0)
        else:
            print(inlist[-k])
    except:
        break