#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_verify_11.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 23:21
# @Site    : 
# @version : V1.0

'''
https的处理，授权准许
'''

import requests

r = requests.get(
    url='https://127.0.0.1:5000/v1/api/books',
    verify=True
)

print(r.text)