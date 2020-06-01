'''
@File    :   数学定理_验证尼科彻斯定理.py
@Time    :   2020/05/19 20:11:27
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        inum   = int(input())
        odd_head,odd_tail = inum*(inum-1)+1, (inum-1)**2+3*(inum-1)+1
        odd    = list(range(odd_head,odd_tail+2,2))
        strodd = list(map(str,odd))
        print('+'.join(strodd))
    except:
        break

