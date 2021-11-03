while True:
    n=int(input(''))
    if n==1:
        print('1 is not prime')
    elif n==2:
        print('2 is prime')
    for i in range(2,n):
        if n%i==0:
            print("{} is not prime".format(n))
            break
        if n==i+1:
            print("{} is prime".format(n))
    break