#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : conftest.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 20:40

import sys,os

path = os.path.join(os.path.dirname(__file__), '../')   # 获取当前的绝对路径
sys.path.append(path)   # 把当前路径加入到python-path