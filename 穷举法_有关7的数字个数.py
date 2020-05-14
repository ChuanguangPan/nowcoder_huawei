'''
@File    :   穷举法_有关7的数字个数.py
@Time    :   2020/05/06 22:02:11
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        num   = int(input())
        count = 0
        for i in range(1,num+1,1):
            if i%7 == 0:
                count += 1
            elif '7' in list(str(i)):
                count += 1
            else:
                continue
        print(count)
    except:
        break

