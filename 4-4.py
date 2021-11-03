a=int(input())
if a==3:
    n=100
    m=999
    for i in range(n,m+1):
        sum = 0
        p = str(i)
        for x in p:
          sum += int(x)**3
        if sum == i:
          print(i)
elif a==4:
    n=1000
    m=9999
    for i in range(n,m+1):
        sum = 0
        p = str(i)
        for x in p:
          sum += int(x)**4
        if sum == i:
          print(i)
elif a==5:
    n=10000
    m=99999
    for i in range(n,m+1):
        sum = 0
        p = str(i)
        for x in p:
          sum += int(x)**5
        if sum == i:
          print(i)
else:
    print("error",end='')