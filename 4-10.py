n=int(input())
num=int(n/2)
nn=5
for i in range(0,num):
        print(' '*(nn-i-1),'*'*(i*2+1),' '*(nn-i-1))
if num==5:
        print('*'*11)
        num=num-1
for n in range(num,-1,-1):
        print(' '*(nn-n-1),'*'*(n*2+1),' '*(nn-n-1))
