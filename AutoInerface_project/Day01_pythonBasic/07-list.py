#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 07-list.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-13 21:35

list1 = [1,99,23,45,100,0,678]

'''
 'append': 追加,
  'clear': 清空, 
  'copy', 
  'count', 
  'extend', 
  'index', 
  'insert', 
  'pop', 
  'remove', 
  'reverse', 
  'sort'
'''

# print(dir(list1))
list1.append(999)       # 追加，默认追加在最后一位
print(list1)

list1.insert(2, 999)
print(list1)

list2 = list1.copy()
print(list2)

print(list1.count(100))     # 统计某元素在列表的个数

print(list1.index(100))     # 列表对应值的索引

list1.remove(100)       # 删除列表中某元素
print(list1)

list1.pop()     # 删除最后一位，并打印出来
print(list1)

list2 = [2,3,4]
list1.extend(list2)     # 将两个列表合并为一个
print(list1)

list1.reverse()     # 反转
print(list1)

list1.sort()        # 从小到大的排序
print(list1)

for i in list1:
    if i>2:
        print(i)

print([x+1 for x in list1])     # 列表推导式

print([x for x in list1 if x>2])