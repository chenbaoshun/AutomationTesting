#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 09-dict.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-13 21:45

dict1 = {'name':'abu', 'age':18}
dict2 = {'address':'chengdu', 'sex':'boy'}

'''
'clear'     清空, 
'copy', 
'fromkeys', 
'get', 
'items', 
'keys', 
'pop', 
'popitem', 
'setdefault', 
'update':组合，合并, 
'values'
'''
# 字典是不能排序的，往字典中追加数据时，有先进先出的原则，但并不实用
# 会按照ASCII码排序输出

# print(dir(dict1))

dict3=dict1.copy()
print(dict3)

dict3=dict1.clear()
print(dict3)

print(dict1.get('name'))

for key,value in dict1.items():
    print(key,':',value)

dict1.update(dict2)       # 对字典的整个扩展（同list的extend）
print(dict1)

print(sorted(dict1.items(),key=lambda item:item[0]))

print(dict1.get('age'))