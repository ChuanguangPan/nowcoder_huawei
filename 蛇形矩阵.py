'''
@File    :   蛇形矩阵.py
@Time    :   2020/04/26 22:00:05
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

def snake_matrix(N):
    if N <= 0:
        return N
    else:
        num = list(range(1,N*(N+1)//2+1,1))
        mylist = []
        for i in range(1,N+1,1):
            t = min(num)
            mylist.append(str(t))
            for j in range(i+1,N+1,1):
                t += j
                mylist.append(str(t))
            out = ' '.join(mylist)
            print(out)
            for k in mylist:
                num.remove(int(k))
            mylist.clear()
    return N    
while 1:
    try:
        N = int(input())
        snake_matrix(N)
    except:
        break