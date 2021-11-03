y=0
x=float(input())
if x==0:
    print("f(0.0)=0.000",end='')
else:
    y=1/x
    print("f(",x,")={:.3f}".format(y),end='',sep='')