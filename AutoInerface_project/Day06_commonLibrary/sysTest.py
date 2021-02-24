#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : sysTest.py
# @Author  : CHIN
# @Time    : 2020-12-24 15:49

'''
sys库
1.变量
2.常用的方法
3.sys模块
MD5的加密
'''

import sys

# print(dir(sys))
# print(sys.argv)
#
# if sys.argv[1]=='sleep':
# 	print('sleep')
# else:
# 	print('end')

print(sys.version)
print(sys.platform)

for item in sys.path:
	print(item)

'''
1.标准库：C:\Program Files\Python37\lib
2.第三方库：C:\Program Files\Python37\lib\site-packages
3.自定义库：
'''

sys.path.append('')