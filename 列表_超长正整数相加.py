'''
@File    :   列表_超长正整数相加.py
@Time    :   2020/05/23 22:04:59
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

# while 1:
#     try:
#         add1, add2, result = list(input()),list(input()), []
#         add1, add2 = list(map(int,add1)), list(map(int,add2))
#         C = 0
#         if len(add1)<len(add2):
#             add1, add2 = add2, add1
#         for i in range(len(add1)):
#             if i<len(add2):
#                 sum1 = add1[-1-i] + add2[-1-i] + C
#             else:
#                 sum1 = add1[-1-i] + C
#             result.append(str(sum1%10))
#             C = 1 if sum1>=10 else 0
#         if C == 1:
#             result.append('1')
#         result.reverse()
#         print(''.join(result))
#     except:
#         break
while True:
    try:
        a = input()
        b = input()
        print(str(int(a) + int(b)))
    except:
        break
