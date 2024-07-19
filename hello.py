# from PIL import Image, ImageDraw, ImageFont

from datetime import datetime, timedelta
import hashlib
import queue
import re
import doctest
import datetime
from urllib.request import urlopen
import os
from urllib import request
import pprint
import pickle
import time
import keyword
import sys
import getopt
import fileinput
import random
from functools import reduce
from def_function.Matrix import Matrix_transfer
from def_function.Son_matrix import son_matrix_transposition
import def_function.Matrix
import calendar
import datetime
import threading
import operator
import requests
import yfinance as yf


headline_0 = "Hello World!"
headline_1 = '''2024/5/17\ the first paragraph'''
# 这里的 r 指 raw，即 raw string，会自动将反斜杠转义
headline_2 = r'''2024/5/17\nthe second paragraph'''
number_learning_example_0 = 123
number_add_to_list = 100
str_learning_separator = 'a,b,c def'
str_learning_example_number = "123456789"
bool_data_0 = True
bool_data_1 = False
list_data_0 = [1, 2, 3, 4, 5]
list_data_1 = list_data_0[:]
list_example_transfer = list(str_learning_example_number)
tuple_example_0 = ()
tuple_learning_0 = ()
tuple_learning_1 = (1,)
tuple_learning_2 = (1)
tuple_learning_example_list = (number_learning_example_0, list_data_0)
tuple_example_word = ('a', 'aba', 'aca', 'da', 'eva', 'bcd')
tuple_example_number = ('1', '121', '131', '141', '151', '222')
set_learning_0 = {1, 2, 3, 4, 5}
set_learning_example_web = {'Google', 'Taobao',
                            'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
set_learning_example_web_social = {'Weichat', 'Qq', 'Facebook'}
str_web_needed_judged = 1
set_learning_example_str = set(str_learning_example_number)
set_learning_example_webinfo = set()
dict_learning_example = {}
dict_exapmle_webinfo = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict_example_create = dict(
    [('name', 'runoob'), ('code', 1), ('site', 'www.runoob.com')])
dict_example_create_1 = dict(name='runoob', code=1, site='www.runoob.com')
dict_example_for_0 = {x: x**2 for x in range(1, 3)}
dict_example_for_1 = {x: x**2 for x in (1, 2, 3)}
dict_example_create_list = {'1': [1, 2, 3], '2': [4, 5, 6]}
dict_example_create_list_1 = dict([('1', [1, 2, 3]), ('2', [4, 5, 6])])
dict_example_create_number_0 = dict(
    [('name', 'runoob'), ('1', 'one'), (1, 'one')])
bytes_example_create_0 = bytes('Hello, world!', 'utf-8')
bytes_example_create_1 = b'Hello, world!'


# get_info_0=input('1')
# 第五个字符不包含
# print(str_learning_example_number[1:5])
# 每隔两个字符取一个，2表示步长
# print(str_learning_example_number[1:5:2])
# print(headline_2)
# \n表示换行
# print(r'\n')
# print('\n')
# print(get_info_0)
# sys.stdout.write(headline_2)
# print(str_learning_example_number,end='')
# print(str(sys.argv))
# print(len(sys.argv))
'''
opts, args = getopt.getopt(sys.argv[1:], 'n:u:', ['name=', 'username='])
print(sys.argv[1:])
print(opts, args)
print('112')
'''
# help(sys)
'''
for line in fileinput.input():
    print(line, end='')
'''
# help(print)
# print(headline_0,str_learning_example_number,sep=':',end='\n',file=sys.stdout)
# print('second')
'''
with open('D:\python_learning_program\pythonProject\print_0.txt','w') as file_print_o:
    print('第一个打印到外部文件的句子',file=file_print_o)
'''
'''
file_print_0 = open('D:\python_learning_program\pythonProject\print_0.txt','r')
print(file_print_0.read())
file_print_0.close()
'''
# with open('D:\python_learning_program\pythonProject\input1.txt', 'r') as file_print_0:
# print(file_print_0.read())
# date_type_0, date_type_1,date_type_2,date_type_3=1,1.5,True,1+1.5j
# print(type(date_type_0),type(date_type_1),type(date_type_2),type(date_type_3))
'''
print(2==3)
print(2<3)
print(bool_data_0 and bool_data_1)
print(bool_data_0 or bool_data_1)
print(not bool_data_0)
print(int(bool_data_0))
print(float(bool_data_1))
print(str(bool_data_0))
print(bool(str_learning_example_number))
'''
# list_data_0[0]=100
# list_data_0[3:]=[]
'''
print(list_data_0[0:])
print(list_data_0[0::2])
print(list_data_0[0::3])
print(list_data_0[0::4])
print(list_data_0[::-2])
print(list_data_0[-1::])
'''
# list_data_0 = [1, 2, 3, 4, 5]
# print(list_data_0)
# print(list_data_0[0::-1])
'''
print(list_data_0[::])
print(list_data_0[::-1])
print(list_data_0[-1::-1])
'''
'''
def reverse_sentence(sentence_input):
    sentence_input_list=sentence_input.split(' ')
    sentence_input_list=sentence_input_list[::-1]
    sentence_output=' '.join(sentence_input_list)
    return sentence_output
print(reverse_sentence('one two three four five'))
list_learning_separator_0 = str_learning_separator.split(',')
#list_learning_separator_1 = str_learning_separator.split(' ')
#print(str_learning_separator.split(','))
#print(str_learning_separator.split(' '))
print(list_learning_separator_0)
print(','.join(list_learning_separator_0))
print(' '.join(list_learning_separator_0))
print(''.join(list_learning_separator_0))
'''
'''
print(type(str_learning_example_number))
print(type(tuple_learning_0),type(tuple_learning_1),type(tuple_learning_2))
'''
# print(set_learning_web)
'''
print(set_learning_web)
if str_web_needed_judged in set_learning_web:
    print('str_web_needed_judged' + ' is in set_learning_web')
else:
    print('str_web_needed_judged' +' is not in set_learning_web')
'''
'''
if str_web_needed_judged  in set_learning_0:
    print(str(str_web_needed_judged) +' is in set_learning_0')
else:
    print(str(str_web_needed_judged) +' is not in set_learning_0')
'''
# print(set_learning_example_web)
# print(set_learning_example_str)
# print(set('abcabcd'))
# print(set_learning_example_web-set_learning_example_web_social)
# print(set_learning_example_web_social | set_learning_example_web)
# print(set_learning_example_web_social & set_learning_example_web)
# print(set_learning_example_web_social ^ set_learning_example_web)
# print(tuple_learning_example_list)
# list_data_0.append(number_add_to_list)
# help(list)
# print(tuple_learning_example_list)
# print(tuple_learning_1)
'''

print(dict_learning_example)
print(dict_learning_example['one'])
print(dict_learning_example['1'])
print(dict_exapmle_webinfo)
print(dict_exapmle_webinfo.keys())
print(dict_exapmle_webinfo.values())
'''
dict_learning_example['one'] = '1-runoob lesson'
dict_learning_example[1] = '1-菜鸟课程'
dict_learning_example['1'] = '1-菜鸟课程'
'''
print(dict_example_create)
print(dict_example_create_1)
print(dict_example_for_0)
print(dict_example_for_1)
print(dict_example_create_list)
print(dict_example_create_list_1)
print(dict_learning_example)

print(dict_example_create_number_0)
print(dict_example_create_1)

print(bytes_example_create_0)
print(bytes_example_create_1)
'''
'''
print(ord('h'))
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
if x[0] == 104:
    print("The first element is 'h'")
'''
# print(list_example_transfer)
# print(repr(list_example_transfer))
'''
print(dict_exapmle_webinfo)
for key_example in dict_exapmle_webinfo:
  
  set_learning_example_webinfo.add(key_example)
print(set_learning_example_webinfo)
'''
'''
print(str_learning_example_number)
print(str_learning_example_number[0:0])
'''
'''
for i in list_data_0:
    tuple_example_0=tuple_example_0+(i,)

print(tuple_example_0)
'''
# print(dict_example_create_list_1)
'''
tuple_reduce_word=list(word_in_tuple.strip('a') for word_in_tuple in tuple_example_word) 
tuple_reduce_number=list(number_in_tuple.strip('1') for number_in_tuple in tuple_example_number) 
print(tuple_reduce_word,tuple_reduce_number)
'''
'''
p = {i:str(i) for i in range(1,5)}
print(p)
'''
'''
print(list_data_0)
print(list_data_1)
print(id(list_data_0))
print(id(list_data_1))
'''
'''
def count_1_bin(n):
    str_count_bin=bin(n)
    return str_count_bin, str_count_bin.count('1')
print(count_1_bin(10))
'''
'''
list1 = [1000, 3, 5]
list2 = [1000, 3, 5]
print(list1 is list2)

print(not (number_learning_example_0))
print(not (number_learning_example_0)>5)
'''
# lst = random.sample('abcd1234',4)
# number_from_list=[int(i) for i in list_data_0]
# print(number_from_list)
# print('\\')
'''
for i in range(101):
    print("\r{}%".format(i), end=' ')
    time.sleep(0.05)
print('\n')
print('从1到10依次为',end=' ')
for i in range(1, 11):
   print('{}'.format(i) ,end=' ')
   time.sleep(0.5)
'''
'''
print('格式话变量的地址：%p' % (1))

var = 1
print(f'变量var的地址:{id(var)}')
'''
# print('输出一个单一的%%')
'''
name = "Alice"
age = 25
message = "Name: %-s, Age: %d" % (name, age)
print(message)
'''
'''
errHTML = 
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>

print(errHTML % "An error occurred while processing the request.")

byte_date=b'hello'
print(byte_date.decode())'''
# print(str_learning_separator[:])

# list_2d = [ [i for i in range(5)] for i in range(5)]
# print(list_2d)
'''
a = [1, 2, 3]
b = a
c = []
c = a
d = a[:]
b[0]=100
print(a,b,c,d)
'''
'''
for x in range(10):
  if x%2:
    print('奇数')
  else:
    print('偶数')
'''
# print ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 ])
'''
list01=[1,2,3]
for i in range(len(list01) - 1, -1, -1):
    print(list01[i])
'''
'''
for i in range(5,-1,-1):
    print(i)
    '''
# print(len((1,2,3)))
'''
country_counter = {}
country_0='china'
country_counter[country_0]=1
print(country_counter)
'''
'''
for key, value in items_view:
    print(key, value)
'''
# print('name  rate'.center(20,'-'))
# print('100 %s'%str_learning_separator)
# 创建一个字典
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# tuple_contray_0=((1,'a'),(2,'b'),(3,'c'))
# dict_reverse_0={my_dict[x]:x for x in my_dict}
# print(dict_reverse_0)
# values_of_dict_0 = my_dict.values()
# print(list(values_of_dict_0))
# print(max(tuple_contray_0))
'''
l = [1, 2]
j = ['a', 'b']
k = ['x', 'y']
d = {key: [] for key in l}
print(d)
d = {key: d.copy() for key in j}
print(d)
d = {key: d.copy() for key in k}
print(d)

thisset = set(("Google", "Runoob", "Taobao"))
x=thisset.pop()
print(thisset)
print(x)
'''
# print(set([9,4,5,2,6,7,1,8]))
# print(set({5,4,2,3,1}))
# print(set([5,4,1,3,2]).pop())
'''
sum_example_100=0
sum_first_number=1
while sum_first_number<=100:
    sum_example_100+=sum_first_number
    sum_first_number+=1
print(sum_example_100)

number=input()
print(number)

i=-1
for i in range(-1,-5,-1):
    print(i)
    i-=1

sites=['a','ab','a','abc','as']
for site in sites:
    if len(site)!=2:
        continue
    print({site})
    if site=='abc':
        break
print('over')
'''
'''
sites = ['a', 'ab', 'a', 'abc', 'as']

for site in sites:
    if site == 'abc':
        break
    if len(site) != 2:
        continue
    print({site})

print('over')
'''
'''
for x in range(2,2):
    print(x)
'''
# print(3%2)
'''
for x in range(2,157):
        if 157%x==0:
            print(157,'不是质数',157,'=',x,'*',157//x)
            break    
else:
    print(157,'是质数')
    '''
'''
num_hang=1
num_lie=1
for num_hang in range(1,10):
    for num_lie in range(1,num_hang+1):
        print(f'{num_lie}*{num_hang}={num_hang*num_lie:<2}',end=' ')
    print('\n')
'''
'''
num_hang=1
num_lie = 1
while num_hang<10:
    while num_lie<=num_hang:
          print(f'{num_lie}*{num_hang}={num_hang*num_lie:<2}',end=' ')
          num_lie+=1
    num_hang+=1
    num_lie=1
    print()
'''
'''
#希望降序排列
list_rank=[1,3,2,4,5,7,6,8,9,10]
sum_number=len(list_rank)
for j in range(sum_number-1,0,-1):
    for i in range(0,j):
       if list_rank[i]<list_rank[i+1]:
         list_rank[i],list_rank[i+1]=list_rank[i+1],list_rank[i]
print(list_rank)
'''
'''
for j in range(9,0,-1):
    print(j)
'''
'''
list_rank=[1,3,2,4,5,7,6,8,9,10]
j=len(list_rank)-1
i=0
while j>=1:
        while i<=j-1:
           if list_rank[i]<list_rank[i+1]:
              list_rank[i],list_rank[i+1]=list_rank[i+1],list_rank[i]
           i+=1
        j-=1
        i=0
print(list_rank) 
'''
'''
import random
dict_compete_computer=dict([(1,'石头'),(2,'剪刀'),(3,'布')])
input_player_legal={'石头','剪刀','布','end'}
while 1:
    number_computer = random.randint(1, 3)
    result_computer=dict_compete_computer[number_computer]
    result_player=input('请输入石头，剪刀，布来开始猜拳游戏，或者输出end结束游戏： ')
    if result_player not in input_player_legal:
        print('输入错误，请重新输入')
        continue
    elif result_player=='end':
        print('游戏结束')
        break
    elif result_computer==result_player:
        print('平局')
    elif (result_computer=='石头' and result_player=='剪刀') or (result_computer=='剪刀' and result_player=='布') or (result_computer=='布' and result_player=='石头'):
        print(f'电脑出了{result_computer},你出了{result_player},你输了')
    else:
        print(f'电脑出了{result_computer},你出了{result_player},你赢了')
'''
'''
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if (a*1000+b*100+c*10+d)*4==d*1000+c*100+b*10+a:
                    print(a,b,c,d)
                    x_result=a*1000+b*100+c*10+d
print(x_result)
'''
'''
import random
while True:
 count_number=1
 number_computer_random=random.randint(1, 100)
 while True:
  number_player_input=input('数字在1-100之间，请输入你猜测的数字：')
  while not number_player_input.isdigit():
     number_player_input=input('输入错误，请重新输入')
     count_number+=1   
  number_player_input=int(number_player_input)
  if number_player_input>number_computer_random:
        print('猜大了，请重新输入,',end=' ')
        count_number += 1
        continue
  elif:
        print('猜小了，请重新输入,',end='')
        count_number+=1
        continue
  else:
        print(f'谜底是{number_computer_random},使用了{count_number}次猜测，你猜到了！')
 continue
'''
'''
while True:
    count_number=0
    number_computer_random=random.randint(1,100)
    print('游戏规则，电脑会产生1-100之间的随机数，你可输入你猜想的数字，如果你输入的数字过大，电脑会提示你猜大了，反之会提示猜小了，然后你可继续猜，直到你猜中为止。试试看需要猜多少次吧')
    while True:
        number_player_input=input('请输入你猜测的数字（输入end结束游戏）：')
        count_number+=1
        if number_player_input=='end':
            print('游戏结束')
            exit()
        if not number_player_input.isdigit():
            print('输入错误，请重新输入')
            continue
        number_player_input=int(number_player_input)
        if number_player_input>number_computer_random:
            print('猜大了，请重新输入',end=' ')
            continue
        elif number_player_input<number_computer_random:
            print('猜小了，请重新输入',end=' ')
            continue
        else:
            print(f'你猜对了，电脑出了{number_computer_random},你用了{count_number}次猜测')
            break
'''
'''

# Create an empty canvas
image = Image.new('RGB', (800, 600), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Draw the background - a large half-enclosed space like a big football field
draw.rectangle([0, 0, 800, 600], fill=(200, 200, 200))  # light grey background
draw.rectangle([50, 50, 750, 550], outline=(0, 0, 0),
               width=5)  # the walls around the field

# Add some text to represent the characters and their positions
font = ImageFont.load_default()

# Draw A - the martial artist with the totem
# A is represented as a green circle
draw.ellipse([100, 250, 150, 300], fill=(0, 255, 0))
draw.text((110, 260), "A", fill=(0, 0, 0), font=font)
draw.line([125, 275, 200, 275], fill=(0, 0, 255), width=5)  # A's spear
draw.line([125, 275, 125, 325], fill=(255, 0, 0), width=3)  # A's sword
draw.ellipse([75, 200, 175, 250], outline=(
    0, 0, 255), width=2)  # A's totem (angel-like)

# Draw B - the modern fighter with the totem
# B is represented as a red circle
draw.ellipse([600, 250, 650, 300], fill=(255, 0, 0))
draw.text((610, 260), "B", fill=(255, 255, 255), font=font)
draw.line([625, 275, 700, 275], fill=(0, 0, 0), width=5)  # B's automatic gun
draw.line([625, 275, 625, 225], fill=(0, 0, 0), width=3)  # B's revolver
draw.ellipse([575, 200, 675, 250], outline=(
    255, 165, 0), width=2)  # B's totem (archer-like)

# Save the image to a file
image_path = "/mnt/data/battle_scene.png"
image.save(image_path)
image.show()

image_path
'''
'''
def is_number_zhishu(num):
    if num<3:
        return ''
    for i in range(2,num):
        if num%i==0:
            return ''
    return num
print(is_number_zhishu(10))
'''
'''
a=3
b=7
print(a)
print(b)
while b<=100:
    print(a+b)
    a,b=b,a+b
'''
'''
n = int(input('请输入一个整数:'))


def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
result = []
for i in range(1, n+1):
    result.append(fab(i))

print(result)
'''
'''
class MyClass:
    def __init__(self, x):
        self.x = 2*x

    def print_x(self):
        print(self.x)
# 创建一个MyClass实例
#obj = MyClass(5)
# 调用print_x方法
#obj.print_x()  # 输出：5
# '''

'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x
'''
'''
def hello():
    print("Hello, world!")
hello()
'''
'''
def change(a):
    print(id(a))   # 指向的是同一个对象
    a = 10
    print(id(a))   # 一个新对象


a = 1
print(id(a))
change(a)
print(a)
'''
#!/usr/bin/python3
# 可写函数说明
'''
def printme(str):
   "打印任何传入的字符串"
   print(str)
   return
# 调用 printme 函数，不加参数会报错
printme(1)
'''
'''
def f(a, b, *, c):
    return a+b+c
print(f(1,2,c=3))
'''
#!/usr/bin/python3
# 可写函数说明
'''
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total
# 调用sum函数
total = sum(10, 20)

a = 10
def sum(n):
   n += a
   a = 11
   print('a = ', a, end=' , ')
   print('n = ', n)
sum(3)
'''
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)  # 手动应用装饰器
say_hello()

#!/usr/bin/python3
a = 10
def test():
    b = a + 1  # 修改同名的全局变量，则认为是一个局部变量
    print(a)
test()
print(a)'''
'''
num = 20
def outer():
    num = 10
    def inner():
        global num
        print(num)
        num = 100
        print(num)
    inner()
    print(num)

outer()
print(num)
def outer_function():
    x = 10  # 外部函数作用域的变量

    def inner_function():
        nonlocal x  # 声明x为非局部变量
        x = 20  # 修改外部函数作用域的变量

    inner_function()
    print("外部函数作用域的变量x:", x)  # 打印修改后的值
outer_function()

class demo:
    name = ""

    def _init_(self):
        self.ex()
        self.start()

    def inputName(self):
        global name
        name = input("輸入您的姓名：")

    def getFirstName(self):
        if len(name) <= 0:
            x = "別鬧！請輸入姓名！"
            return x
        else:
            x = name[0]
            return x

    def getLastName(self):
        if len(name) <= 1:
            y = "別鬧！長度不夠！"
            return y
        else:
            y = name[1:]
            return y
myname = demo()
myname.inputName()
print(myname.getFirstName())
print(myname.getLastName())
'''
'''

class Demo:
    def __init__(self):
        self.name = ""

    def input_name(self):
        self.name = input("请输入您的姓名：")

    def get_first_name(self):
        if len(self.name) <= 0:
            return "请输入姓名"
        else:
            return self.name[0]

    def get_last_name(self):
        if len(self.name) <= 1:
            return "姓名长度不够"
        else:
            return self.name[1:]

my_name = Demo()
my_name.input_name()
print(my_name.get_first_name())
print(my_name.get_last_name())
'''
'''
class Person:
    def __init__(self, name, age):
        self.name = name  # name是实例变量
        self.age = age    # age是实例变量


# 实例化Person类的两个对象
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1.name, person1.age)
'''
'''
def demo(*p):
    i=0
    for var in p:
        var(i)
        i+=1
def d1(i):
    print("这里是第一个子函数,输入的数是",i)
def d2(i):
    print("这里是第二个子函数,输入的数是",i)
def d3(i):
    print("这里是第三个子函数,输入的数是",i)
def d4(i):
    print("这里是第四个子函数,输入的数是",i)
demo(d1,d2,d3,d4)
'''
'''
list1 = [1, 2, 3, 4, 5]
list2=list(filter(lambda x: x % 2 == 0, list1))
list3=list(map(lambda x: x**2, list1))
list4=reduce(lambda x,y:x+y,list1)
list5=reduce(lambda x,y:x*y,list1)
print(list2,list3,list4,list5,sep='\n')
'''
'''
def greet(name):
    print(f"Hello, {name}!")

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator





def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
'''
'''
class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.curr_num = 0

    def __iter__(self):
        self.curr_num = 0
        return self

    def __next__(self):
        if self.curr_num < self.max_num:
            self.curr_num += 2
            return self.curr_num
        else:
            raise StopIteration
    def calculate_sum(self):
        return sum(self)

my_iterator = MyIterator(5)
print(list(my_iterator))
print(my_iterator.calculate_sum())

list1=[1,2,3,4,5]
filtered_iterator = filter(lambda x: x % 2 == 0,list1)
print(list(filtered_iterator))  # 输出: [2, 4]
'''
'''
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# 创建一个自定义的迭代器
my_iterator = MyIterator([1, 2, 3, 4, 5])
#print(list(my_iterator))  # 输出: [1, 2, 3, 4, 5]
print(next(my_iterator))
print(list(my_iterator))

# 使用 filter 过滤偶数
filtered_iterator = filter(lambda x: x % 2 == 0, my_iterator)
print(list(filtered_iterator))  # 输出: [2, 4]

# 使用 map 对每个元素进行平方操作
mapped_iterator = map(lambda x: x ** 2, my_iterator)
print(list(mapped_iterator))  # 输出: [1, 4, 9, 16, 25]

'''
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# 使用 .items() 方法获取键值对
# items = my_dict.items()

# 输出字典视图对象中的元素（键值对元组）
# print(items)  # 输出: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 遍历字典视图对象中的键值对元组
# for key, value in items:
#   print(key, value)
# 输出:
# a 1
# b 2
# c 3
'''
array = []
for i in range(30):
    if i % 3 == 0 and i % 5 == 0:
        array.append("能被3-5整除")
    elif i % 5 == 0:
        array.append("能被5整除")
    elif i % 3 == 0:
        array.append("能被3整除")
    else:
        array.append("不能能被3-5整除")

array = ["能被3-5整除" if i % 3 == 0 and i % 5 == 0 else "能被5整除" if i %
         5 == 0 else "能被3整除" if i % 3 == 0 else "不能被3-5整除" for i in range(30)]
print(array)

matrix = [ [7, 2, 9, 4], [5, 6, 9, 8], [9, 10, 11, 12],]
relist1 = [row[i] for i in range(4) for row in matrix]
relist2=[row[i] for row in matrix for i in range(4)]
print(relist1)
print(relist2)
#print( sys.path, '\n')
#print(matrix_transposition.__file__)
matrix =[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],] 
transposed_matrix = matrix_transposition.matrix_transposition(matrix)
#list_0=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
transposed_matrix = matrix_transposition.matrix_transposition(matrix)
# list_0=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)
'''
# print(dir(matrix_transposition))
# print(matrix_transposition.__name__)
'''
if __name__ == '__main__':
    print('main')
    print(__name__)
else:
    print('not main')'''
# print(sys.path)
# file_0.write('hello world\n')
# file_0.seek(0)
# file_0 = open('./test_file/read_write.txt', 'a+')
# print(file_0.readlines())

'''
value = ('www.runoob.com', 14)
s = str(value)
file_0.write(s)
file_0.close()

file_0 = open('./test_file/read_write.txt', 'a+')
print(file_0.tell())
print(file_0.seek(-1, 2))
file_0.close()

file_0 = open('./test_file/read_write.txt', 'ab+')
#print(file_0.tell())
print(file_0.seek(0))
print(file_0.read(1))
file_0.close()
list1 = [1, 2, 3,]
list1.append((3,4,5))
print(list1)
print(list1[3])'''
#!/usr/bin/python3

# 使用pickle模块将数据对象保存到文件
'''
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.txt', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output)

output.close()
#!/usr/bin/python3
# 使用pickle模块从文件中重构python对象
pkl_file = open('data.txt', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'tags': ['python', 'programming', 'data']
}

pprint.pprint(data)

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件
'''
'''
datafile = 'person.data'
line = '======================================='
message = 
=======================================
Welcome bookmark:
    press 1 to show list
    press 2 to add pepole
    press 3 to edit pepole
    press 4 to delete pepole
    press 5 to search pepole
    press 6 to show menu
    press 0 to quit
=======================================

print(message)


class Person(object):
    """通讯录联系人"""

    def __init__(self, name, number):
        self.name = name
        self.number = number

# 获取数据

def get_data(filename=datafile):
    # 文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

# 写入数据

def set_data(name, number, filename=datafile):

    personList = {} if get_data() == None else get_data()

    with open(filename, 'wb') as f:
        personList[name] = Person(name, number)
        pickle.dump(personList, f)

# 保存字典格式的数据到文件

def save_data(dictPerson, filename=datafile):
    with open(filename, 'wb') as f:
        pickle.dump(dictPerson, f)

# 显示所有联系人

def show_all():
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name, v.number)
        print(line)
    else:
        print('not yet person,please add person')
        print(line)

# 添加联系人

def add_person(name, number):
    set_data(name, number)
    print('success add person')
    print(line)

# 编辑联系人

def edit_person(name, number):
    personList = get_data()
    if personList:
        personList[name] = Person(name, number)
        save_data(personList)
        print('success edit person')
        print(line)

# 删除联系人

def delete_person(name):
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)
            print('success delete person')
        else:
            print(name, ' is not exists in dict')
        print(line)

# 搜索联系人
def search_person(name):
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(name).number)
        else:
            print('No this person of ', name)
        print(line)


while True:
    num = input('>>')

    if num == '1':
        print('show all personList:')
        show_all()
    elif num == '2':
        print('add person:')
        name = input('input name>>')
        number = input('input number>>')
        add_person(name, number)
    elif num == '3':
        print('edit person:')
        name = input('input name>>')
        number = input('input number>>')
        edit_person(name, number)
    elif num == '4':
        print('delete person:')
        name = input('input name>>')
        delete_person(name)
    elif num == '5':
        print('search :')
        name = input('input name>>')
        search_person(name)
    elif num == '6':
        print(message)
    elif num == '0':
        break
    else:
        print('input error, please retry')

with open('print_0', 'w+') as f:
    f.seek(0)
    print(f.read())
'''
# print("|", format("RUNOOB"), "|")
'''
pathTmp='D:\python_learning_program\pythonProject\hello.py'
def is_path_pyfile(path):
    return path[(path.rfind('.')+1):] == 'py'

list_pyfile=[]
if is_path_pyfile(pathTmp):
    list_pyfile.append(pathTmp)
print(list_pyfile)

# 指定目录
directory_path = "D:\python_learning_program\pythonProject"

# 使用 os.walk 遍历目录及其子目录
list_pyfile = []
for root, directories, files in os.walk(directory_path):
   for filename in files:
        if filename.endswith('.txt'):
            list_pyfile.append(os.path.join(root, filename))

print(list_pyfile)
try:
    x = 1 / 0  # 会引发 ZeroDivisionError
#except FileNotFoundError:
    #print("File not found error")
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zero division error")


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
    raise'''

'''
try:
        raise NameError('HiThere')  # 模拟一个异常。
except NameError:
        print('An exception flew by!')
   '''
'''
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError('第二种')  # 触发异常
except MyError as e:
    print('My exception occurred, value:', e.value)
'''
'''
def test1():
    print('test1-1')
    print(num)
    print('test2-2')


def test2():
    print('test2-1')
    test1()
    print('test2-2')


def test3():
    try:
        print('test3-1')
        test1()
        print('test3-2')
    except Exception as result:
        print('检测出异常{}'.format(result))
    print('test3-2')


test3()
print('-------------')
test2()

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__class__.__name__)
t = Test()
t.prt()
y=Test()
y.prt()

aaa=son_matrix_transposition([[1,2,3],[4,5,6],[7,8,9]])
print(aaa.matrix_transposition())

random_path = os.path.join(sys.prefix, 'lib', 'python3.8', 'random')
print(random_path)

#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')'''
'''
# 思考题正确答案
class A():
    def __init__(self):
        print('enter A')
        print('leave A')

class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')

class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')

class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

d = D()

class C:
  def __init__(self, a):
    self.a = a

  def construct(self, a):
    c = C(a)
    #self = c

  def getid(self):
    return id(self)


if __name__ == '__main__':
  c1 = C(2)
  print(c1.construct(3) ) # c1.a == 2
 # print(id(c1) == c1.getid())  # True

a=5
def test():
    print(a)
test()

a=5
def test():
    print(a)
test()

b=5
def test1():
    a=1
    b=a
    print(b)'''

# print(os.curdir)
# print(os.listdir(os.curdir))
# print(dir(os))
# import glob
# print(glob.glob('*.py'))

'''
def create_or_update_log_file(filename):
    try:
        # 尝试打开日志文件
        with open(filename, 'a') as file:
            file.write("Log entry\n")

    except FileNotFoundError:
        # 如果文件不存在，向标准错误流输出警告消息，并创建一个新的日志文件
        sys.stderr.write('Warning, log file not found starting a new one\n')
        with open(filename, 'w') as file:
            file.write("New log entry\n")
'''
'''



for line in urlopen('http://http://localhost:51698'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
       print(line)
    print(line)

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45'''

'''

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()   # 自动验证嵌入测试
'''
'''
a=10
print(bin(a))
print(oct(a))
print(hex(a))'''

'''
b=0b1010
b=str(b)
b_10=int(b,2)
print(b_10)
print(oct(b_10))
print(hex(b_10))

c=52
print(type(bin(c)))'''

'''
d=0o77
d=str(d)
d_10=int(d,8)
print(d_10)
print(bin(d_10))
print(hex(d_10))

e=0x2b
e=str(e)
e_10=int(e,16)
print(e_10)
print(bin(e_10))
print(oct(e_10))

a='A'
b=102
print(ord(a))
print(chr(b))'''

'''
text = "123 world"

# 使用 re.match
result_match = re.match(r'\d+', text)
print(result_match.group())  '''

'''
pattern = r'[-+\*/]'  # 加入了转义符号 \，匹配字面意义的 + 和 *
text = "1 + 2 - 3 * 4 / 5"
operators = re.findall(pattern, text)
print(operators)  # 输出: ['+', '-', '*', '/']'''


# with open('./test_file/read_write.txt','r+') as f:
# print(f.read())
# f.write('the second 2024/6/3')
'''
    locate_0=f.tell()
    print(f.seek(locate_0-8))
    print(f.read())'''

# str_0 = 'the first 2024/6/3'
# print(sys.getsizeof(str_0))

'''
mouths_day=calendar.monthrange(2024,6)
mouth_first_day=mouths_day[0]
mouth_sum_days=mouths_day[1]
print(mouth_first_day, mouth_sum_days)'''

'''
str_calcu_0 = '2.5*2.5*2.5'
str_calcu_1 = '10+5'
str_calcu_2 = '10.5-5'
str_calcu_3 = ' 2.5*5'
str_calcu_4 = '2.5*2.5*2.5'
str_calcu_5 = '2.5/0'
str_calcu_6 = '10/5'

print(calcul_num(str_calcu_0))
print(calcul_num(str_calcu_1))
print(calcul_num(str_calcu_2))
print(calcul_num(str_calcu_3))
print(calcul_num(str_calcu_4))
print(calcul_num(str_calcu_5))
print(calcul_num(str_calcu_6))

a=' 2.5* 5'
print(calcul_num(a))

print(type(calendar.month(2024,6)))
print(calendar.month(2024,6))'''

'''
list_0=[1,2,3,4,5]
list_0.append('new')
list_1=list_0.copy()
list_0.extend(['a','b','c'])
list_2=list_0.copy()
list_0.insert(0,'first')
list_3=list_0.copy()
'''
# print(list_0)
# print(list_1)
# print(list_2)
# print(list_3)

# print(list_0[3])
# print(list_0[3:])
# print(list_0[:3])

# print(list_0[1:3])
# print(list_0[::2])
# print(list_0[1:-1])
# print(list_0[::-2])

# print(list_0.index('new'))
# print(list_0.count('new'))
# print('0' in list_0)

'''
list_0=[1,2,3,3,2,1,2,3,1]
for i in list_0:
    if i==2:
        list_0.remove(i)'''

'''
list_1 = [1, 2, 3, 3, 2, 1, 2, 3, 1]
list_2=[i for i in list_1 if i!=2]
print(list_2)

list_1 = [1, 2, 3, 3, 2, 1, 2, 3, 1]
list_1.pop(2)
print(list_1)

list_1 = [1, 2, 3, ]
list_2=list_1+[4,5,6]
print(list_2)   
list_3=list_1*2
print(list_3)   '''

'''
list_1 = ['one', 'two', 'three','four','five' ]
str_1=' '.join(list_1)
print(str_1)
list_2=str_1.split(' ')
print(list_2)
list_3=[i*2 for i in list_1]
print(list_3)'''

'''
dict_0 = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
list_0=dict_0.keys()
list_1=dict_0.values()
list_2=dict_0.items()
list_3=[k for k,v in list_2]
list_4=[v for k,v in list_2]
list_5=[(k,v) for k,v in list_2]
list_6=['%s=%s' % (k,v) for k,v in list_2]
print(list_0)
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(list_6) '''

'''
list_1 = ['one', 'two', 'three', 'four', 'five']
list_2=[i for i in list_1 if len(i)==3] 
print(list_2)
list_3=[i for i in list_1 if len(i)!=3] 
print(list_3)'''

'''
dict_0={}
i=1
while i<=100:
    j=1
    while j<=9:
       dict_0[i]=j
       j+=1
       i+=1  
       if i==101:
           break'''
'''
peple =[]
for i in range(1,31):
    person = 'person%d'%i
    peple.append(person)

c = 0
max =30
t = 0
while max >15:
    god = []
    for pe in peple:
        c += 1
        if c % 9 == 0:
            print(c,pe,'离开')
            max -= 1
            god.append(pe)
    for pe in god:
        peple.remove(pe)
print('留下人员',peple)
'''
'''
liver = list(range(1, 31))
index = 1
list_index = index - 1
while True:
    if len(liver) <= 15:
        break
    else:
        if index == 9:
            print('{0}号下船了'.format(liver[list_index]))
            liver.remove(liver[list_index])
            index = 1
        else:
            index += 1
            list_index += 1
        if list_index == len(liver):
            list_index = 0'''

'''
people = list(range(1, 31))
while len(people) > 15:
    i = 1
    while i < 9:
        people.append(people.pop(0))
        i += 1
    print('{:2d}号下船了'.format(people.pop(0)))
'''

'''
sum = list(range(1, 31))
while len(sum) > 15:
    for i in range(8):
        sum.append(sum.pop(0))
    print('{}号下船了'.format(sum.pop(0)))'''

# print(1%5==1)
# print(0/5*4)

'''
print('按下enter键开始计时，ctrl+c退出计时')
input('')
starttime=time.time()
try:
    while True:
      print('时间：',round(time.time()-starttime,1),'秒')
      time.sleep(1)
except KeyboardInterrupt:
    endtime=time.time()
    print('总共用时：',round((endtime-starttime),1),'秒')'''

# result = 0
# for i in range(1, 10):
#    result += i**3
# print(result)

# 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。


def reverse_array(arr, d):
    arr += arr[:d]
    arr = arr[d:]
    return arr


'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(list_1)
list_2=list_1.copy()
the_first=list_2.pop(0)
the_end=list_2.pop()
list_3=[the_end,]+list_2+[the_first,]
print(list_3)

list_4=list_1.copy()
list_4[0],list_4[-1]=list_4[-1],list_4[0]
print(list_4)

list_5=list_1.copy()    
list_5[0],list_5[4]=list_5[4],list_5[0]
print(list_5)
'''
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_6=list_1.copy()
list_6=list_6[::-1]
print(list_6)

list_2=list_1.copy()
list_2.reverse()
print(list_2)

list_0=[1,2,3,4,5,6,7,8,9]
list_0.clear()
print(list_0)

list_0=[1,2,3,4,2,3,2,3,2]
for i in list_0:
    while list_0.count(i)>1:
        list_0.remove(i)
print(list_0)

list_1=[1,2,3,4,2,3,2,3,2]
list_1=list(set(list_1))
print(list_1)

list_0=[1,2,3,4,2,3,2,3,2]
set_0=set()
list_1=[]
for i in list_0:
    if i not in set_0:
        set_0.add(i)
        list_1.append(i)
print(list_1)    

dict_0={1:2,2:3,3:4}
dict_1=list(dict_0)
print(dict_1)

keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys, 0)
print(list(my_dict))  # 输出 {'a': 0, 'b': 0, 'c': 0}

list_0=[1,2,3,4,2,3,2,3,2]
list_1=[]
[list_1.append(i) for i in list_0 if i not in list_1]
print(list_1)

list_0=[2,3,4,2,3,2,3,2,5]
list_1=[1,2,2,4,4,5]
set_common=set(list_0)&set(list_1)
list_2=[i for i in list_0 if i not in set_common]
list_3=[i for i in list_1 if i not in set_common]
print(list_2)
print(list_3)

list_0=[2,3,4,2]
list_1=list(list_0)
#print(list_1)
#print(list_0.count(2))
sum=0
for i in range(0,len(list_0)):
    sum+=list_0[i]
print(sum)'''

'''
list_0=[2,3,4,2]
sum=reduce(lambda x,y:x+y,list_0)
multiple=reduce(lambda x,y:x*y,list_0)
print(sum)
print(multiple)

str_0='hello world'
str_1=str_0[0:5]+str_0[6:]
print(str_1)

# 匹配日期，但不捕获年份
pattern = r"(?:\d{2})-(\d{2})-(?:\d{4})"
text = "Today's date is 01-23-2022."
match = re.search(pattern, text)
if match:
    print(match.group(0))
    print(match.group(1))  '''

'''
code = 'a = 5\nb = 10\nprint("Sum:", a + b)'

exec(code)

str_0='hello world'
print(str_0[0:-5])'''

# dict_0={10:5,9:3,1:2,8:4,9:10}
'''
print(sorted(dict_0))
for i in sorted(dict_0):
    print(i,dict_0[i])'''
# print(sorted(dict_0,reverse=True))
# print(sorted(dict_0.items(), key=lambda kv: (kv[1], kv[0])))
'''
list_0=sorted(dict_0)
dict_1={x:dict_0[x] for x in list_0}
print(dict_1)

tuple_0=sorted(dict_0.items(), key=lambda kv: (kv[1], kv[0]))
dict_2={x:y for x,y in tuple_0}
print(dict_2)

lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }] 
list_1 = sorted(lis, key=lambda x: x["age"]) 
list_2 = sorted(lis, key=lambda x: x["age"],reverse=True) 
print(list_1) 
print(list_2)
sum=0
for i in lis:
    sum+=i['age']
print(sum)'''

'''
dict_0={1:'ok',2:'ok',3:'ok'}
sum=''
for i in dict_0:
    sum+=dict_0[i]
print(sum)

print(dict_0.keys)
print(dict_0.values)
print(reduce(lambda x,y:x+y,dict_0.values()))'''
'''
dict_0={1:'ok',2:'ok',3:'ok'}
dict_1={4:22,5:33,6:44}
dict_3={**dict_0,**dict_1}
#dict_0.update(dict_1)
#del dict_0[2]
#print(dict_0)
#dict_0.pop(2)
#print(dict_0)
#dict_1={k:v for k,v in dict_0.items() if k==2}
print(dict_3)'''

'''
a1 = "2019-5-10 23:40:00"
timearray = time.strptime(a1, '%Y-%m-%d %H:%M:%S')
print(timearray)
#timestamp=int(time.mktime(timearray))
#print(timestamp)
str_time=time.strftime('%Y-%m-%d %H:%M:%S',timearray)
print(str_time)

date_time_now=datetime.datetime.now()
print(date_time_now)
#time_now=time.time()
#print(time_now)
date_three_days_ago=date_time_now-datetime.timedelta(days=3)
print(date_three_days_ago)
timestamp_three_days_ago=int(date_three_days_ago.timestamp())
date_three_days_ago_str=date_three_days_ago.strftime('%Y-%m-%d %H:%M:%S')
print(date_three_days_ago_str)
print(timestamp_three_days_ago) '''

# date_three_days_ago=datetime.datetime.now()-datetime.timedelta(days=3)
# print(date_three_days_ago)


# 获取当前时间
'''current_time = datetime.datetime.now()

# 计算3天前的时间
three_days_ago = current_time - datetime.timedelta(days=3)

print("三天前的时间:", three_days_ago)


dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
three_days_ago = dateArray - datetime.timedelta(days=3)
str_three_days_ago = three_days_ago.strftime('%Y-%m-%d %H:%M:%S')
print(str_three_days_ago)'''


'''# 先获得时间数组格式的日期

threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
print(threeDayAgo)

# 转换为时间戳
#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
#three_days_ago_str = time.strftime('%Y-%m-%d %H:%M:%S',threeDayAgo)
#print(three_days_ago_str)
print(otherStyleTime)'''

'''
timestamp_0=time.time()
time_tuple=time.localtime(timestamp_0)
time_str=time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
print(time_str)

time_now=datetime.datetime.now()
time_str=time_now.strftime('%Y-%m-%d %H:%M:%S')
print(time_str)

print("..######..\n..#....#..\n..######..", end = " ") 
print("\n..#....#..\n..#....#..\n\n") 

t_0=[1,2]
element=3
print(serch_element(list_0,element,0,len(list_0)-1))'''

'''输入的字符串为aaabc，count[97]=0+1,count[97]=1+1,count[97]=1+1+1,count[98]=0+1,count[99]=0+1
count[97]=3,count[98]=1,count[99]=1
count[97]=count[97]+0=3,count[98]=count[98]+count[97]=1+3=4,count[99]=count[99]+count[98]=1+4=5
count[97]=3,count[98]=4,count[99]=5
i=0,output[4]=c  count[99] =5-1=4 
i=1,output[3] = b count[98] =4-1=3 
i=2,output[2] = a count[97] =3-1=2 
i=3,output[1] = a count[97] =2-1=1 
i=4,output[0] = a count[97] =1-1=0 

'''
# print(next(gen))
# print(feibo(1))
# print(feibo(10))

'''fib_gen = fibonacci_generator()
list_1=[]
for _ in range(10):
    list_1.append(next(fib_gen))
print(list_1)

list_0=['  a ','b ','c ','d ','e ']
for i in list_0:
    print(i.strip())'''

# list_0 = ['\nhello\n', '\nworld\n', '\ni\n', '\nam\n']
# print(list_0[0], list_0[1], list_0[2], list_0[3])
'''
print(list_0[0].strip(),list_0[1].strip(),list_0[2].strip(),list_0[3].strip())
list_1=[]
for i in list_0:
    i_tran=re.sub(r'^\s+|\s+$','',i)
    list_1.append(i_tran)
print(list_1[0],list_1[1],list_1[2],list_1[3])'''

# print(list_0[0].strip(), list_0[1].strip(),list_0[2].strip(), list_0[3].strip())
# print(list_0[0].lstrip(), list_0[1].lstrip(), list_0[2].lstrip(), list_0[3].lstrip())
# print(list_0[0].rstrip(), list_0[1].rstrip(), list_0[2].rstrip(), list_0[3].rstrip())


'''my_list = ["apple", "banana", "cherry", "date"]
#my_list.sort(key=lambda x: len(x), reverse=True)
list_new=sorted(my_list,key=lambda x: len(x),reverse=True)
print(list_new)
#print(my_list)
list_1=[1,2,5,3,4,6,7,8,9]
list_2=sorted(list_1,key=lambda x:x)
print(list_2)

tasks=['go']
print(list(enumerate(tasks, start=1)))
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")'''
# print(list_remove(30,9,15))

'''list_0=[i for i in range(1,31)]
print(list_0)
list_0=list_0[8:]+list_0[:8]
print(list_0)
remove=list_0.pop(0)
print(remove)
print(list_0)'''
'''
peple =[]
for i in range(1,31):
    person = 'person%d'%i
    peple.append(person)
c = 0
max =30
t = 0
while max >15:
    god = []
    for pe in peple:
        c += 1
        if c % 9 == 0:
            print(c,pe,'离开')
            max -= 1
            god.append(pe)
            peple.remove(pe)
print('留下人员',peple)      

x = [1, 2, 3]
random.shuffle(x)
print(x)  # 输出的顺序会是 [3, 1, 2] 或者其他打乱的顺序 '''


# str_1='http://www.baidu.com'
# match_0=re.match(r'http://',str_1)
# print(re.match(r'http://', str_1).span())
# print(re.match(r'https://',str_1))
# print(re.match(r'https://', str_1).span())
# print(re.match(r'www',str_1))
# print(match_0.group(0))

'''str_='cats are smarter than dogs cats cats'
pattern_0=r'(.*) are (.*?) (.*)'
match_0=re.match(pattern_0,str_,re.M|re.I)
print(match_0.group(0))
print(match_0.group(1,2,3)

print(re.search(r'cat',str_).group(0))
print(re.search(r'dog',str_).group(0))

number='400-800-1200 #来自天外的号码'
number_0=re.sub(r'#.*$', '', number)
print(number_0)
number_1=re.sub(r'\D', '', number_0)
print(number_1)
print(number)

s = 'A23G4HFD567'
def double_num(match):
    match_num=int(match.group('num'))
    return str(match_num*2)
new_s=re.sub(r'(?P<num>\d+)' ,double_num ,s)
print(new_s)

s = 'A23G4HFD567'
print(re.search(r'\d*',s).group(0))

pattern=re.compile(r'\d+')
match_0=pattern.match('odjfodd111',7,10)
match_1=pattern.match('111gfh')
print(match_0)
print(match_1.group(0))
print(match_0.start())
print(match_0.end())
print(match_0.span())


str_0='Hello World Wide Web'
pattern_0=re.compile(r'([a-z]+) ([a-z]+)',re.I)
match_0=pattern_0.match(str_0)
print(match_0.group(0))
print(match_0.group(1))
print(match_0.group(2))
print(match_0.start(1))
print(match_0.end(2))
print(match_0.span(1))
print(match_0.span(2))

str_0='runoob 123 google 456'
#match_0=re.findall(r'\d+',str_0)
#print(match_0)
pattern_0=re.compile(r'([a-z]+) (\d+)')
match_0=pattern_0.findall(str_0)
print(match_0)
for i in match_0:
    print(i)

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match)

str_0='.runoob, runoob, runoob.'
pattern_0=r'(\W+)'
match_0=re.split(pattern_0,str_0)
print(match_0)

pattern_0=re.compile(r'\d+')
print(pattern_0)

pattern_0=re.compile(r'(\d+)([a-z]+)')
def tran_data(match):
    return str(match.group(2))+str(match.group(1))
match_0=pattern_0.sub(tran_data, '123abc')
print(match_0)

regex = re.compile('123.*', re.S)
x=regex.sub('123*', '123ab\nc')
print(x)


s = "apple apple pear pear orange banana"
pattern = r'(\w+)\s\1'
matches = re.findall(pattern, s)
print(matches)  # 输出: ['apple', 'pear']


s = "apple apple pear pear orange banana"
pattern = r'(\w+)\s\1'
matches = re.finditer(pattern, s)
for match in matches:
    print(match.group(0))  # 输出完整的匹配内容


def time_print(gap):
    for i in range(5):
        time.sleep(gap)
        print(i,gap)

tread_0=threading.Thread(target=time_print,args=(1,))
tread_1=threading.Thread(target=time_print,args=(2,))
tread_0.start()
tread_0.join()  
print('tread_0 end')
tread_1.start()


# 定义一个简单的函数作为线程的目标

def worker(num):
    print(f'线程{num}开始执行')
    time.sleep(6-num)
    print(f'线程{num}执行结束')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

# 等待所有线程执行结束
for t in threads:
    t.join()

print('所有线程执行结束')


#!/usr/bin/python3


exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")


my_list = [1, 2, 3]
print(dir(my_list))


class MyClass:
    def __init__(self, value):
        self.value = value


obj1 = MyClass(5).value
obj2 = MyClass(10).value

result = obj1 + obj2  # 如果没有定义 __add__ 方法，这里会抛出 TypeError 错误
print(result)'''


'''# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')

# 返回 json 数据
print(x.json())


# 导入 requests 包
import requests

 
kw = {'s':'python 教程'}

# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://www.runoob.com/", params = kw, headers = headers)

# 查看响应状态码
print (response.status_code)

# 查看响应头部字符编码
print (response.encoding)

# 查看完整url地址
print (response.url)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)



url = "https://www.zhihu.com/api/v3/account/api/login/qrcode"

headers = {
    "x-zse-93": "101_3_3.0",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZniu0e6nXc8YqXLFZkArZkCOOovNMiwCL7iu0e6kXeTFZKHFZrL_BkvO17820XM20cL_1kwxYUqwTmMFZSiUqe6nxE_YywLOm-Uw1tukR-JS8zGXTgwL1Aunu0cXCnJXI7Qr0EMYxc4PGtJH8gcVBAu3OuufIK82CzcpTdXtuSRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThXwM2bVOZUxpbwN_hB3f2cVCQCwsDqXCiwH1WwNGDvX_o4NY7GOqJBLMIUYPvHe_Mq38HJCOh928NutLvCCGtqrM2gYVnGoCTGxGAupCbqc_FuCmbGF9wrgMQcLp1gCCzgLyo7e9o4emJ7VqG931i9Nfe_XM8hCmpDHLzcwy-ut19wHC4qfzqqLGkD3YrDCLFDHCQQeCYgo_sqomyUo8Bc38iwtsBDCKDgO8LcOLoTL_cq3_3GYOuwHBtgtOnwHmsGLZrRpKrrH_ygeB_gwBfU9m_beVbU2M5wXO-r3C",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.249.400 QQBrowser/12.5.5658.400",
    "x-zse-96": "2.0_wIuxY3JupaB1=Sn7z5Hi7AFqYsU9wjaqV=HrvVQqbq6GbpRXdFlvs2HA0SeH/TmR",
    "x-requested-with": "fetch",
    "x-xsrftoken": "dYfjVSiP41VsZA4zki1yBfCFbYchvvMQ",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"",
    "Accept": "*/*",
    "Origin": "https://zhuanlan.zhihu.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://zhuanlan.zhihu.com/p/102392715",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

cookies = {
    "_xsrf": "dYfjVSiP41VsZA4zki1yBfCFbYchvvMQ",
    "__zse_ck": "001_Nl2k8Ej6jP1bb/hwNbKwzEzVM8qQV26Mg+yHmgAXSoKDfJUNq=lHGSxSbzBF5vJcPE9eABwe16LMAa7hFfRy5zBvvbKoUBEahK3rUPPEo7tFjCBWu4mISw6E95V3ILQt",
    "_zap": "1adebe0d-346e-4eb4-95a0-c49f71460e97",
    "d_c0": "ALAQ9m6kwhiPTtUVyN7TzGvWkp4ghpL-axs=|1718159085",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1718159092",
    "captcha_session_v2": "2|1:0|10:1718163446|18:captcha_session_v2|88:bzkwSmdVL0RSYlB0bWFna3htMHMrak9qZ1VBREUwQlZoU0lxSkk4Z3JxMzZSYzBWdjJTNGwvMTdBMFVYSk9qSw==|f9cf194b91bf761dcb47c9c667c3104c6957530c1f618d70902b7f2708d02e33",
    "gdxidpyhxdE": "CCqUIJq8raKz87EzioDoTEUvqivcxSjkkt%2B13o%2BRk04m%5CMG79HM6BemIy0s5%2B2sewCgYyj1Q9hgntbA558HoH8AMbE%2BPf4Gi4DR4%2BiMeDv63IsLE6dGWa%5CgEJp3HoT7ac5ltTsSA%2B2yExLDfQp5%2BX8uosUTHKDnMKpE%2F0QaHCcKNn5p8%3A1718166668037",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1718173154",
    "BEC": "b0eab4e8c2499716509071e260d20835",
    "KLBRSID": "fb3eda1aa35a9ed9f88f346a7a3ebe83|1718173144|1718173143",
}

response = requests.post(url,headers=headers,cookies=cookies)
print(response.json())    


sha256_hash = hashlib.sha256()
sha256_hash.update(b'Hello, ')
print(sha256_hash.hexdigest())
sha256_hash.update(b'Runoob!')
print(sha256_hash.hexdigest())

end_time_0=datetime.datetime.now()
str_end_time_0=end_time_0.strftime('%Y-%m-%d')
print(str_end_time_0)

#start_time_0=
#share_data=yf.download('',start=)

# 获取当前日期
current_date = datetime.datetime.now()
str_current_date = current_date.strftime('%Y-%m-%d')
#print(type(current_date))

# 计算三个月前的日期
three_months_ago = current_date - datetime.timedelta(days=10)
str_three_months_ago = three_months_ago.strftime('%Y-%m-%d')
#print("三个月前的日期:", three_months_ago)

share_data=yf.download('600519.SS',start=str_three_months_ago,end=str_current_date)
print(share_data.head())



import yfinance as yf

# 获取股票数据
symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)
print(data.head())

from selenium import webdriver
print(webdriver.Remote)'''

#//*[@id="kw"]

'''k=345
def sum_0(num):
    one=345*240*1.5
    return int(one*num/100) 

def sum_1(num):
    one=320*100*1.5+320*180*2*0.55*1.5
    return int(one*num/100)

print(sum_0(4),sum_1(4))

gn=9*2.4
hz=9+9*0.55*1.8*2
print(gn,hz)'''






