#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 函数.py
# @Author  : CHIN
# @Time    : 2020-9-4
# @version : V1.0

# 函数示例
# def select_option():
#     print('----请选择功能----')
#     print('查询余额')
#     print('取款')
#     print('存款')
#     print('----退出功能----')
#
# print('密码正确，登录成功')
# select_option()
# print('查询余额完毕')
# select_option()
# print('取款成功')
# select_option()

# 1.调用函数
# print('参数1')

# 2.定义函数
# def关键字 + 空格 + 函数名称 + () + 冒号(:) # 可以填写参数要求
#     写函数内容的时候，换行、缩进
# func1
# func2
# def func1(var): #定义函数
#     print(f'一个简单的函数，接收了参数{var}')
#
# # 函数运行的时机是进行“调用”
# # 调用函数：写函数名+(),如果有参数要求，需要写参数，没有参数，但格式须保持
# var = "字符串变量"
# func1(var)
#
# var = '    '
# func1(var)

# 3.参数、函数
# def func2(): #定义函数
#     print('一个简单的函数，不需要参数')
# func2()
# def add_sum1():
#     res = 1 + 2
#     print('调用到了给函数')
#     # return res  #如果说函数包装了一个计算过程，那么这个计算一定有“结果”。这个结果就可以用return关键字来实现
# # 方式1：
# print(add_sum1())   # *一个不充电，函数的参数也可以是另一个函数（函数的嵌套）
# 方式2：
# var = add_sum1()
# print(var)

# def add_sum():
#     result = 1+2
#     print(result)
#
# add_sum()
#
# def add_sum3(a,b):  # 定义函数的时候，写的对参数的要求也叫“形式参数（形参）”
#     result1 = a+b
#     return result1
#
# # res = add_sum3(100,30)
# # print(res)
# res = add_sum3('10',1)
# print()
# def add_sum4(a,b,c):  # 定义函数的时候，写的对参数的要求也叫“形式参数（形参）”
#     res = 0
#     a = int(a)
#     b = int(b)
#     if c == "进行计算":
#         res = a + b
#     return '计算结果',res
#
# # res = add_sum3(100,30)
# # print(res)
# res = add_sum4('10',1,'进行计算')
# print(res)

# 返回值，return
# def buy():
#     return ('口罩')
# goods = buy()
# print(goods)

# 函数说明文档
# def calc(a,b):
#     '''
#     求和计算器
#     :param a:加法计算的第一个“数值”，需是int格式
#     :param b:加法计算的第二个“数值”，需是int格式
#     :return: a+b的结果
#     '''
#     return a+b
# result = calc(4,8)
# print(result)
# help(calc)

# 定义函数时的嵌套
# *函数可以用到任何地方，可以是普通的代码段，其他函数的参数位置、其他函数的内容
# *对于使用函数，需要遵循
# def testB():
#     print('‐‐‐‐‐testB‐‐‐‐‐start')
#     print('testB执行的代码')
#     print('‐‐‐‐‐testB‐‐‐‐‐end')
# def testA():
#     print('‐‐‐‐‐testA‐‐‐‐‐‐start')
#     testB()
#     print('‐‐‐‐‐testA‐‐‐‐‐‐end')
# testA()

# def print_one_line():
#     print('-'*10)
#
# # print_one_line()
#
# def many_lines(n):
#     i = 1
#     while i <= n:
#         print_one_line()
#         i += 1
#
# many_lines(2)

# def sum3(a,b,c):
#     result = a+b+c
#     return result
#
# # result = sum3(2,4,6)
# # print(result)
#
# def ave3(x,y,z):
#     result = sum3(x,y,z)
#     mean = result/3
#     return mean
#
# result = ave3(4,7,8)
# print(result)

# def chengfa(a,b,c):
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     result = a*b*c
#     return result
#
# result = chengfa(2,'4',6)
# print(result)

# 函数、变量的作用域
# def testA():
#     a = 100 # 函数内部的变量
#     print(a)
#     print('方法调用成功')
#
# testA()
# print(a)    #函数内部的变量，不能在函数外部直接调用

# a = 100
# def testA():
#     print(a)
# def testB():
#     print(a)
#
# testA()
# testB()
# 代码可以读到 同级别 或者 更大级别的变量
# 相对不能读到 更小级别 的变量
# 也不能先读取，后定义
# def func_testC():
#     var = 'TEST C 的变量'
#     def sub1():
#         print(var)
#         var1 = '子方法的变量'
#     sub1()
#     # print(var1)     #这里会报错，因为变量的作用域不同
# func_testC()
# a = 100
# def testA():
#     print(a)
# def testB():
#     a = 200
#     print(a)
#
# testA()
# testB()
# print(f'全局变量是{a}')

# a = 100
# def testA():
#     print(a)
# def testB():    # global 关键字，声明a是全局变量
#     global a
#     a = 200
#     print(a)
#
# testA()
# testB()
# print(f'全局变量是{a}')

# # 1.共用全局变量
# glo_num = 10
# # 修改全局变量
# def test1():
#     global glo_num
#     glo_num = 200
# def test2():
#     print(glo_num)
#
# # 调用test1函数修改全局变量
# test1()
# # 调用test2函数打印全局变量
# test2()

# # 2.返回值作为参数传递
# def test1():
#     return 50
# def test2(num):
#     print(num)
#
# # 调用test1函数把返回值保存到一个变量中
# result = test1()
# # 把保存test1函数返回结果的变量传给test2作为参数
# test2(result)

# # 函数的返回值
# def test1():
#     return 1
#     return 2
#
# #调用test1()
# result = test1()
# print(result)
#
# def test1():
#     return 1,2
#
# #调用test1()
# result = test1()
# print(result)

# 针对函数的参数
# # 1.位置参数：python解析参数的方式1-按照参数顺序
def user_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
#
# user_info('bull',20,'男')
#
# # 2.关键字参数：指定“形参”名
# def user_info(name,age,gender):
#     print(f'您的名字是{name},年龄是{age},性别是{gender}')
#
# user_info('bull',age=20,gender='男') #位置参数要放在关键字参数的后面，关键字参数不要求顺序，无所谓
# user_info('bull',gender='男',age=20)

# 3.缺省参数：在定义函数时，可以定义带“默认值”的参数
# 定义函数的时候，带默认值的参数要写在“普通形参”的后边
# def user_info(name,age,gender='男'):
#     print(f'您的名字是{name},年龄是{age},性别是{gender}')
#
# # 调用函数，使用默认参数，不传gender
# user_info('bull',18)
# # 调用函数，更改默认的参数值
# user_info('tom',age=23,gender='男')
# # 调用函数，关键字参数不区分顺序，只要在位置参数后面就可以
# user_info('jack',gender='男',age=25)

# 4.不定长参数
# def user_info(*args):
#     print(args)
#
# user_info('TOM')
# user_info()
# user_info('tom',90)

# def user_info(**kwargs):
#     print(kwargs)
#
# # 返回的结果是{'name': 'tom', 'age': 10, 'gender': '男'}
# user_info(name='tom', age=10, gender='男')