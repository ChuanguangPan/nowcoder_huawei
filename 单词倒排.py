'''
@File    :   单词倒排.py
@Time    :   2020/04/23 17:18:54
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

import re

while 1:
    try:
        inp   = input()
        instr = re.findall(r'[a-zA-Z]+',inp)
        instr.reverse()
        print(' '.join(instr))

    except:
        break