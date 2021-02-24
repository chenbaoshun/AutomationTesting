#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : fs.py
# @Author  : CHIN
# @Time    : 2020-12-22 21:43

'''
getattr():根据字符串的形式去某个模块中寻找某个对象（函数）
hasattr():根据字符串的形式去某个模块中判断某个对象（函数）是否存在
setattr():根据字符串的形式去某个模块中设置某个对象（函数）
delattr():根据字符串的形式去某个模块中删除某个对象（函数）
'''

# 通过__import__导入目标模块并且放在一个对象中
f = __import__('login')

# 通过对象找login模块中的index的字符串并调用
f.index()

import login

# 调用login模块中的logout函数
f = getattr(login,'logout')
f()

# 如何找到Person中的info方法并且调用
obj = login.Person()
func = 'info'
if hasattr(obj,func):
	f = getattr(obj,func)
	f()
else:
	print('sorry')

obj = login.Person()
f = setattr(obj,'exit','this is a exit method')
f2 = hasattr(obj,'exit')
print('setattr后的结果',f2)
f3 = delattr(obj,'exit')
f4 = hasattr(obj,'exit')
print('delattr后的结果',f4)

# 需求：在login模块中设置变量str2
f = setattr(login,'str2','hello chengdu')
f2 = hasattr(login,'str2')
print(f2)
f3 = getattr(login,'str2')
print(f3)
f4 = delattr(login,'str2')
f5 = hasattr(login,'str2')
print(f5)