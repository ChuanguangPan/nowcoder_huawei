'''
@File    :   穷举_完全数个数.py
@Time    :   2020/05/07 21:19:26
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

def count(n:int) -> int:
    mylist = []
    for i in range(1,n+1,1):
        b = 0
        for j in range(1,i//2+1,1):
            if i%j == 0:
                b += j
        if b == i:
            mylist.append(i)
    return len(mylist)

while 1:
    try:
        N = int(input())
        print(count(N))
        
    except:
       break

