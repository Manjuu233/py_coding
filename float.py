a=1.1
b=2.2
c=2.1

print(a+b) #等于3.3000000000000003 为什么会这样？

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

print(a+c) #并不是都会出现以上情况