'''
@File    :   简单密码.py
@Time    :   2020/04/22 08:55:03
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        inp = list(input())
        j   = []
        for i in inp:
            if i.isupper():
                if i == 'Z':
                    j.append('a')
                else:
                    j.append(chr(ord(i.lower())+1))
            elif i.islower():
                if i<'d':
                    j.append('2')
                elif i<'g':
                    j.append('3')
                elif i<'j':
                    j.append('4')
                elif i<'m':
                    j.append('5')
                elif i<'p':
                    j.append('6')
                elif i<'t':
                    j.append('7')
                elif i<'w':
                    j.append('8')
                else:
                    j.append('9')
            else:
                j.append(i)
        print(''.join(j))       

    except:
        break