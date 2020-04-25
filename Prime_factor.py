def getResult(ulDataInput):
    half = ulDataInput//2+1
    i = 2
    if half <= 2:
        return (str(ulDataInput)+' ')
    else:
        while i < half:
            if ulDataInput%i == 0:
                return (str(i) +' '+getResult(ulDataInput//i))
            i = i+1
        return (str(ulDataInput)+' ')

try:
    ulInput = int(input())
    print(getResult(ulInput))
except:
    pass