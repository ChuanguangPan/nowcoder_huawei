'''
@File    :   单向链表修正.py
@Time    :   2020/05/04 17:12:35
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        inputlist = input().split()
        N, head, mylist = inputlist[0], inputlist[1], inputlist[2:]
        newlist = []
        newlist.append(head)
        i = 0
        while i<=len(mylist)-3:
            m,n = mylist[i], mylist[i+1]
            newlist.insert(newlist.index(n)+1,m)
            i += 2
        if mylist[-1] in newlist:
            newlist.remove(mylist[-1])
        else:
            pass
        print(' '.join(newlist))

    except:
       break

