#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : 09-dict04.py
# @Author  : CHIN
# @Time    : 2020-12-20 22:51

'''
数据类型的转换
'''

str1 = '9.6'
str_list = str1.split('.')
print(str_list)
list_str = '.'.join(str_list)
print(list_str)

dict1 = {'name':'coco','age':18}
dict_list = dict1.items()
# dict_list = list(dict1.keys())
print(dict_list)
list_dict = dict(enumerate(dict_list))
print(list_dict)