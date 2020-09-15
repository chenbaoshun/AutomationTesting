#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 异常处理.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 15:11
# @Site    : 
# @version : V1.0

try:
    f = open('test.tt','r')
    res_list = f.readlines()
    # print(res_list)
except Exception as e:
    print(f'错误信息{e}')
    print('文件读取失败，需进行相应的处理')
finally:
    f.close()

print(res_list)
