#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 文件处理.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 14:42
# @Site    : 
# @version : V1.0

import random

# open('data.txt','r')

# f = open('test.txt','w')
# print(f'f变量的数据类型是{type(f)}')
#
# f.write('赵钱孙李周冯陈左丘西门南宫')
#
# f.close()
import os

# filename = 'data/data.txt'
# #
# # f = open(filename,'r')
# with open(filename,'r') as f:
#     res = f.readline()
#
#     print(res)
with open(r'.\data\data.txt','w',encoding='utf-8') as f:
    f.write('abcdefghijklmnopqrstuvwxyz')

# f = open('names.txt','w')
# def get_random_name():
#     first_name = ["赵","钱","孙","李","周","冯","陈","左丘","西门","南宫"]
#     last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
#     # range_f_name = len(first_name)-1
#     # range_l_name = len(last_name)-1
#
#     fname = random.choice(first_name)
#     lname = random.choice(last_name)
#
#     res = fname + lname
#
#     return res
#
# def get_random_names(num):
#     name_list = []
#     for i in range(num):
#         name = get_random_name()
#         name_list.append(name)
#         print(name_list)
#     return name_list
#
# names = get_random_names(9)
# f.write(names)
# f.close()