'''
@File    :   兔子总数.py
@Time    :   2020/04/27 15:08:54
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        month = int(input())
        rabbit_age = [1,0,0]
        for i in range(month-1):
            rabbit_age[2] += rabbit_age[1]
            rabbit_age[1] = rabbit_age[0]
            rabbit_age[0] = rabbit_age[2]
        print(sum(rabbit_age))

    except:
        break