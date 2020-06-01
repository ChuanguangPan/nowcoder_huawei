'''
@File    :   给出日期输出一年的第几天.py
@Time    :   2020/05/16 17:42:24
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        year, month, day = int(input()), int(input()), int(input())
        num_days         = [31,28,31,30,31,30,31,31,30,31,30,31]
        num_days_run     = [31,29,31,30,31,30,31,31,30,31,30,31]
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            out = sum(num_days_run[0:month-1]) + day
        else:
            out = sum(num_days[0:month-1]) + day
        print(out)
    except:
        break

