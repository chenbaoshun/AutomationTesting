#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_sessions_09.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 22:35
# @Site    : 
# @version : V1.0

'''
Session会话对象
'''

import requests

def login(url):
    s = requests.Session()
    params = {}
    headers = {}
    r = s.get(url=url, params=params, headers=headers)
    return s

def profile():
    r = login().get(
        url='',
        cookies=login()
    )
    print(r.text)

profile()