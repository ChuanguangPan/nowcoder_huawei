while 1:
    try:
        string  = input()
        string  = string.replace('0x','')
        strlen = len(string)
        k = 0
        c = 1
        for j in string:
            if   j== 'A' or j == 'a':
                j = 10
            elif j == 'B' or j == 'b':
                j = 11
            elif j == 'C'  or j == 'c':
                j = 12
            elif j == 'D'  or j == 'd':
                j = 13
            elif j == 'E'  or j == 'e':
                j = 14
            elif j == 'F'  or j == 'f':
                j = 15
            else:
                j = int(j)
            k = j*(16**(strlen-c)) + k
            c = c+1
        print(k)
    except:
        break