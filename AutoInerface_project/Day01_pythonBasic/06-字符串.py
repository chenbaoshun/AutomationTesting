#!/usr/bin/python3  
# -*- coding: utf-8 -*-

# @File    : 06-字符串.py
# @Author  : CHIN
# @Time    : 2020-12-20 00:11

str1 = 'admin'
# print(dir(str1))

# str2 = str1.replace('ad', 'baidu')
# print(str2)

# print(str1.find('m'))

# print(str1.startswith('a'))     # 判断字符串以某字符开头
# print(str1.endswith('n'))       # 判断字符串以某字段结尾

print(str1.upper())

str1 = 'ADMIN'
print(str1.lower())

str1 = '19'
print(str1.isdigit())

str1 = '你好,天空'
print(str1.split(','))
print(','.join(str1.split(',')))

# 字符串的格式化
name = 'yunya'
age = 18

print('我的名字是%s,我今年%s岁'%(name,age))      # %针对的是字符串和整数类型
print('我的名字是%s,我今年%d岁'%(name,age))      # 建议统一使用%s,兼容所有
print('我的名字是{0},我今年{1}岁'.format(name,age))
print('我的名字是{name},我今年{age}岁'.format(name=name,age=age))