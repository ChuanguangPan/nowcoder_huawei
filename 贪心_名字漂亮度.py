'''
@File    :   贪心_名字漂亮度.py
@Time    :   2020/05/04 09:31:03
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''
def beauty(name):
    nameset = set(name)
    countlist = []
    for i in nameset:
        countlist.append(name.count(i))
    newlist = sorted(countlist)
    newlist.reverse()
    value, beauty_degree = 26, 0
    for j in range(len(newlist)):
        beauty_degree += newlist[j]*value
        value -= 1
    return beauty_degree   

while 1:
    try:
        N = int(input())
        for i in range(N):
            print(beauty(input()))
    except:
        break