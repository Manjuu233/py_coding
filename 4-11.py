try:
    num=int(input())
    su = 0
    for i in range(num):
        grade = eval(input())
        su += grade
    avg  = su / num

except ZeroDivisionError:
    print("除0错误，n不能等0")
except:
    print("数值错误")
else:
    print("正确")
    print("avg={:.2f}".format(su / num))
finally:
    print("程序结束")
