import random as r
a, n = map(int, input().split())
r.seed(a)
for i in range(n):
    n1 = r.randint(1, 9)
    n2 = r.randint(1, 9)
    print("{0}+{1}=".format(n1, n2))