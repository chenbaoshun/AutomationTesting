#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : md5.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-25 12:46
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

if __name__ == '__main__':
    string = '待加密的字符串'
    e = Encrypt(string) # 实例化
    print(e.md5())
    ex = e.base64encode()
    print(ex)

    el = Encrypt(ex)
    print(el.base64decode())

    # # 假设需要加密一个token
    # key = 'key343579759'
    # # 用户唯一标识，一般是userID，或者手机号、身份证号这样的唯一
    # userid = '6654'
    # # 加入一个时间戳，跟服务器时间做比较。若相差大于“过期时间”，则该数据报错“超时（过期）”
    # time = '202010252108'
    # # 拼接token字符串
    # token = key + time + userid
    # print(token)
    # e = Encrypt(token)
    # token_md5 = e.md5()
    # print(token_md5)