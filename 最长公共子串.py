'''
@File    :   最长公共子串.py
@Time    :   2020/05/08 17:57:54
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        str3, str4 = input(), input()
        maxlen, len3, len4 = 0, len(str3), len(str4)
        if len3<=len4:
            str1, str2 = str3, str4
            len1, len2 = len3, len4
        else:
            str1, str2 = str4, str3
            len1, len2 = len4, len3
        out = ''
        for i in range(len1):
            for j in range(i,len1,1):
                substring = str1[i:j]
                len5 = len(substring)
                if len5<=maxlen:
                    continue
                else:
                    if substring in str2:
                        maxlen = len5
                        out    = substring
                    else:
                        break
        print(out)
    except:
        break
