#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_sessions_08.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 22:35
# @Site    : 
# @version : V1.0

'''
1. 发送登录请求
2. 登录成功后，把sessionID的信息返回给客户端
3. 客户端再次发送请求，需要在请求头里面（cookie）带上返回的sessionID
'''

import requests

def login(url):
    params = {}
    headers = {}

def profile():
    r = requests.get(
        url='',
        cookies=login()
    )
    print(r.text)

profile()