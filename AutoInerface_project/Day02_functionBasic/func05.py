#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func05.py
# @Author  : CHIN
# @Time    : 2020-12-21 20:31

'''
作用域
全局作用域：全局变量
局部作用域：针对局部
从上到下，优先在自己作用域
'''

name = '雲涯'

# def f():
# 	print(name)
# f()

def f():
	global name
	name = '雲涯微课堂'
	print(name)

f()

def f():
	name='我是父函数的值'
	def f1():
		name='我是子函数的值'
		print(name)
	return f1()
f()
