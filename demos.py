#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
#author linqiang
date 2018/04/12
function basic exercises(代码和编码规范 前半部分为idle下编程练习，后半部分为pycharm变成练习)




#1 Hello World实例
print("Hello World!")


#2 通过用户输入两个数字，并计算两个数字之和
#方法1
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')
#求和
sum = float(num1) + float(num2)
#显示计算结果
print("数字1和数字2相加的结果是：{2}".format(num1,num2,sum))
#方法2
print("两个数字相加的结果是%.1f"%(float(input("请输入第一个数字")) + float(input("请输入第二个数字"))))

#3 计算一个数字的算术平方根
#方法1
num = float(input('请输入一个数字'))
num_sqrt = num ** 0.5
print('%0.3f的算数平方根是%0.3f'%(num,num_sqrt))
#方法2
import cmath
num = int(input('请输入一个数字：'))
num_sqrt = cmath.sqrt(num)
print("{0}的算数平方根是{1:.3f}+{2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))

#4一元二次方程ax*2 + bx +c =0用户输入abc
##用求根公式法解一元二次方程的一般步骤为：
##①把方程化成一般形式  ，确定a，b，c的值（注意符号）；
##②求出判别式  的值，判断根的情况；
##③在  （注：此处△读“德尔塔”）的前提下，把a、b、c的值代入公式 进行计算，求出方程的根。
import cmath
a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input('请输入c: '))

d = (b**2) - 4 * a * c
#两个根的计算公式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("结果为{0}{1}".format(sol1,sol2))

#5 计算三角形面积，用户输入三边长度
##已知三角形的三边分别是a、b、c， 
##先算出周长的一半s=1/2(a+b+c) 
##则该三角形面积S=根号[s(s-a)(s-b)(s-c)] 
##这个公式叫海伦——秦九昭公式 

a = float(input('请输入第一个边长'))
b = float(input('请输入第二个边长'))
c = float(input('请输入第三个边长'))

s = (a+b+c)/2
area = (s*(s-b)*(s-a)*(s-c)) ** 0.5
print("三角形的面积为%.2f"%area)

#6 随机数生成
import random
print ("{0}".format(random.random()))
print (str(random.randint(0,19)))

#7 摄氏度转华氏度
celsius = float(input("请输入摄氏温度："))
fahrenheit = celsius * 1.8 + 32
print ("%.2f摄氏度转为华氏摄氏度为%.3f"%(celsius,fahrenheit))

#8 用户输入两个变量，并相互交换
x = input("请输入第一个变量x")
y = input('请输入第二个变量y')
z = x
x = y
y = z
print("x是{0}，y是{1}".format(x,y))

#第二种方法
x = input("请输入x")
y = input('请输入y')
x, y =y, x
print("x是{0}，y是{1}".format(x,y))

#9 if语句判断数字正负
num = float(input('输入一个数字：'))
if num > 0:
    print("正数")
elif num ==0:
    print('零')
else:
    print("负数")
#方法2 内嵌if

x = float(input("请输入数字"))
if x >= 0:
    if x == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")

#10 判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
        
    try:
        import unicodedata
        unicodedat.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False

#11 判断奇数偶数
num = int(input("请输入一个数字"))
if num%2 == 0:
    print("{0}偶数".format(num))
else:
    print("奇数")

#12 判断用户输入的年份是否是闰年

year = int(input("请输入年份："))
if (year%4) == 0:
    if (year%100) == 0:
        if (year%400) ==0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("是闰年")
else:
    print("不是闰年")

#13获取最大值函数
#方法1
print(max(1,2))
print(max("a","b"))
#方法2
print(max((1,2)))

#14 质数判断
num = int(input("请输入一个数字："))
if num > 1:
    for i in range(2,num):
         if num % i == 0:
            print("{0}不是质数".format(num))
            break
    else:
          print("是质数")
else:
    print("是质数")
      

#15 输出指定范围内的素数
lower = int(input("输入区间最小值："))
upper = int(input("输入区间最大值："))
for num in (lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

#16阶乘实例
num = int(input("请输入数字："))
factorial = 1
if num <0:
    print('负数没有阶乘')
elif num == 0:
    print('0的阶乘为1')
else:
    for i in range(2,num + 1):
        factorial = factorial * i
print("{0}的阶乘结果是{1}".format(num,factorial))

#17 乘法表
for j in range(1,10):
    for i in range(1,j+1):
        print("{0}*{1}={2}\t".format(j,i,j*i),end="")
    print("\n")

#18菲波那切数列
nterms = int(input("请输入你需要几项"))
n1 = 0
n2 = 1
count = 2
if nterms == 1:
    print("菲波那切数列：")
    print(n1)
else:
    print("菲波那切数列：")
    print(n1,n2,end=" ")
    while nterms > count:
        nth = n1 + n2
        print(nth,end=" " )
        n1 = n2
        n2 = nth
        count+=1

#19阿姆斯特朗数
num = int(input("请输入一个数字："))
sum = 0
n = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum +=digit ** n
    temp = temp // 10
if num ==sum:
    print("是")
else:
    print("不是")

#20 十进制转二进制 八进制 十六进制

dec = int(input("请输入数字："))
print("十进制",dec)
print("二进制",bin(dec))
print("八进制",oct(dec))
print("十六进制",hex(dec))
print("十六进制 %X 2"%(dec))

#21ASCII码与字符相互转换
c = input("请输入一个字符：")
a = int(input("请输入一个ASCII码"))
print(c+"的ASCII码是",ord(c))
print(a,"的字符",chr(a))

#22求最大公约数
def hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if(x%i==0)and(y%i==0):
            hcf = i
    return hcf

num1 = int(input("请输入x"))
num2 = int(input("请输入y"))
print("最大公约数是",hcf(num1,num2))

#23最小公倍数
def lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if(greater%x==0)and(greater%y==0):
            lcm = greater
            break
        greater += 1
        print('2')
    return lcm
num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))
print(lcm(num1,num2))

#24简单计算器实现
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("选择运算 1 相加，2相减，3相乘，4相除")
choice = int(input("请输入选择的方法"))
x = int(input("请输入第一个数"))
y = int(input("请输入第二个数"))


if choice == 1:
    print(add(x,y))
elif choice == 2:
    print(subtract(x,y))
elif choice == 3:
    print(multiply(x,y))
elif choice ==4:
    print(divide(x,y))
else:
    print("选择有误")

#25生成日历
import calendar
yy = int(input("请输入年份"))
mm = int(input("请输入月份"))

print(calendar.month(yy,mm,w=3 ,l=2))

#26 使用递归的方式来生成菲波那切数列
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
nterms = int(input("请输入项数"))
if nterms <= 0:
    print("请输入正数")
else:
    print("fibo")
    for i in range(nterms):
        print(recur_fibo(i))

#27 文件IO
with open("test.txt","wt")as out_file:
    out_file.write("nihao hi")
with open("test.txt","rt")as in_file:
    text = in_file.read()
print (text)

#28 29字符串判断
print ("ceshi")
str = "wo shiYIGE大西瓜，2号"
str2 = "   "
str3 = "170022"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str2.isspace())
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())

#30计算每个月天数
import calendar
monthRange = calendar.monthrange(2016,9)
print(monthRange)

#31通过datetime模块获取昨天日期
import datetime


def get_yesterday():
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    return yesterday


print(get_yesterday())
print ("ceshi")
str = "wo shiYIGE大西瓜，2号"
str2 = "   "
str3 = "170022"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str2.isspace())
print(str.upper())
print(str.lower())
print(str.capitalize())
"""
"""
pycharm下练习


#1 列表
list1 = ["Google", "baidu", "sohu"]
list2 = [1, 2, 3, 4, 5, 6, 7]
print(list1[2])
list2[1] = 29
del list2[-2]
print(list2[1], list2)
list3 = [[2, 8], [0, 4], 3]
print(list3[0][1])
list3.append(3)
print(list3.count(3),list3,list3.index(3))

#2元组
tup1 = (50,)
tup2 = ('Google', 'Run', 'Xiaomi')
print(tup1[0], tup2[1], tup2)
tup3 = tup2 + tup1;
print(tup3,len(tup3),max(tup2))

#3字典
x = 1
dict22 = {"Name": "xiaoming", "Age": 3, "Class": 5, "sex": "boy"}
dict22['Age'] = 6
del dict22["sex"]
print(dict22['Name'], dict22['Age'], type(dict22), dict22)

# 4循环
letter = "How are you"
for i in letter:
    if i == 'o':
        pass
        print("find")
    print(i)


i = 1
while True:
    print("2")
    i += 1
    if i == 20:
        break
print("End")

letter2 = [1, 2, 3, 4, 5, 6]
it = iter(letter2)
print(next(it))
print(next(it))
import sys

#5函数
sum = lambda x1, x2: x1 + x2
print(sum(10, 20))
 

def printinfo(arg1, *arg2):
    print(arg2)


printinfo(1, 2, 3, 4, 5, 6, 7, 8)

#6文件
fo = open("xiaomi.txt","rb")
print(fo.name)
# str22 = "I am fine,thank you."
# fo.write( str22 )

print(fo.read(10))

fo.close()
#7异常
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

#类
class MyClass:
    i = 123
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def f(self):
        return "hello"


x = MyClass(11,3)
y =MyClass(2,3)
print("属性i是",x.i)
print("类的方法f输出是",x.f())
print(y.i,x.i)
"""


class People:
    name = "xiaomi"
    age = 2
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(self.name,self.age,self.__weight)


y = People("xiaoer",5,70)
y.speak()
print(y.name)


class Stu(People):
    grade = ""

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print(self.name, self.age, self.grade)


s = Stu("xiaosan", 2, 30, 7)
s.speak()

# TODO 继续1