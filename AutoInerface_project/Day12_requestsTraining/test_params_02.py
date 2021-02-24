#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_params_02.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 10:56
# @Site    : 
# @version : V1.0

import requests

'''
post请求：
url:http://httpbin.org/post?name=chin&age=18
data={'address':'chengdu'}
请求方法：POST
'''

data = {'address':'chengdu'}
params = {'name':'chin','age':18}
r = requests.post(
    url='http://httpbin.org/post',
    data=data,
    params=params
)