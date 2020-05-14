'''
@File    :   顺序计数_找出字符串中第一个只出现一次的字符.py
@Time    :   2020/05/07 21:49:50
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        instr = input()
        i = 0
        while i<len(instr):
            char = instr[i]
            if instr.count(char) == 1:
                print(char)
                break
            else:
                i += 1
        if i == len(str):
            print(-1)

    except:
        break

