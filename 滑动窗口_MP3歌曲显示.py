'''
@File    :   滑动窗口_MP3歌曲显示.py
@Time    :   2020/05/08 17:18:17
@Author  :   Pan 
@Version :   1.0
@Contact :   pwd064@mail.ustc.edu.cn
@License :   (C)Copyright 2020-2025, USTC
@Desc    :   None
'''

while 1:
    try:
        num, operation      = int(input()), input()
        loc_all, loc_screen = 1, 1
        if num<=4:
            for ope in operation:
                if ope == 'U':
                    loc_all = num-(num-loc_all+1)%num
                else:
                    loc_all = (loc_all+1)%num
            for i in range(1,num+1,1):
                print(i,end='')
                if i != num:
                    print('',end=' ')
                else:
                    print('')
            print(loc_all)
        else:
            for ope in operation:
                if ope == 'U':
                    if loc_all == 1:
                        loc_all    = num
                        loc_screen = 4
                    elif loc_screen == 1:
                        loc_all    -= 1
                    else:
                        loc_all    -= 1
                        loc_screen -= 1
                else:
                    if loc_all == num:
                        loc_all    = 1
                        loc_screen = 1
                    elif loc_screen == 4:
                        loc_all    += 1
                    else:
                        loc_all    += 1
                        loc_screen += 1
            for i in range(1,5,1):
                    print(loc_all+i-loc_screen,end='')
                    if i != 4:
                        print('',end=' ')
                    else:
                        print('')
            print(loc_all)

    except:
        break

