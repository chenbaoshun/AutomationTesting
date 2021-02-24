#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : osTest.py
# @Author  : CHIN
# @Time    : 2020-12-24 14:49

import os

# print(dir(os))

# print(os.system('ipconfig'))

# # 创建文件夹
# os.mkdir('c:/log')
# os.rmdir('c:/log')
#
# # 对文件或目录进行重命名
# os.rename('c:/log','c:/newlog')

# # 对目录的处理
# print('当前文件的目录：',os.path.dirname(__file__))
# print('当前文件的上一级目录：',os.path.dirname(os.path.dirname(__file__)))
# print('当前文件的上上一级目录：',os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# 需求：实现对Day3目录下的login文件内容的读取
base_dir = os.path.dirname(os.path.dirname(__file__))

f = open(os.path.join(base_dir,'Day03_packageAndmodule/login.py'),'r',encoding='utf-8')
print(f.read())

'''请求参数是不确定的，可能有一个，可能有N个'''