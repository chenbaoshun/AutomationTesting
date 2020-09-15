#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 20200823_3周_陈宝顺.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-09-06 22:39
# @version : V1.0

'''
一、作业：
1.对批量生成随机姓名函数，进行优化。要求写入文件的数据没有重复项
'''
# 具体分析：
# 1-随机生成姓名
# 2-批量生成姓名
# 3-检查去重
# 4-文件操作（打开、写入、关闭）

import random

def get_random_name():
    first_name = ["赵","钱","孙","李","周","冯","陈","左丘","西门","南宫"]
    last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]

    fname = random.choice(first_name)
    lname = random.choice(last_name)

    res = fname + lname
    return res

def get_random_names(num):
    name_list = []
    for i in range(num):
        name = get_random_name()
        name_list.append(name)

    return name_list

def write_data_t():     # 写入数据方法
    name_list = get_random_names(10)
    removename_list = []  # 设置一个空列表存储去重后的姓名
    fp = open('name_data.txt', 'a')
    for i in name_list:  # 先把随机生成的姓名列表进行去重
        if i not in removename_list:  # 如果名字不在新列表中，则添加到新列表里
            removename_list.append(i)

    for i in removename_list:
        fp.write(i)
        fp.write('\n')
    fp.close()

if __name__ == "__main__":      # 主函数进行调用
    write_data_t()

'''
2.按照面向对象的思想，尝试设计一个随机生成地址的“类”（进行语言描述即可，不用具体编码）
类：地址
-省
-市
-区
-街道
-小区
-单元楼房
实例：家庭地址-四川省成都市武侯区石羊街道新园社区1单元1楼101室
-省：四川省
-市：成都市
-区：武侯区
-街道：石羊街道
-小区：新园社区
-单元楼房：1单元1楼101室
'''
