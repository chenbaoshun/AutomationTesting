#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : fileTest.py
# @Author  : CHIN
# @Time    : 2020-12-26 20:13

'''
r - 读
read() -->
'''


'''
a - 追加
'''
# f = open('file.json','a')
# f.write('chin')
# f.close()

'''文件的上下文处理'''
with open('file2','w') as f:
	f.write('chin')

