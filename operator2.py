a,b=233,666
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

c,d=233,233
print(a==b) #比value
print(a is b) #比ID
print(a is not b) #a的id和b的id是不相等的吗？

lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
print(lst1==lst2) #比value
print(lst1 is lst2) #比ID
print(lst1 is not lst2) #lst1的id和lst2的id是不相等的吗？
print(id(lst1))
print(id(lst2)) #随便看看
