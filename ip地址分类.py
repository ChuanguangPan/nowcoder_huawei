'''
@File    :   ip地址分类.py
@Time    :   2020/04/21 19:29:40
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

import re

A,B,C,D,E,error,private = [0]*7

while 1:
    try:
        global bmask
        ip, mask     = input().split('~')
        if_iplegal   = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
        ignore       = re.compile(r'^[0]{1}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
        if_masklegal = re.compile(r'^[1]+[0]+$')
        temp         = mask.split('.')
        bmask        = ''
        aa           = 1
        if len(temp)==4:
            for i in temp:
                if int(i) > 255:
                    aa = 0
                    continue
                b = '{:08b}'.format(int(i))
                bmask    = bmask+str(b)
            if aa == 1 and re.match(if_iplegal,ip)!=None and re.match(if_masklegal,bmask)!=None: 
                if re.match(ignore,ip)!=None:
                    aa = 0
                    continue                      
                flag = ip.split('.')
                if aa == 1 and int(flag[0])<256 and int(flag[1])<256 and int(flag[2])<256 and int(flag[3])<256:
                    if int(flag[0])<127:
                        A += 1
                        if int(flag[0])==10:
                            private += 1
                    elif int(flag[0])<192 and int(flag[0])>127:
                        B += 1
                        if int(flag[0])==172 and int(flag[1])<32 and int(flag[1])>15:
                            private += 1
                    elif int(flag[0])<224 and int(flag[0])>191:
                        C += 1
                        if int(flag[0])==192 and int(flag[1])==168:
                            private += 1
                    elif int(flag[0])<240 and int(flag[0])>223:
                        D += 1
                    elif int(flag[0])<256 and int(flag[0])>239:
                        E += 1  
                    else:
                        pass
                else:
                    error += 1
            else:
                error += 1   
        else:
            error += 1   

    except:
        print(A,B,C,D,E,error,private)
        break