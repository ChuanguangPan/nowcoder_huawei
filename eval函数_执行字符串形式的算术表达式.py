'''
@File    :   eval函数_执行字符串形式的算术表达式.py
@Time    :   2020/05/04 20:10:19
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        a = input()
        b = a.replace('[','(').replace(']',')')
        c = b.replace('{','(').replace('}',')')
        print(eval(c))
    except:
        break