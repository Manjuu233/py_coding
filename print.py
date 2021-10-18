print(233666) #数字
print('wdnmd') #字符串
print(2+2) #表达式

#输出到文件
#指定的盘符要存在
fp=open('D:/out.txt','a+') #a+的含义：如果文件不存在则创建，存在则在内容后继续追加
print('wdnmd',file=fp)
fp.close

#不换行输出
print('w','d','n','m','d')