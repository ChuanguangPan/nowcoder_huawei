'''
@File    :   统计各类型字符个数.py
@Time    :   2020/04/27 15:28:04
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''
import re

while 1:
    try:
        instr = input()
        l = len(instr)
        eng = len(re.findall(r'[a-zA-Z]',instr))
        dec = len(re.findall(r'[0-9]',instr))
        nspace = len(re.findall(r' ',instr))
        print(eng)
        print(nspace)
        print(dec)   
        print(l-eng-dec-nspace)

    except:
        break