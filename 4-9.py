c=r=int(input())
def getPix(r, c):
    num = r
    if num > c:
        num = c
    return '%4d'%(num+1)
if __name__ == '__main__':
    for i in range(r):
        for j in range(c):
            print( getPix( i, j ), end = '')
        print('')