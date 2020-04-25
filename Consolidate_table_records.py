mydict     = dict()
record_len = int(input())

for i in range(record_len):
    a, b  = input().split()
    index = int(a)
    value = int(b)
    if index in mydict.keys():
        mydict[index] = mydict[index]+value
    else:
        mydict[index] = value
    # print(mydict)
mylist = sorted(mydict)
for i in mylist:
    print(i,mydict[i])
