'''
@File    :   排序和去重_整型数组合并.py
@Time    :   2020/05/26 20:56:11
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        n1,intarr1,n2,intarr2 = input(), list(map(int,input().split())),input(),list(map(int,input().split()))
        print(''.join(list(map(str,sorted(set(intarr1+intarr2))))))
    except:
        break

