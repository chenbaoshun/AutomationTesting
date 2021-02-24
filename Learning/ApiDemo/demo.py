#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : demo.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 21:06

url = "http://apis.juhe.cn/xzpd/query?key=7179e359dfaddcb027681295e7a33eb9&men=%E9%87%91%E7%89%9B&women=%E7%99%BD%E7%BE%8A"
# 解码工具 代码
import urllib.parse,requests
print(urllib.parse.unquote(url))
# 脚本 -- 接口