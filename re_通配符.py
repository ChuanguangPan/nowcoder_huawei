'''
@File    :   re_通配符.py
@Time    :   2020/05/12 21:18:55
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

import re 

while 1:
    try:
        instr, str2 = input(), input()
        str1 = instr.replace("?","\w{1}").replace(".","\.").replace("*","\w*")
        pattern = re.compile(str1)
        if re.match(pattern,str2)!=None:
            print('true')
        else:
            print('false')
    except:
        break

