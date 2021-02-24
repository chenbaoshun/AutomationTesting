#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : fs_case.py
# @Author  : CHIN
# @Time    : 2020-12-22 22:28

url = input('请输入路由地址:\n')

target_models,target_function = url.split('/')
m = __import__(target_models)
if hasattr(m,target_function):
	target_function = getattr(m,target_function)
	target_function()
else:
	print('Not Found 404 Page')