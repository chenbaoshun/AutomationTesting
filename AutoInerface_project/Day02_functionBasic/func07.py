#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func07.py
# @Author  : CHIN
# @Time    : 2020-12-21 23:10

'''
装饰器：
1.函数可以当做一个变量
2.函数的参数也可以是参数
3.函数是可以嵌套的
'''

def f():
	print('hello')

per = f()
per

def f2(a):
	return a
f2(f())

def login(username='coco',pwd='admin'):
	if username=='coco' and pwd=='admin':
		return 'asdfghjkl'
	else:
		return '账号登录失败'
def profile(token):
	if token=='asdfghjkl':
		return '欢迎来到扣扣世界'
	else:
		return '请登录系统'
print(profile(login()))

def f3():
	def f4():
		print('hello coco')
	return f4()
f3()