'''
@File    :   dict_sort.py
@Time    :   2020/04/18 16:56:36
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

num_sen, mylist = int(input()), []
for i in range(num_sen):
    mylist.append(input())
newlist = sorted(mylist)
for i in newlist:
    print(i)
    