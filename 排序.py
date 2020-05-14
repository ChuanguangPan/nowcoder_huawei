'''
@File    :   排序.py
@Time    :   2020/05/07 21:40:31
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        b = sorted(b)
        print(' '.join(list(map(str,b[0:a[1]]))))
    except:
        break

