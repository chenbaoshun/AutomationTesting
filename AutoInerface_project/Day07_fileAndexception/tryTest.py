#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : tryTest.py
# @Author  : CHIN
# @Time    : 2020-12-25 21:57

def div(a,b):
	return a/b
try:
	div(1,99.9)
except Exception as e:
	print(e.args)