'''
@File    :   回溯法_和为24.py
@Time    :   2020/05/10 19:43:51
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''
def cal24(alllist, outstr, index_list):
    if len(outstr)==7:
        if eval(''.join(outstr))==24:
            return True
        else:
            if '*' in outstr:
                outstr.insert(0,'(')
                for i in range(len(outstr)):
                    if outstr[i] == '*':
                        outstr[i] = ')*'
                        break
                if eval(''.join(outstr))==24:
                    return True
            return False
    elif len(outstr)==0:
        for i in range(4):
            index_list.append(i)
            if cal24(alllist,[alllist[i]],index_list):
                return True
            index_list.remove(i)
        return False
    for i in range(4):
        if i in index_list:
            continue
        else:
            outstr1 = outstr + ['+'] + [alllist[i]]
            index_list.append(i)
            if cal24(alllist,outstr1,index_list):
                return True
            index_list.remove(i)
            outstr2 = outstr + ['-'] + [alllist[i]]
            index_list.append(i)
            if cal24(alllist,outstr2,index_list):
                return True
            index_list.remove(i)
            outstr3 = outstr + ['*'] + [alllist[i]]
            index_list.append(i)
            if cal24(alllist,outstr3,index_list):
                return True
            index_list.remove(i)
            outstr4 = outstr + ['/'] + [alllist[i]]
            index_list.append(i)
            if cal24(alllist,outstr4,index_list):
                return True
            index_list.remove(i)
    return False            
    
while 1:
    try:
        innum = input().split()
        index = []
        out   = []
        if cal24(innum, out, index):
            print('true')
        else:
            print('false')

    except:
        break

