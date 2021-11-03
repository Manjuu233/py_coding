def fun(m, n):
    p = m*n
    while m%n!=0:
        m, n = n, m%n
    return (n, p//n)
a,b = map(int,input().split(','))
print('GCD:%d, LCM:%d'%fun(a,b))