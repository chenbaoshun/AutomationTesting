#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_fileud_12.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 23:23
# @Site    : 
# @version : V1.0

import requests

def login():
    s = requests.Session()
    url = ''
    data = {}
    headers = {}

    r = s.post(url=url, data=data, headers=headers)
    # print(r.text)
    return s

def profile():
    r = login().get(url='')
    print(r.text)

def upload():
    url = ''
    data = {}
    headers = {'Content-Type': ''}
    files = {'file': ("logo.png", open('E:/logo.png','rb'), 'imag/jpeg', {})}       # 文件格式参数必须传入，上传是以二进制流的方式读取，下载是以二进制流的方式写入

    r = login().post(url=url, data=data, files=files, headers=headers)

# login()
upload()