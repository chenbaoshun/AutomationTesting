#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 函数.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 17:01
# @Site    : 
# @version : V1.0

# ①使用方法的第一种方式
# import winsound
# winsound.MessageBeep()

# ②对遍历进行计算、逻辑、输出操作
# print("字符串")    #方法名称()

# 方法的定义：def 关键字，防范后边需要处理参数，参数可有可无，但格式必须有 - ()
def func1():
    res = 10+5
    print(res)
    return res  #return关键字后边描述的是这个方法的“值”（返回值）
# 方法被调用的时候执行
func1()

def func2(num1,num2):
    tol = num1+num2
    print(tol)
    return tol
# 方法被调用的时候执行
func2(9,8)

'''
本日复盘：
了解基本数据类型
字符串的各种方法
    基于“序列”这种数据结构
列表的各种操作
元组和列表的异同
字典数据类型（映射结构）
定义方法
'''