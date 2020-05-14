'''
@File    :   英语数字.py
@Time    :   2020/04/28 17:06:13
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

Digits = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
Tendigits = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def num(x):
    ret = ''
    if x > 0:
        if x//100 > 0:
            ret += '%s hundred '%(Digits[int(x//100-1)])
            if x%100 > 0:
                ret += 'and '
        if (x%100)//10 > 1:
            ret += '%s '%(Tendigits[int((x%100)//10-2)])
            if x%10 > 0:
                ret += '%s '%(Digits[int(x%10-1)])
        else:
            ret += '%s '%(Digits[int(x%20-1)])
    return ret

while 1:
    try:
        indec = int(input())
        out = ''
        x = int(indec//1e6)
        y = indec%1e6
        if x > 0:
            out += '%smillion '%(num(x))
        x = int(y//1e3)
        y = y%1e3
        if x > 0:
            out += '%sthousand '%(num(x))   
        x = int(y)
        if x > 0:
            out += '%s'%(num(x)) 
        mylist = list(out)
        if mylist[-1] == ' ':
            mylist.pop()
        print(''.join(mylist))

    except:
        break
