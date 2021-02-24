#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : func.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 21:41

'''
1.函数的定义：
函数是一段可以重复调用的代码，通过输入的参数值，返回需要的结果。
2.函数的本质：
把函数块的代码起个别名，供以后来进行调用
3.函数作用域的注意事项：

'''

def add(a,b,c,d):
    print(a+b+c+d)

add(2,3,4,1)
add(a=1,b=2,c=3,d=4)

# 文件的路径以及具体的文件，模式，编码，换行
open('log.txt')

'''
默认参数：
1.有默认参数的放在没有默认参数的后面，否则会报错
2.在执行时，一定记得参数传值，关键参数对应值要一一对应
'''
def add01(a=2,b=3):
    print(a+b)

add01()

def add02(a,b=3):
    print(a+b)

add02(3,4)

def login(username='admin',password='admin'):
    pass

# data的目录下（.txt,.csv,.xml,.config）
def data_dir(filePath='d:/data',filename=None):
    # pass
    print(filePath)
    print(filename)
# data_dir('test.txt')
data_dir(filename='test.txt')

def f():
    print('Hello World')

def f1(a):
    return a

f1(f())

def f(a, b):
    print()

def f(a, b=None):
    print()

'''
函数的3种类型：
1.def f():
    print('Hello World')
    
2.def f(a, b):
    print()
    
3.def f(a, b=None):
    print()
'''

def getFile(director='d:/', filename=None):
    pass
getFile(filename='.csv')



