#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 认识变量.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-23 0023 12:31
# @Site    : 
# @version : V1.0

# num1 = 100
# num2 = 87
# result = num1 + num2
# #result = 100 + 87
# print(result)

# python里的变量的定义/声明，就是一个赋值的过程。在python里“=”是赋值符号

# r = ''  #如果想要空值，依然是给它赋值

# 变量命名
# 变量名，可以包括数字、字母、_(下划线)
# 变量不能用数字开头
# 变量名不能和python关键字重合
import keyword
print(keyword.kwlist)

# 命名习惯的目的：容易理解
# 命名冲突的问题：大小驼峰、下划线
# 大驼峰：UserName
# 小驼峰：userName
# 下划线(环蛇）：user_name

# var = 100
# print(type(var))
# print() 把字符展示到控制台的“方法”
# type() 把变量类型进行“输出”

# var = True
# print(type(var))
#
# print("字符")  #蓝色的标注：可执行的方法
# """
# 方法的后边，需要跟一个()。
# ①如果括号里是空的，
# 就说它不需要参数
# ②如果括号里有任何东西，
# 这个方法是需要参数的
# """
#
# age = 25
# name = 'bull'
# weight = 63.5

# print 格式化处理
# 1. 使用“%”
# print("我的名字叫%s",name)
# 2.使用{}.format
# print("我的名字叫{}".format(name))
# print("我的名字叫{},年龄是{}".format(name,age))
# 3.f'' *python3.6之后的版本可以使用
# print(f'我的名字是{name}')
# print(f'当前代码运行到{}')

# 转义字符
# print('第一行内容',end='\n')
# print('第二行内容')
# 小结：print方法就是用例输出内容到调试区

# 输入
# 将数据输入给程序
# 最基础的输入方法：
# input()
# input 方法，会等待键盘输入和回车键。然后将键盘输入的字符储存起来

# text = input('请输入字符：') #先接收键盘输入，把键盘输入的字符存储到变量text里
# num = int(input('请输入数字：'))
# print('输入的字符类型为：',type(text),type(num))
# print('从键盘获取到的字符是：{}'.format(text))  #使用print格式化输出，展示text变量的值
# print('获取到的数字是：{}'.format(num))

# num1 = '100'
# num2 = '87'
# result = int(num1) - int(num2)
#
# print(result)
