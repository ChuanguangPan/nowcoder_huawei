'''
@File    :   第5次反弹高度.py
@Time    :   2020/04/26 22:56:10
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        height = float(input())
        dist = height
        distance = height
        lasth = 0.0
        for i in range(4):
            dist /= 2.0
            distance += dist*2.0
        dist /= 2.0
        print('%.6f'%distance)
        print('%.6f'%dist)

    except:
        break