'''
@File    :   矩阵乘法实现.py
@Time    :   2020/05/11 20:08:58
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        m,n,p = int(input()), int(input()), int(input())
        mat1, mat2, prod = [], [], []
        for i in range(m):
            prod.append([])
        for i in range(m):
            mat1.append(list(map(int,input().split())))
        for i in range(n):
            mat2.append(list(map(int,input().split())))
        for i in range(m):
            for j in range(p):
                temp = 0
                m1, m2 = mat1[i], list(a[j] for a in mat2)
                for k in range(len(m1)):
                    temp += m1[k]*m2[k]
                prod[i].append(temp)
        for i in prod:
            out = ' '.join(list(map(str,i)))
            print(out)
    except:
        break

