#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : md5_tools.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-10-27 21:28
# @Site    : 
# @version : V1.0

import base64
import hashlib

class Encrypt():
    def __init__(self, string):
        self._string = string.encode('utf-8')   # 内部变量

    def md5(self):
        # 封装MD5加密
        try:
            md5_string = hashlib.md5(self._string)
            return md5_string.hexdigest()
        except:
            return '字符串加密失败'

    def base64encode(self):
        try:
            return base64.b64encode(self._string).decode('utf-8')
        except:
            return 'base64加密失败'

    def base64decode(self):
        try:
            return base64.b64decode(self._string).decode('utf-8')
        except:
            return 'base64解密失败'