'''
@File    :   split_8char.py
@Time    :   2020/04/15 17:06:20
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

for i in range(2):
    string = input()
    if string != '':
        strlen = len(string)
        if strlen%8 != 0:
            string = string + '0'*int(8-strlen%8)
            strlen = strlen + int(8-strlen%8)
        for j in range(strlen//8):
            print(string[j*8:(j+1)*8])
       