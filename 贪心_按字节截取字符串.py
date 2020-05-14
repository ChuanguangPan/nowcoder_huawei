'''
@File    :   按字节截取字符串.py
@Time    :   2020/05/04 09:57:08
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

def select_n_char(instr: str,N: int):
    indexes, count = 0, 0
    for i in instr:
        if count <= N:
            if ord(i) > 255:
                count += 2
            else:
                count += 1
            indexes += 1
        else:
            break
    indexes -= 1
    return instr[0:indexes]
              
while 1:
    try:
        instr, N1 = input().split()
        N = int(N1)
        print(select_n_char(instr,N))

    except:
        break