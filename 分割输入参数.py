'''
@File    :   分割输入参数.py
@Time    :   2020/05/16 17:54:37
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''
while 1:
    try:
        incommand, flag,prev = input(), 0, 0
        mylist = []
        for i in range(len(incommand)):
            if incommand[i] == '"':
                if flag == 1:
                    mylist.append(incommand[prev:i])
                    prev = i+1
                else:
                    prev += 1
                flag = 1-flag
            else:
                if flag == 0 and incommand[i] == ' ':
                    mylist.append(incommand[prev:i])
                    prev = i+1
        mylist.append(incommand[prev:])
        while '' in mylist:
            mylist.remove('')
        print(len(mylist))
        for i in mylist:
            print(i)
    except:
        break

