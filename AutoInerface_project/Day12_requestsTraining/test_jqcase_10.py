#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_jqcase_10.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 23:13
# @Site    : 
# @version : V1.0

import requests
from requests.auth import HTTPBasicAuth

r = requests.get(
    url='http://127.0.0.1:5000/v1/api/books',
    auth=HTTPBasicAuth('admin','admin')
)

print(r.text)