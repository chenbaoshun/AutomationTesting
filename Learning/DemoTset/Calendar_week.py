#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Calendar_week.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-24 22:47
# @Site    : 
# @version : V1.0

from DemoTset import Calendar

year = int(input("输入年份："))
month = int(input("输入月份："))
days = Calendar.get_num_month(year, month)

# age = 18
# name = "Tony"
#
# print("名字是%s"%name,"年龄是%s"%age)

print(days)