def my_generator():
    for i in range(1, 4):
        yield i

a=1
for num in my_generator():
    a+=num



# gen = my_generator()  # 生成器函数返回生成器对象

# print(next(gen))  # 输出: 1
# print(next(gen))  # 输出: 2
# print(next(gen))  # 输出: 3
