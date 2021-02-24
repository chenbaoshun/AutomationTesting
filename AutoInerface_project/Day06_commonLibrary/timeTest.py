#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : timeTest.py
# @Author  : CHIN
# @Time    : 2020-12-24 14:40

import time as t

# print(dir(t))

# 获取时间戳
print(int(t.time()))

# 获取当前时间
print(t.localtime(t.time()))
print(t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))
nowTime = t.strftime('%y-%m-%d %H:%M:%S',t.localtime())
print(type(nowTime))
# print(t.mktime())

t.sleep(2)