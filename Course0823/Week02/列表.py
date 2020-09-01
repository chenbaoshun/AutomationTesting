#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 列表.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 11:37
# @Site    : 
# @version : V1.0

# 列表是一个有序的序列
# 可变的序列

# test_list = [1,'a',[1,2],{"name":"刘备"},{2,3},(1,2,"李四")]
# # 列表的查找
# print(test_list[2])
# # 统计
# print(test_list.count('a'))
#
# # 计算列表长度
# print(len(test_list))

# 举例：实现一个简单的登录功能
# name_list = ['tom','sad']
# var = input("请输入用户名：")
# if var in name_list:
#     print('用户已存在')

# 增加元素
# # append-在类别末尾增加一个元素
list_1 = []
# list_1.append('str')
# print(list_1)
# # insert-在列表的某一个位置，插入一个元素
# list_1.insert(2,'xu')
# print(list_1)
#
# # extent -  列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一加入列表中
# list_1.extent('xu')
# list_1.extent(['x','u'])

# del - 删除
del list_1
del list_1[0]
# remove - 移除特定值
list_1.remove('x')
# pop - 删除指定下标的数据（默认为最后一个），并返回该数据
list_1.pop(0)
list_1.pop()

# clear - 清空列表
list_1.clear()

# reverse - 逆转
list_1.reverse()

# sort - 排序
list_1.sort()

# copy - 复制
new_list = list_1.copy()

# # 对列表的循环遍历
# # 使用for循环：
# names = ['tom','mike','lily','dany']
# for i in names:
#     print(i)
#
# # 使用while
# n = 0
# while n < len(names):
#     print(names[n])
#     n = n+1
#     print(f'当前是第{n}个循环')

# 列表嵌套
name_list = [['xiaoming'],['xiaoli','xiaohua'],['xiaozhou']]
print(name_list[1][0])

# 在列表里
# num_list = [1,2,3]
# num_list[2] = [3,4,5]

# 元组
t = (1,2,3)
# t[0] = 4 #对其中一个元素进行修改

# 元组只能做查找，提取值