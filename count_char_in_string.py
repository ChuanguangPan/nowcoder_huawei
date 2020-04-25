'''
@File    :   count_char_in_string.py
@Time    :   2020/04/15 15:46:11
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        mylist  = []
        strlen  = int(input())
        for i in range(strlen): 
            mylist.append(int(input()))
        myset   = set(mylist)
        mylist2 = sorted(myset)
        for li in mylist2: 
            print(li)
    except:
        break
