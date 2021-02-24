#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : second.py
# @Author  : CHIN
# @Time    : 2020-12-22 16:15

import first

print(first.index2)
print(first.index())

per = first.Index
per.hello()

# from 模块 import 类，函数，变量
# from first import Index,index,index2
from first import *

per = Index()
per.hello()
index()
index2