n,m=map(int,input().split())
for i in range(n,m+1):
    sum = 0
    p = str(i)
    for x in p:
      sum += int(x)**3
    if sum == i:
      print(i)
