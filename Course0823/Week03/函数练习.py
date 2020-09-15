#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 函数练习.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 13:34
# @Site    : 
# @version : V1.0

# 需求：
# 工作之中，会需要注册大量的账户（需要注册信息：姓名、身份证、地址）。这时候编辑和记录名字就成为一个问题。
# 这里编写一个随机生成姓名函数

# 需求分析：
# 1.编写一个函数，命名为“get_random_name”
# 2.针对“大量”：函数需要具有批量的功能，所在在“get_random_name”基础上拓展编写“get_random_names”批量生成的函数
# 3.对于需求，生成什么样的姓名（需先搞清楚）：生成中文姓名

# 具体设计
# 1.利用python的random库，来实现“随机”的功能
# 2.对于姓名，一般分成“姓氏”和“名字”
# 3.随机姓名=随机姓氏+随机名字（随机的量=姓氏*名字）

# 编码
import random
# v = random.randint(1,5)
# print(v)

# def get_random_name():
#     first_name = ["赵","钱","孙","李","周","冯","陈","左丘","西门","南宫"]
#     last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
#     range_f_name = len(first_name)-1
#     range_l_name = len(last_name)-1
#
#     fname = random.randint(0,range_f_name)
#     lname = random.randint(0,range_l_name)
#
#     res = first_name[fname] + last_name[lname]
#
#     return res
#
# name = get_random_name()
# print(name)

# 练习1：
# 用random.choice(seq)来替换randint,优化上述代码

# random.choice(seq)
# 从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError。

# v = [1,2,3,4,5,'df']
#
# ran = random.choice(v)
#
# print(ran)

def get_random_name():
    first_name = ["赵","钱","孙","李","周","冯","陈","左丘","西门","南宫"]
    last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
    # range_f_name = len(first_name)-1
    # range_l_name = len(last_name)-1

    fname = random.choice(first_name)
    lname = random.choice(last_name)

    res = fname + lname

    return res

def get_random_names(num):
    name_list = []
    for i in range(num):
        name = get_random_name()
        name_list.append(name)
        print(name_list)
    return name_list

get_random_names(9)
# print(names)

# 练习2：
# 利用get_random_name()方法，
# 扩展编写get_random_names()#批量生成随机姓名函数
