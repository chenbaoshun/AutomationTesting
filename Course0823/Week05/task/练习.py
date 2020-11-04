#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 练习.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-22 22:06
# @Site    : 
# @version : V1.0

import requests
import unittest
import HTMLTestRunner
from urllib3 import encode_multipart_formdata

url = 'http://192.168.31.213/mtx/index.php?s=/index/user/reg.html'
data = {
    "accounts": "chin_mtx",
    "pwd": "123456",
    "type": "username",
    "is_agree_agreement": "1"
}

headers = {
    "Content-Type": "multipart/form-data"
}

encode_data = encode_multipart_formdata(data)
data = encode_data[0]
headers['Content-Type'] = encode_data[1]

reg = requests.post(url=url, headers=headers, data=data)

print(reg.status_code)
print(reg.content.decode('utf-8'))
# print(reg.text)