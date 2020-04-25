'''
@File    :   素数伴侣.py
@Time    :   2020/04/23 16:26:56
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        N = int(input())
        Nstr = input().split()
        Nint = [int(i[0:N]) for i in Nstr]
        mydict, mylist = dict(),[]
        for i in range(N):
            for j in range(i+1,N,1):
                if Nint[i] != Nint[j]:
                    mydict[(Nint[i],Nint[j])] = Nint[i]+Nint[j]
        for i,j in mydict.items():
            if j%2 == 0:
                mylist.append(i)
        for i in mylist:
            mydict.pop(i)
        value  = list(mydict.values())
        remli  = []
        maxval = max(value)
        for i in range(2,int(maxval/2+1)):
            for j in value:
                if (i != j and j%i == 0):  
                    remli.append(j)
            for j in remli:
                value.remove(j)
            remli.clear()
        print(len(value),value)

    except:
        break