'''
@File    :   length_of_string.py
@Time    :   2020/04/15 15:20:38
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

sentence = input()
strlen = len(sentence)

for i in range(strlen):
    if sentence[strlen-1-i] == ' ':
        print(i)
        break
    elif i == strlen-1:
        print(strlen)
    else:
        pass
