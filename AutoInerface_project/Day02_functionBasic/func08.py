#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func08.py
# @Author  : CHIN
# @Time    : 2020-12-21 23:27

'''
装饰器案例
封闭原则：已实现的功能代码尽可能不要做修改
开放原则：对现有的功能代码可扩展
需求：在调用f1或f2函数时，先打印“书籍名”，再打印“课堂名”
'''

def getInfo(func):
	def inner():
		print('《Python自动化测试实战》')
		func()      # 相当于执行被装饰的函数f1
	return inner

@getInfo        # 装饰器：被装饰的函数实际上是函数的参数，即f1是getInfo函数的参数
# 先执行装饰器函数，再执行被装饰的函数
def f1():
	# print('《Python自动化测试实战》')
	# getInfo()
	print('网易云课堂')

@getInfo
def f2():
	# print('《Python自动化测试实战》')
	# getInfo()
	print('51CTO课堂')

f1()

'''
装饰器执行步骤：
1.执行getInfo函数时，把被装饰的函数f1当作参数来传递
2.getInfo函数的返回值会重新赋值
3.一旦结合装饰器后，调用f1函数其实执行的是inner函数的内部，原来的函数f1被覆盖
4.被装饰的函数f1重新赋值给装饰器的内层函数inner
'''

def login(username='coco',pwd='admin'):
	if username=='coco' and pwd=='admin':
		return 'asdfghjkl'
	else:
		return '账号登录失败'

def login(func):
	def inner(token='asdfghjkl456'):
		if token=='asdfghjkl456':
			return func(token)
		else:
			return '请重新登录系统'
	return inner

@login
def profile(token):
	return '欢迎来到coco空间'

# print(profile('asdfghjkl456'))
# 函数参数不确定时，使用动态参数
def outer(func):
	def inner(*args,**kwargs):
		print(args,kwargs)
		func()
	return inner