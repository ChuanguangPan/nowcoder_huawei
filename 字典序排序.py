'''
@File    :   字典序排序.py
@Time    :   2020/05/21 20:49:43
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        n, num = int(input()), input().split()
        def printseq(atstation:list,outstation:list,train):
            global n,num
            
            if train==n:
                atstation.reverse()
                print(outstation+atstation)
                return True
            for i in range(3):
                if i==0:
                    atstation.append(num[train])
                    print(atstation,outstation)
                    printseq(atstation,outstation,train+1)
                    atstation.pop()
                    print(111)
                elif i==1:
                    outstation.append(num[train])
                    print(atstation,outstation)
                    printseq(atstation,outstation,train+1)
                elif i==2 and len(atstation)>0:
                    outstation.append(atstation.pop())
                    printseq(atstation,outstation,train)
            return False
        printseq([],[],0)
    except:
        break

