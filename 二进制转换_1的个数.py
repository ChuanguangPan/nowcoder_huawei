'''
@File    :   二进制转换_1的个数.py
@Time    :   2020/05/08 16:50:10
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        print(str(bin(int(input()))).count('1'))
    except:
        break

