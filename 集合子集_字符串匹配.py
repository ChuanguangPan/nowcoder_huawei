'''
@File    :   集合子集_字符串匹配.py
@Time    :   2020/05/26 21:12:31
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        str1, str2 = set(input()), set(input())
        print(str.lower(str(str1.issubset(str2))))
    except:
        break

