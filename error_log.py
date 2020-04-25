logdict = dict({})
logdict2 = dict({})
printlist = []
while 1:
    try:
        string  = input()
        strlist = string.split('\\')
        dot_num = strlist.pop().split()
        dot_num1 = dot_num[0].split('.')
        
        if len(dot_num1[0])>16:
            dot_num1[0] = dot_num1[0][-16:]
        key = dot_num1[0]+' '+dot_num[1]
        
        if key not in logdict.keys():
            logdict.update({key:1})
            printlist.append(key)
        else:
            logdict[key] = logdict[key] + 1
        
    except:
        break

printlist = printlist[-8:]
for i in printlist:
    print(i+' '+str(logdict[i]))