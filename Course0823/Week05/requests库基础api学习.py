#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : requests库基础api学习.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-20 15:40
# @Site    : 
# @version : V1.0

import requests
# https://requests.readthedocs.io/zh_CN/latest/

# 发送get请求
# requests.get(url,params=None,**kwargs)

ip = 'http://192.168.31.213:8080'
path1 = '/pinter/com/getSku'
url1 = ip + path1
# data = {
#     'id':'1'
# }

print(url1)

g = requests.get(url=url1)
print(type(g))
print(g.text)
print(type(g.text))
print(g.json())
print(type(g.json()))
print(g.json())
# 由文档可知，对于get函数只有“url”是必传参数

# post请求
path2 = '/pinter/com/login'
url2 = ip + path2
data = {
    'userName':'admin',
    'password':'1234'
}

print(url2)

p = requests.post(url=url2,data=data)
print(p.json())