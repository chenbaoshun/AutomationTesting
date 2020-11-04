#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : create_case.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-11 16:13
# @Site    : 
# @version : V1.0

from allpairspy import AllPairs

# 需要一个列表入参
# 列表里的每一个子元素，就表示一个参数
# 每一个子元素，用列表的形式描述所有可能的取值

data = [
    ['IE','chrome','360安全浏览器'],
    ['windows','android','mac'],
    ['登录模块测试集','支付模块测试集','内容模块测试集']
]