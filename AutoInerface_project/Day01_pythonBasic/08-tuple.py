#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 08-tuple.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-13 21:41

'''
元组是不可变的，但是元组里面的数据内容是可变的
没有增删改
'''

'''
'count', 'index'
'''

# print(dir(tuple))

tuple1 = (1,5,6,['yunya','18'],{'name':'coco','age':18})

tuple1[3][0]='admin'
tuple1[4]['name']='雲涯'
print(tuple1)