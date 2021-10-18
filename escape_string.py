#转义字符
print('hello\nhow are you') #newline的首字母表示换行

#观察间距，发现了什么？
print('hello\thow are you') #四个空格的位置
print('helloooo\thow are you')

print('hello\rhow are you') #回车后 how are you 覆盖了前面的 hello

print('hello\bhow are you') #退格，所以少了o

print('https:\\blog.helloalone.cn') #为什么少了一个/
print('https:\\\\blog.helloalone.cn') #现在呢

print(r'hello\nhow are you') #在字符串前加上r或R不让字符串中的转义字符起作用
#print(r'hello\nhow are you\') #最后一个字符不能是一个反斜杠
print(r'hello\nhow are you\\') #但偶数个反斜杠是可以的