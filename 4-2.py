input=input()
lst=input.split(" ",1)
amount=float(lst[0])
extra=float(lst[1])

if (amount<=50):
    total=0.53*amount
    print("cost =","{:.2f}".format(total))
else:
    total=(50*0.53)+((amount-50)*(0.53+extra))
    print("cost =","{:.2f}".format(total))
    
