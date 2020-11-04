#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 装饰器.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-20 10:01
# @Site    : 
# @version : V1.0

# 装饰器本质上也是一个函数
# 1.没有参数的装饰器
# 定义装饰器函数
# def logger(func):       # 在python里，一切都是对象
#     def wrapper(*args,**kwargs):
#         print("进入装饰器函数")
#
#         func(*args,**kwargs)    # 真正的函数在装饰器重新调用
#
#         print("装饰器功能执行完毕")
#
#     return wrapper
#
# @logger     # @的语法会把下一行定义的函数，加到装饰器的入参
# def add(x,y):
#     print("进入被修饰的函数")
#     print(f'{x}+{y}={x+y}')
#
# add(1,2)

# 2.带有参数的装饰器
def say_hello(contry):
    def wrapper(func):
        def second(*args,**kwargs):
            if contry == 'china':
                print("来自装饰器的‘你好’")
            elif contry == 'america':
                print("来自装饰器的‘hello’")
            else:
                return
            func(*args,**kwargs)

        return second
    return wrapper

@say_hello('america')
def america():
    print("I am come from America")

@say_hello('china')
def china():
    print("我来自中国")

america()
print('*'*10)
china()