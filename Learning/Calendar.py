#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Calendar.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-24 22:30
# @Site    : 
# @version : V1.0

'''
计算闰年 平年
'''
# 被4整除  不能被100整除 或者400整除 闰年
# 余数--
# //取整  %取余

# print(11 % 3)

# year = int(input("输入年份："))
#
# if year%4 == 0 and year%100 != 0 or year%400 == 0:
#     print('闰年')
# else:
#     print('平年')

def is_leap_year(year):

    return year%4 == 0 and year%100 != 0 or year%400 == 0

def get_num_month(year,month):

    if month in(1,3,5,7,8,10,12):
        return 31
    elif month in(4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    return 28

# print(get_num_month(2020,2))