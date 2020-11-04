#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : data.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-11 12:04
# @Site    : 
# @version : V1.0

import yaml

with open('./data.yml',encoding='utf-8') as file:
    d = yaml.safe_load(file)

print(d['str'])
print(d['str2'])
print(d['int'])
print(d['float'])
print(d['bool'])
# print(data['None'])
# print(data['time'])
# print(data['date'])
# print('*'*30)
# # 列表
# print(data['list'])
# print('*'*30)
# # 字典
# print(data['dict'])
# print('*'*30)
# # 嵌套
# var = data['list2']
# print(var)
# print(type(var))
# print(type(var[2]))
# print('*'*30)
# var = data['dict2']
# print(var)
# print(type(var))
# print(type(var['小李']))