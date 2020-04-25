'''
@File    :   坐标移动.py
@Time    :   2020/04/20 16:47:00
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''
import re

while 1:
    try:
        Loc      = [0,0]
        Instring = input().split(';')
        pattern  = re.compile(r'^([A|W|S|D]\d+)$')
        
        for i in Instring:
            if re.match(pattern,i):
                if   i[0]=='A':
                    Loc[0] -= int(i[1:])
                elif i[0]=='D':
                    Loc[0] += int(i[1:])  
                elif i[0]=='S':
                    Loc[1] -= int(i[1:]) 
                elif i[0]=='W':
                    Loc[1] += int(i[1:]) 
                else:
                    pass
        print(str(Loc[0])+','+str(Loc[1]))        
        
    except:
        break