#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_jsons_04.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 11:02
# @Site    : 
# @version : V1.0

import requests
import json

'''
application/x-www-form-urlencoded  -->  data json!=
application/json  -->  json格式的字符串数据类型  -->  字符串
data
json
1.满足的要求：application/json
2.请求参数必须是dict（但条件2须在条件1下）
'''

'''查询电话归属地'''
data = {'mobileCode':'13018204373','userID':''}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(
    url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
    headers=headers,
    json=data
)

print(r.text)