'''
@File    :   int_bin_1_num.py
@Time    :   2020/04/18 17:03:38
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

int2bin  = bin(int(input()))
bin_1num = str(int2bin).count('1')
print(bin_1num)
