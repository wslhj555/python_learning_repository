# 我的类和函数
import re
import calendar
import datetime
import random


class Matrix_transfer:
    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_transposition(self):
        '''这个函数用于将矩阵进行转置'''
        return [[row[i] for row in self.matrix]for i in range(len(self.matrix[0]))]


def max_common_divi(a, b):
    """找到两个数之间的最大公约数"""
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


'''
print(max_common_divi(10,25))
print(max_common_divi(5,10))
print(max_common_divi(2,3))'''


def f1(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)


def min_common_multiple(a, b):
    """找到两个数的最小公倍数"""
    for i in range(max(a, b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i


def min_common_multiple_0(a, b):
    """找到两个数的最小公倍数"""
    return a*b//max_common_divi(a, b)


'''
print(min_common_multiple(5,7))
print(min_common_multiple(15,125))
print(min_common_multiple(125,346))
'''

# print(max_common_divi(1000,1005))
'''
def add(a,b):
    return a+b

num_1=input('第一个数')
num_2=input('第二个数')
print(add(int(num_1),int(num_2)))
'''


def calcul_num(str_0):
    """计算字符串的运算结果"""
    str_0 = str_0.replace(' ', '')
    match = re.match(r"^(\d+\.?\d*)([-+*/])(\d+\.?\d*)$", str_0)
    try:
        if match:
            num_1, func, num_2 = match.groups()
            print(num_1, func, num_2)
            if func == "+":
                return float(num_1)+float(num_2)
            elif func == "-":
                return float(num_1)-float(num_2)
            elif func == "*":
                return float(num_1)*float(num_2)
            else:
                try:
                    return float(num_1)/float(num_2)
                except:
                    return "除数不能为0"
        else:
            return "输入格式错误"
    except:
        return "输入格式错误"


def feibo_n(n):
    """斐波那契数列"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return feibo_n(n-1)+feibo_n(n-2)


def feibo_list(n):
    """斐波那契数列"""
    fib_list = []
    for i in range(1, n+1):
        fib_list.append(feibo_n(i))
    return fib_list


'''
print(feibo_list(10))
print(feibo_list(20))
'''


def get_day_before(n):
    """获取n天前的日期"""
    now_date = datetime.datetime.now()
    interval_days = datetime.timedelta(days=n)
    day_before_date = now_date-interval_days
    return day_before_date.strftime('%Y-%m-%d')

# print(get_day_before(40))


def delete_num(sum, gap, rest):
    '''一共有sum个数字，报数1-gap，报数为gap的数字删掉，然后循环，直到剩余rest个数字'''
    # i是总数的循环，j是报数的循环
    dict_0 = {}
    i = 1
    while i <= sum:
        j = 1
        while j <= gap:
            dict_0[i] = [j]
            i += 1
            j += 1
            pass


def del_num_list(sum, gap, rest):
    '''一共有sum个数字，报数1-gap，报数为gap的数字删掉，然后循环，直到剩余rest个数字'''
    list_0 = [1 for i in range(1, sum+1)]
    list_1 = []  # 记录删掉数字的编号，即i+1
    i = 0  # i是列表的下标
    count = 1
    while i < sum:
        i += 1
        count += 1
        if i == sum:
            i = 0
        while list_0[i] == 0:
            i += 1
            if i == sum:
                i = 0
        while count == gap:
            if list_0[i] != 0:
                list_0[i] = 0
                count = 0
                list_1.append(i+1)
            else:
                i += 1
                continue
        if list_0.count(1) == rest:
            break
    return list_1


def total_fish():
    '''计算鱼的总数'''
    total = 0
    while True:
        total += 1
        fish_num = total
        enough = 1
        for _ in range(1, 6):
            if fish_num % 5 == 1:
                fish_num = (fish_num-1)//5*4
            else:
                enough = 0
                break
        if enough == 1:
            return total


def reverse_array_new(arr, d):
    for _ in range(0, d+1):
        arr.append(arr.pop(0))
    return arr


def serch_element(list_0, element, start, end):
    if start > end:
        return -1
    mid = int((start+end)/2)
    if list_0[mid] == element:
        return mid
    elif list_0[mid] > element:
        return serch_element(list_0, element, start, mid-1)
    else:
        return serch_element(list_0, element, mid+1, end)


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


# list_1 = [3, 1, 1, 1, 5, 9, 2, 6, 5, 5, 5]
# print(sort_list(list_1))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]
# print(sort_list(arr))

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# print(quicksort([3, 6, 8, 19, 1, 5]))  # [1，3, 5, 6, 8, 19]

def select_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# print(select_sort([3, 6, 8, 19, 1, 5]))


def countSort(arr):

    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


def xier_sort(arr):
    n = len(arr)
    mid = n//2
    while mid > 0:
        for i in range(mid, n):
            j = i
            while j >= mid and arr[j-mid] > arr[j]:
                arr[j-mid], arr[j] = arr[j], arr[j-mid]
                j -= mid
        mid //= 2
    return arr


def process_data(data):
    # 在这里进行数据处理，这里只是简单地将字符串转换为大写
    return data.upper()


def data_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # 去除换行符并返回每一行数据


def data_generator_url(file_path):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    with open(file_path, 'r') as file:
        for line in file:
            urls = re.findall(url_pattern, line)
            for url in urls:
                yield url


def save_processed_data(generator, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for data in generator:
            processed_data = process_data(data)
            output_file.write(processed_data + '\n')  # 将处理后的数据写入文件


'''
input_file_path = 'input_data.txt'  # 输入文件路径
output_file_path = 'output_data.txt'  # 输出文件路径

# 生成器循环处理数据并保存
data_gen = data_generator(input_file_path)
save_processed_data(data_gen, output_file_path)'''


def multiply_generator(j):
    i = 1
    while i <= j:
        yield f'{i}x{j}={i*j}'
        i += 1


def feibo(n):
    a, b = 0, 1
    list_0 = []
    if n == 1:
        list_0.append(0)
    while n > 1:
        a, b = b, a+b
        n -= 1
        list_0.append(a)
    return list_0


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def data_generator(file_path):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    with open(file_path, 'r') as f:
        for line in f:
            # urls = re.findall(url_pattern, line)
            return line


# for i in data_generator('./test_file/read_write.txt'):
    # print(i)

def read_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            urls = re.findall(r'https?://\S+?(?=,|$)', line)
            if urls:
                for url in urls:
                    yield url
            else:
                continue


'''file_path_0 = './test_file/read_write.txt'
for i in read_file(file_path_0):
    print(i)'''

# 分鱼问题


def calcu_sum(n):
    fish = 1
    per_num = n
    while True:
        sum = fish
        n = per_num
        while n > 0:
            if (sum-1) % per_num == 0:
                print(sum-1, per_num)
                sum = (sum-1)/per_num*(per_num-1)
                n -= 1
            else:
                break
        if n == 0 and sum != 0:
            return fish
        fish += 1

# print(calcu_sum(5))

# 分鱼问题


def calcu_sum_0(n):
    fish = 1
    while True:
        end = 1
        total = fish
        for _ in range(1, n+1):
            if (total-1) % n == 0 and total != 1:
                total = (total-1)//n*(n-1)
            else:
                end = 0
                break
        if end:
            return fish
        fish += 1

'''
print(calcu_sum_0(1))
print(calcu_sum_0(2))
print(calcu_sum_0(3))
print(calcu_sum_0(4))
print(calcu_sum_0(5))
'''


def list_remove(sum, gap, rest):
    list_0 = [i for i in range(1, sum+1)]
    list_1 = []
    while True:
        list_0 = list_0[gap-1:]+list_0[:gap-1]
        remove = list_0.pop(0)
        list_1.append(remove)
        if len(list_0) == rest:
            break
    return list_1


def my_function(*args):
    print(args)


