lst=[]
input=int(input())
for i in range(1,input+1):
    if input%i==0:
        lst.append(i)
    else:
        continue
print(lst)