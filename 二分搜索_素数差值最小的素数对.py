'''
@File    :   二分搜索_素数差值最小的素数对.py
@Time    :   2020/05/07 22:00:02
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

def isprime(n : int) -> bool:
    if n%2 == 0:
        return False
    elif n%3 == 0:
        return False
    elif n%5 == 0:
        return False    
    for i in range(2,n//5+1,1):
        if n%i == 0:
            return False 
    return True            

while 1:
    try:
        N = int(input())
        for i in range(N//2,N,1):
            if isprime(i):
                if isprime(N-i):
                    print(N-i)
                    print(i)
                    break
    except:
        break

