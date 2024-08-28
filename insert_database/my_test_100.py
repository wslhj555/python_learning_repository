# 1.找到2000-3200(包含)之间所有的能被7整除但是不被5整除的数，打印出来
import math
import random
import copy
import re
list1_one = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        list1_one.append(i)
# print(list_one)

# 2.给定一个列表，计算列表每个数的阶乘，并保存


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


list2_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2_three = []
for i in list2_two:
    list2_three.append(factorial(i))
# print(list2_three)

# 3.生成一个字典，键值对为i:i*i,i是1到n之间的数字


def create_dict(n):
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = i*i
    return my_dict


def create_dict_two(n):
    return {i: i*i for i in range(1, n+1)}
# print(create_dict_two(5))


# 4.将一个逗号分割的数字带单位序列，转化成一个列表或者数组
list4 = ['100个', '10日', '9号', '5头', '3千']
list4_one = re.findall(r'[0-9]+', ','.join(list4))
# print(list4_one)
list4_one = [int(i) for i in list4_one]

'''list4_one=[]
for i in list4:
    if '个' in i:
        list4_one.append(int(i.split('个')[0]))
    elif '日' in i:
        list4_one.append(int(i.split('日')[0]))
    elif '号' in i:
        list4_one.append(int(i.split('号')[0]))
    elif '头' in i:
        list4_one.append(int(i.split('头')[0]))
    elif '千' in i:
        list4_one.append(int(i.split('千')[0]))

tuple4_two=tuple(list4_one)
print(tuple4_two)'''
# print(list4_one)

# 5.定义一个有两个方法的类，1.getString，从控制台获取字符串，2.打印大写的字符串


class String:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("请输入字符串：")
        return self.string

    def printUpperString(self):
        print(self.string.upper())


'''if __name__ == '__main__':
    my_string = String()
    my_str=my_string.getString()
    print(my_str)
    my_string.printUpperString()'''

# 6.根据给定的公式，计算打印值

'''import math
c=50
h=30
value=[]
print('请输入组数字值')
items=[i for i in input().split(',')]
print(items)
for d in items:
    value.append(int(math.sqrt(2*c*float(d)/h)))
print(value)'''

# 7.x，y为输入，生成二维数组，数组的第i行第j列的元素值是i*j，一共x行，y列，最终生成的列表是x个内嵌列表


def create_2d_array(x, y):
    my_array = []
    for i in range(x):
        my_array.append([])
        for j in range(y):
            my_array[i].append(i*j)
    return my_array


def create_2d_array_two(x, y):
    return [[i*j for j in range(y)] for i in range(x)]

# print(create_2d_array_two(3,4))
# print(create_2d_array(3,4))

# 8.一个字符串，以逗号分割，按照字母顺序进行排序，然后再以逗号分割打印，比如输入的是without，hello，bag，world


def sort_string(str):
    str_list = str.split(',')
    str_list.sort()
    return ','.join(str_list)
# print(sort_string('without,hello,bag,world'))

# 9.接受一行字符，将所有字符大写后输出，输入为without，hello，bag，world


def upper_string(str):
    return str.upper()
# print(upper_string('留without,hello,bag,world'))

# 10，输入为以空格为分割的字符串，删掉重复单词后，按照字母顺序打印这些单词，输入的是liu hong jie amen


def remove_duplicate_word(str):
    list10_1 = str.split(' ')
    list10_2 = list(set(list10_1))
    list10_2.sort()
    return ' '.join(list10_2)
# print(remove_duplicate_word('liu hong jie amen liu hong jie amen'))

# 11.输入为四位二进制数，用逗号分割的字符串，现在需要把能被5整除的数找出来，以逗号分割输出，输入为1010,1100,1011,1110,1001,1101,1010,1111


def find_5(str):
    list11 = str.split(',')
    list11_1 = []
    for i in list11:
        if int(i, 2) % 5 == 0:
            list11_1.append(i)
    return ','.join(list11_1)
# print(find_5('1010,1100,1011,1110,1001,1101,1010,1111'))

# 12.12.找到1000-3000之间所有位数都是2倍数的数


def is_multiple_2(n):
    thounds = n//1000
    hundreds = (n-thounds*1000)//100
    tens = (n-thounds*1000-hundreds*100)//10
    ones = n-thounds*1000-hundreds*100-tens*10
    if thounds % 2 == 0 and hundreds % 2 == 0 and tens % 2 == 0 and ones % 2 == 0:
        return n
    else:
        return False


def find_multiple_2(start, end):
    result = []
    for i in range(start, end+1):
        if is_multiple_2(i):
            result.append(i)
    return result

# print(find_multiple_2(1000,3000))

# 13.输入一串字符串，如hello,world?  20124,计算有多少字母，多少数字


def count_char(str):
    count_letter = 0
    count_digit = 0
    for i in str:
        if i.isalpha():
            count_letter += 1
        elif i.isdigit():
            count_digit += 1
    return count_letter, count_digit
# print(count_char('hello,world?  20124'))

# 14.计算大写字母和小写字母的数量，比如输入Liu Hong Jie20141


def count_upper_lower(str):
    count_upper = 0
    count_lower = 0
    for i in str:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    return count_upper, count_lower
# print(count_upper_lower('Liu Hong Jie20141'))

# 15.给定a的值，计算a+aa+aaa+aaaa的值


def calculate(a):
    return 4*a+3*10*a+2*100*a+1*1000*a


def calculate_two(a):
    return a+int(f'{a}{a}')+int(f'{a}{a}{a}')+int(f'{a}{a}{a}{a}')
# print(calculate_two(9))

# 16.使用列表推导输出列表中的每个奇数，列表的输入来源于一串数字


def odd_list(str):
    return [int(i) for i in str.split(',') if int(i) % 2 != 0]
# print(odd_list('1,2,3,4,5,6,7,8,9'))


# 17.输入一串字符串tom，19,80；john，20,90；json，21,85，升序对元组进行排列，元组结构（name，age，height），先根据name，再根据age，再根据height排序
def sort_tuple(str):
    list17 = [(i.split(',')[0], int(i.split(',')[1]), int(i.split(',')[2]))
              for i in str.split(';')]
    list17.sort(key=lambda x: x[0])
    list17.sort(key=lambda x: x[1])
    list17.sort(key=lambda x: x[2])
    return list17


def sort_tuple_two(str):
    list17 = [(i.split(',')[0], int(i.split(',')[1]), int(i.split(',')[2]))
              for i in str.split(';')]
    return sorted(list17, key=lambda x: (x[0], x[1], x[2]))
# print(sort_tuple_two('tom,19,80;john,20,90;json,21,85'))


tuple_list = [('john', 20, 90), ('json', 21, 85), ('tom', 19, 80)]
tuple_list.sort(key=lambda x: (x[0], x[1], x[2]))
# print(tuple_list)

# 18.使用生成器定义一个类，生成器可以在0-n范围间迭代可以被7整除的数字


class MyGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i


my_generator = MyGenerator(30)


def generater_18(n):
    for i in range(n):
        if i % 7 == 0:
            yield i


my_gen = generater_18(30)
list_gen_18 = []
for i in my_gen:
    list_gen_18.append(i)
# print(list_gen_18)

list18 = []
for i in my_generator:
    # print(i)
    list18.append(i)


# 19.给定一个列表，里面有数字，字符，统计每个元素出现的次数，按字母顺序对键进行排序后输出
def count_element(list19):
    count_dict = {}
    for i in list19:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return dict(sorted(count_dict.items()))


list_19 = ['apple', 'banana', 'apple', 'orange',
           'banana', 'pear', 'apple', 10, 20, 30, 10]
list_19_str = [str(i) for i in list_19]
# print(count_element(list_19_str))

# 20.使用**计算数字的平方


def square(n):
    return n**2

# print(square(3))

# 21.获取一个内置函数的文档，doc（）
# print(abs.__doc__)
# print(str.upper.__doc__)

# 22.定义一个类，他具有类参数，且有相同的实例参数


class Myclass22:
    class_param = 30

    def __init__(self, class_param):
        self.class_param = class_param

    def instance_method(self, instance_param):
        print(
            f"Class parameter: {self.class_param}, Instance parameter: {instance_param}")

# my_object = Myclass22(10)
# my_object.instance_method(20)
# print(Myclass22.class_param)

# 23.定义一个类，他具有类参数，且有相同的实例参数，且实例方法可以修改类参数


class Myclass23:
    def __init__(self, class_param):
        self.class_param = class_param

    def instance_method(self, instance_param):
        self.class_param = instance_param
        print(
            f"Class parameter: {self.class_param}, Instance parameter: {instance_param}")


# 23.定义一个求和的函数
def get_sum(*args):
    result = 0
    for i in args:
        result += i
    return result
# print(get_sum(1,2,3,4,5))

# 24.定义一个将整数转化为字符串，并打印的函数


def int_to_string(num):
    print(str(num))
# int_to_string(10)

# 25.定义一个函数，接受多个字符串，求和


def get_sum_25(*args):
    result = 0
    for i in args:
        result += int(i)
    return result
# print(get_sum_25('1','2','3','4','5'))

# 26.定义一个函数，他能将多个字符串连接起来


def join_string(*args):
    return ''.join(args)
# print(join_string('hello','world','ok'))

# 27.定义一个函数，输入两个字符串，将他们以最大长度输出，如果他们长度相等，则将他们分两行打印


def print_centered_string(s, width):
    centered_str = s.center(width, '*')
    print(centered_str)

# print_centered_string('hello', 50)

# 28.定义一个函数，接受一个整数，判断奇数还是偶数


def is_odd_or_even(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
# print(is_odd_or_even(3))

# 29.定义一个函数，打印一个字典，其中键值对是平方的关系


def create_square_dict(n):
    mydict = {}
    for i in range(1, n+1):
        mydict[i] = i**2
    return mydict
# print(create_square_dict(5))

# 31.定义一个函数，生成一个字典，键值对是平方关系，打印值


def get_dict_value(n):
    mydict = {i: i**2 for i in range(1, n+1)}
    list31 = []
    for i in mydict.values():
        list31.append(i)
    return list31


# print(get_dict_value(5))
dict31 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
list31 = []
for key, value in dict31.items():
    list31.append(key)
# print(list31)

# 33.打印一个列表，元素是1-n之间的平方


def get_square_list(n):
    return [i**2 for i in range(1, n+1)]
# print(get_square_list(5))


# 34.取列表前5个值
list34 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def get_list_first_5(list34):
    return list34[:5]
# print(get_list_first_5(list34))

# 35.获取列表最后5个元素


def get_list_last_5(list34):
    return list34[-5:]
# print(get_list_last_5(list34))

# 36.定义一个函数，打印除前五之外的值


def print_list_except_first_5(list34):
    return list34[5:]

# print(print_list_except_first_5(list34))

# 37.获取一个元组，里面是1-n的平方


def get_tuple_square(n):
    return tuple(i**2 for i in range(1, n+1))


def get_tuple_square_2(n):
    tuple37 = ()
    for i in range(1, n+1):
        tuple37 += (i**2,)
    return tuple37


# print(get_tuple_square_2(5))
list_000 = [1, 2, [1, 2]]
list_001 = copy.deepcopy(list_000)
list_001[2][0] = 3
# print(list_000)
# print(list_001)

# 38.给定一个元组，对元组切片，获得两个元组，前半部分和后半部分


def get_tuple_part(tuple38):
    return tuple38[:len(tuple38)//2], tuple38[len(tuple38)//2:]
# print(get_tuple_part((1,2,3,4,5,6,7)))


# 39.给定一个元组，将元组中的偶数取出，组成一个新元组
tuple39 = (1, 2, 3, 4, 5, 6, 7)


def get_tuple_even(tuple39):
    return tuple(i for i in tuple39 if i % 2 == 0)
# print(get_tuple_even(tuple39))

# 40.给定一个字符串，如果字符串是yes或者Yes，或者YES，为真，否则为假


def is_yes(str):
    if str == 'yes' or str == 'Yes' or str == 'YES':
        return True
    else:
        return False

# print(is_yes('YEs'))


# 41.给定一个列表，使用过滤函数过滤列表的偶数
list41 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_even(list41):
    return list(filter(lambda x: x % 2 == 0, list41))


list41_0 = filter(lambda x: x % 2 == 0, list41)
# print(list41_0)
# print(filter_even(list41))

# 42.给定一个列表，使用map函数将列表中的元素转化为字符串
list42 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def map_to_string(list42):
    return list(map(str, list42))
# print(map_to_string(list42))

#


def map_and_filter(list42):
    return list(map(lambda x: str(x), filter(lambda x: x % 2 == 0, list42)))
# print(map_and_filter(list42))


list_44 = [1, 2, 3, 4, 5]
list44_0 = list(map(lambda x: x**2, list_44))
# print(list44_0)

# 45.定义一个American类，一个printNation的静态方法


class American:
    @staticmethod
    def printNation():
        print("America")

# American.printNation()

# 46.定义一个类，和子类


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    name = 'a  dog'

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    @classmethod
    def bark(cls):
        cls.name = 'a bad dog'
        print(cls.name+"wangcai wangcai wangcai")


dog1 = Dog("wangcai", 2)
# print(dog1.name)
# print(dog1.age)
# Dog.bark()
# 47.定义一个Circle类，用半径构造，定义一个计算面积的方法


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2


circle47 = Circle(3)
# print(circle47.get_area())

# 48.定义一个Rectangle类，有长度和宽度构造，一个计算面积的方法


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length*self.width


rectangle48 = Rectangle(3, 4)
# print(rectangle48.get_area())

# 49.定义一个shape类，子类square，以长度为参数，这两个类都有area方法


class shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        pass


class square(shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length**2


square49 = square(3)
# print(square49.area())
# 50.引发一次RuntimeError异常


def raise_error():
    raise RuntimeError("This is a runtime error")

# raise_error()

# 51.编写函数计算5/0，用try except来捕获异常


def divide_5_0():
    try:
        print(5/0)
    except ZeroDivisionError:
        print('error')
# divide_5_0()
# 52.定义一个自定义异常类，将字符串消息作为属性


class MyException(Exception):
    def __init__(self, message):
        self.message = message


# 53.输入json@google.com的格式字符串，然后获取用户名


def get_username(json_str):
    pattern = r'(.*?)@'
    match = re.search(pattern, json_str)
    if match:
        return match.group(1)
    else:
        return None


json_str = 'user@google.com'
# print(get_username(json_str))

# 54.输入json@google.com格式字符串，获取公司的名称


def get_company(str):
    pattern = r'@(.*?)\.'
    match = re.search(pattern, str)
    if match:
        return match.group(1)
    else:
        return None

# print(get_company('user@google.com'))

# 55.接受一个单词序列为输入，打印只由数字构成的单词，输入为10 cat5 dog 100


def print_digit_word(words):
    for word in words:
        if word.isdigit():
            print(word)

# print_digit_word(['10','cat5','dog','100'])


# 56.打印unicode字符串‘hello world’
str56 = 'hello world'

# 57.python中的解码和编码
# 编码示例
str57 = '你好，世界'
encoded_str = str57.encode('utf-8')
# print(encoded_str)  # 输出: b'hello world'

# 解码示例
decoded_str = encoded_str.decode('utf-8')
# print(decoded_str)  # 输出: hello world

# 58.编写一个特殊注释表名py文件是unicode格式的
# -*- coding: utf-8 -*-

# 59.计算1/2+2/3+3/4+...   +n/(n+1),函数的输入为n


def sum_of_series(n):
    result = 0
    for i in range(1, n+1):
        result += i/(i+1)
    return result

# print(sum_of_series(5))

# 60.n>0,F(n)=1,F(n)=F(n-1)+100，给定一个n值，计算函数的输出


def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 100
    else:
        return fibonacci(n-1)+100

# print(fibonacci(5))

# 61.输入n，如果n=0，f（n）=0，如果n=1，f（n）=1，如果n>1,f(n)=f(n-1)+f(n-2),编写一个函数


def fibonacci_gen(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_gen(n-1)+fibonacci_gen(n-2)

# print(fibonacci_gen(10))
# 62.用生成器写一个程序，输出0-n之间的偶数


def gen_even(n):
    for i in range(0, n+1, 2):
        yield i


# print(list(gen_even(10)))
for i in gen_even(10):
    pass
    # print(i)
# 63.用生成器写一个程序，输出0-n之间可以被5和7整除的数字


def gen_divisible_by_5_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# print(list(gen_divisible_by_5_7(150)))

# 64.用assert验证列表中[2,4,6,8]都是偶数


def test_is_even(lst):
    for num in lst:
        assert num % 2 == 0


list64_0 = [2, 4, 6, 8]
list64_1 = [2, 3, 4, 5]
list_64 = []
list_64.append(list64_0)
list_64.append(list64_1)
list_ok = []
list_error = []
for i in list_64:
    try:
        test_is_even(i)
        list_ok.append(i)
    except AssertionError:
        list_error.append(i)
# print(list_ok)
# print(list_error)

# test_is_even(list64_1)

# 65.输入字符串25+36*2，输出运算结果

# 66.生成一个1-100之间的随机数


def get_random_num():
    return random.randint(1, 100)


list66 = []
for i in range(10):
    list66.append(get_random_num())
# print(list66)

# 67.用math模块生成一个0-100之间的随机浮点数
def get_random_float():
    return random.uniform(0,100)

#print(get_random_float())
# 68.编写一个程序输出0-10之间的随机偶数
def get_random_even():
    return random.choice([2, 4, 6, 8, 10])
#print(get_random_even())

# 69.输出一个随机数，要求可以被5和7整除，在0-1000之间
def get_ran_5_7():
    return random.choice([i for i in range(0, 1001) if i % 5 == 0 and i % 7 == 0])
#print(get_ran_5_7())

#70.生成一个随机数列表，包含五个100-200之间的随机数
def get_random_list():
    return [random.randint(100, 200) for i in range(5)]
#print(get_random_list())

# 71.生成一个列表，包含100-200之间的5个随机偶数
def get_random_even_list():
    return [random.choice([i for i in range(100, 201) if i % 2 == 0]) for i in range(5)]
#print(get_random_even_list())

# 72.生成一个列表，包含0-1000之间的5个随机整数，要求能被5和7整除
def get_random_5_7_list():
    return [random.choice([i for i in range(0, 1001) if i % 5 == 0 and i % 7 == 0]) for i in range(5)]
#print(get_random_5_7_list())

#73.打印一个随机数，随机数在7-15之间
def get_random_num_7_15():
    return random.randint(7, 15)
#print(get_random_num_7_15())

#74.压缩和解压缩字符串'hello world!hello world!hello world!hello world!hello world!hello world!'
str74 = 'hello world!hello world!hello world!hello world!hello world!hello world!'

# 压缩  
import zlib
compressed_str = zlib.compress(str74.encode('utf-8'))
#print(compressed_str[:10])
#print(compressed_str)
# 解压缩
decompressed_str = zlib.decompress(compressed_str).decode('utf-8')
# 打印
#print(decompressed_str)

# 75.获取一个函数的运行时间，比如打印100次helloworld的运行时间
import time

def print_hello_world():
    for i in range(100):
        print('hello world')
start_time = time.time()
#print(start_time)
#print_hello_world()
end_time = time.time()
#print('运行时间:', end_time - start_time)

#76.编写一个程序洗牌和打印列表[3,6,7,8]
list76 = [3, 6, 7, 8]
import random
random.shuffle(list76)
#print(list76)

# 77.编写一个程序，生成主语在['i','you']，动词在['play','love']，对象在['hockey','football']中的所有句子。
list77_0 = ['i', 'you']
list77_1 = ['play', 'love']
list77_2 = ['hockey', 'football']
for i in list77_0:
    for j in list77_1:
        for k in list77_2:
            pass
            #print(i, j, k)

# 78.给定一个列表，将列表中的偶数删除，列表是[5,7,77,45,22,12,15]
list78_0 = [5, 7, 77, 45, 22, 12, 15]
def remove_even(lst):
    return [i for i in lst if i % 2 != 0]
#print(remove_even(list78_0))

# 79.给定一个列表，删除列表中可以被5和7整除的数，列表是[12,24,35,70,88,120,155]
list79_0 = [12, 24, 35, 70, 88, 120, 155]
def remove_5_7(lst):
    return [i for i in lst if i % 5 != 0 or i % 7 != 0]
#print(remove_5_7(list79_0))

# 80.去掉列表中索引为偶数的元素，列表是[1,2,3,4,5,6,7,8,9,10,11]
list80_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def remove_even_index(lst):
    return [i for j, i in enumerate(lst) if j % 2 != 0]
#print(remove_even_index(list80_0))
#print(enumerate(list80_0))

# 81.生成一个3*5*8三维数组，每个元素为0
import numpy as np
# 生成一个3x5x8的三维数组，每个元素为0
array_3d = np.zeros((3, 5, 8))
#print(array_3d)
# 82.给定一个列表[1,2,3,4,6,7,8,9],去掉列表索引为0,4,5的元素
list82_0 = [1, 2, 3, 4, 6, 7, 8, 9]
def remove_index_0_4_5(lst):
    result = []
    for i, num in enumerate(lst):
        if i != 0 and i != 4 and i != 5:
            result.append(num)
    return result
#print(remove_index_0_4_5(list82_0))
# 83.给定一个列表，[1,2,3,3,4,5,6],删除列表中的3
list83_0 = [1, 2, 3, 3, 4, 5, 6]
def remove_3(lst):
    return [i for i in lst if i != 3]    
#print(remove_3(list83_0))

#84.两个表格为[1,2,3,4,5]和[3,4,5,6,7]，编写程序获得两个列表的交集，输出为新列表
list84_0 = [1, 2, 3, 4, 5]
list84_1 = [3, 4, 5, 6, 7]
def get_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
#print(get_intersection(list84_0, list84_1))
def get_intersection_2(lst1, lst2):
    result=[]
    for i in lst1:
        if i in lst2:
            result.append(i)
    return result
#print(get_intersection_2(list84_0, list84_1))

#85.给定一个列表[1,5,2,3,4,5,6,6,6,6,7],删除重复的值，按照原顺序输出新表
list85_0 = [1, 5, 2, 3, 4, 5, 6, 6, 6, 6, 7]
def remove_duplicate(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
#print(remove_duplicate(list85_0))

# 86.定义person类，两个子类male和female，所有的类都有方法，getgender，male类结果是male，而female的结果是female
class Person: 
    gender='unknown'
    def getgender(self):
        pass

class Male(Person):
    gender='male'
    def __init__(self,gender):
        self.gender=gender
    def getgender(self):
        return self.gender

john = Male('female')
#print(john.getgender())
john.gender='changing'
#print(john.getgender())

# 87.给定字符串abcddddcbd，计算各个字母的数量，输出为字典
str87_0 = 'abcddddcbd'
def count_letters(str):
    result = {}
    for i in str:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
#print(count_letters(str87_0))

#88.给定一个字符串比如one two three，按相反的顺序获得一个新字符串
str88_0 = 'one two three'
def reverse_string(str):
    return ' '.join(str.split(' ')[::-1])
#print(reverse_string(str88_0))

# 88.给定两个列表，['liu','hong','jie'][1,2,3]将他们对齐，输出成一个字典
list88_0 = ['liu', 'hong', 'jie']
list88_1 = [1, 2, 3]
def align_lists(lst1, lst2):
    result = {}
    for i, j in zip(lst1, lst2):
        result[i] = j
    return result
#print(align_lists(list88_0, list88_1))

#89.接受一个字符串，将他以相反的顺序获得一个新字符串，str=one two three
str89_0 = 'one two three'
def reverse_string_2(str):
    return str[::-1]
#print(reverse_string_2(str89_0))

# 90.接受一个字符串，str=one two three，获取偶数索引的元素，生成一个新字符串
str90_0 = 'one two three'

def get_even_index_str(s):
    result = ''
    for i, char in enumerate(s):
        if i % 2 == 0:
            result += char
    return result
#print(str90_0[0], str90_0[2], str90_0[4], str90_0[6], str90_0[8], str90_0[10], str90_0[12])
#print(get_even_index_str(str90_0))

# 91.打印列表[1,2,3]的所有排列组合
list91_0 = [1, 2,3]
def get_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in get_permutations(rest):
            result.append([lst[i]] + p)
            #print(result)
    return result
#print(get_permutations(list91_0))
#print(list91_0[:0],list91_0[1:],list91_0[:1],list91_0[2:])
#get_permutations(list91_0)

# 92.鸡兔同笼问题，一共35个头，和94条腿，求一共有多少兔子和鸡
def get_num_of_rabbits_and_chickens(num_of_heads, num_of_legs):
    for i in range(num_of_heads+1):
        for j in range(num_of_heads+1-i):
            if 2*i+4*j == num_of_legs and i+j==num_of_heads:
                return (i, j)
#print(get_num_of_rabbits_and_chickens(35, 94))
#print(23*2+4*12)

#93.给定一个字符，用他构造一个底边长为5个字符，高为3个字符的等腰三角形
def print_isosceles_triangle(char):
    for i in range(3):
        for j in range(5):
            if i == 1 and j == 2:
                print(' ', end='')
            else:
                print(' ', end='')
        print(char)
#print_isosceles_triangle('*')

#94.给定一个字符串Hello_world_yoyo。将他转化成[Hello,world,yoyo]
str94_0 = 'Hello_world_yoyo'
def str_to_list(s):
    return s.split('_')
#print(str_to_list(str94_0))

#95.打印一个99乘法表
def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1,i+1):
            print(f'{i}*{j}={i*j}', end='\t')
        print()
#print_multiplication_table()

# 96.统计字符串hello，world，yoyo中字母l出现的次数
def count_letter_l(str):
    count=0
    for i in str:
        if i == 'i':
            count+=1
    return count
#print(count_letter_l('hello world yoyo'))

#98.将列表[1,-1,3,4,5,-6]都改成绝对值
def get_absolute_list(lst):
    return [abs(i) for i in lst]
#print(get_absolute_list([1,-1,3,4,5,-6]))

#100.给定一个字符串，one two three 将空格替换成_
str100_0 = 'one two three'
def replace_space_with_underscore(s):
    return s.replace(' ', '_')
#print(replace_space_with_underscore(str100_0))