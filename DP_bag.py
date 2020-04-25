'''
@File    :   DP_bag.py
@Time    :   2020/04/19 20:58:01
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

items = dict()
str_budget, str_num = input().split()
budget, num = int(str_budget)//10, int(str_num)
gain  = [0]*(budget+1)
lines = 0
for i in range(num):
    v1,p1,q1 = input().split()
    lines    = lines + 1
    v, p, q  = int(v1)//10, int(p1), int(q1)
    if q == 0:
        items[lines] = [(v,p)]
    else:
        items[q].append((v,p))
for i in items.keys():
    if len(items[i])<3:
        for k in range(3-len(items[i])):
            items[i].append((0,0))
    for j in range(budget,0,-1):
        a, b = items[i][0]
        if a <= j:
            gain[j] = max(gain[j], gain[j-a]+a*b)
            x1, y1  = items[i][1]
            x2, y2  = items[i][2]
            if j-a-x1 >= 0:
                gain[j] = max(gain[j], gain[j-a-x1]+a*b+x1*y1)
            if j-a-x2 >= 0:
                gain[j] = max(gain[j], gain[j-a-x2]+a*b+x2*y2)
            if j-a-x1-x2 >= 0:
                gain[j] = max(gain[j], gain[j-a-x1-x2]+a*b+x1*y1+x2*y2)
print(gain[budget]*10)


