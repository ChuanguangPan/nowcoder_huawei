'''
@File    :   穷举法_DNA序列.py
@Time    :   2020/05/08 16:58:08
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        instr, strlen = input(), int(input())
        GCratio, flag, out = 0, 0, instr[0:strlen]
        for i in range(len(instr)-strlen):
            Substring = instr[i:i+strlen]
            if 'A' not in Substring and 'T' not in Substring:
                flag = 1
                print(Substring)
                break
            else:
                temp = Substring.count('G')+Substring.count('C')
                if temp>GCratio:
                    GCratio = temp
                    out = Substring
        if flag == 0:
            print(out)
    except:
        break

