#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_request_01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-08 22:46
# @Site    : 
# @version : V1.0

import requests

r = requests.get(
    url='http://httpbin.org/get',
    params=None
)

print('请求地址：',r.url)
print('响应头：',r.headers)
print('json格式的数据:',r.json())
print('基本文本的数据:',r.text)
print('二进制的内容：',r.content)
print('状态码:',r.status_code)
print('cookies:',r.cookies)