#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func06.py
# @Author  : CHIN
# @Time    : 2020-12-21 21:28

'''
内部函数:python内部已经定义的函数
type
len
lambda
map
'''
str1 = 'admin'
print(type(str1))
print(len(str1))

list1 = [44,56,345,1]
print(min(list1))
print(max(list1))
print(sum(list1))
print(divmod(100,3))

per = lambda a,b:a+b
print(per(2,5))

age = 10

if age>5:
	print('true')
else:
	print('false')

print('true') if age>5 else print('false')

login = lambda username,pwd:print('登录成功') if username=='coco' and pwd=='admin' else print('登录失败')
login('coco','admin')

data = lambda **kwargs:dict(sorted(kwargs.items(),key=lambda item:item[0]))
print(data(name='coco',age=18))

# map
list1 = [1,2,3,4,5]
def f():
	list2=[]
	for i in list1:
		i+=100
		list2.append(i)
	print(list2)
f()

def f(a):
	return a+100
print(list(map(f,list1)))

'''
def __init__(self, func, *iterables): # real signature unknown; restored from __doc__
    pass
'''
# 进行列表的过滤 filter
def f():
	list2=[]
	for i in list1:
		if i>1:
			list2.append(i)
	print(list2)
f()
print(list(filter(lambda a:a>1,list1)))