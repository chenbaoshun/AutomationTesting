#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 05-控制流和循环.py
# @Author  : CHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-19 22:05

# age = 25
#
# if age>20:
# 	print(True)
# elif age>25:
# 	print('大于25')
# else:
# 	print(False)

# 布尔类型时，无需在条件判断时做条件内容
# a=True
#
# if a:
# 	print('结果正确')
# else:
# 	print('结果错误')

# 循环
# 循环打印出1~9的所有数字
# for i in range(0,10):   # range左闭右开(包含头不包含尾）
# 	print(i)

# while True:
# 	# pass
# 	p = int(input('1、姓名 2、年龄\n'))
# 	if p==1:
# 		name=input('你的名字是什么？\n')
# 	elif p==2:
# 		age=input('你的年龄：\n')
# 	else:
# 		break

age = 19

if age>20:
	print('success')
else:
	print('fail')

print('success') if age>20 else print('fail')

if age>15:print('正确')