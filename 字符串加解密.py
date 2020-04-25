'''
@File    :   字符串加解密.py
@Time    :   2020/04/23 19:27:47
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

def Encrypt(instr):
    mylist  = list(instr)
    newlist = []
    for i in mylist:
        if i.isdecimal():
            newlist.append(str((int(i)+1)%10))
        elif i.isalpha():
            if i.islower():
                if i == 'z':
                    i = 'A'
                else:
                    i = chr(ord(i.upper())+1)
            else:
                if i == 'Z':
                    i = 'a'
                else:
                    i = chr(ord(i.lower())+1)
            newlist.append(i)
        else:
            newlist.append(i)
    rstr = ''.join(newlist)
    return rstr         

def unEncrypt(instr):
    mylist  = list(instr)
    newlist = []
    for i in mylist:
        if i.isdecimal():
            newlist.append(str((int(i)+9)%10))
        elif i.isalpha():
            if i.islower():
                if i == 'a':
                    i = 'Z'
                else:
                    i = chr(ord(i.upper())-1)
            else:
                if i == 'A':
                    i = 'z'
                else:
                    i = chr(ord(i.lower())-1)
            newlist.append(i)
        else:
            newlist.append(i)
    rstr = ''.join(newlist)
    return rstr      

while 1:
    try:
        stra = input()
        strb = input()
        print(Encrypt(stra))
        print(unEncrypt(strb))

    except:
        break