#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Dic.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 16:04
# @Site    : 
# @version : V1.0

# 字典
# *本质上是“映射”
# 字典里“：”左边的值是“键”，右边是“值”

# list = ['tom','man',20]
# dic = {'tom':['男',20]}
# print(dic['tom'])
# print(type(dic))

# 基础知识
# 字符串的创建：{}
# 字符串对应的类型是dict
# 字典里的一个元素，必然是“键值对”（键、值使用“：”来分隔）
# 字典里的“键”是字符串类型
# 字典里边的元素，使用“，”来分隔
# *键值对应为，key/value、k/v
# *字符串是可变数据类型

# 字典的增删改查
# 初始化
# dic = {}
dic = {'tom':'21','lily':'23'}

# 增加元素
# *字典是无序
# dic['bull'] = 30
# dic['bull'] = 25
# print(dic)
#
# # 删除元素
# # del dic['bull']
# # print(dic)
#
# # clear() - 归零
# dic.clear()
# print(dic)
# item key value
# print(dic.keys())   #keys方法能够输出字典包含的所有“键”
# print(dic.values()) #values方法能够输出字典包含的所有“值”

# print(dic.items())
# # print(dic['liu'])   #获取不存在的“键”，会抛出“KeyError”异常阻碍程序运行
# print(dic.get('liu'))
# print('next step')

# res = dic.get('liu','没有找到目标值')
# if res

# 字典的遍历
# for key in dic：   #如果不指定，那么遍历字典会去遍历“键”
for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

for item in dic.items():
    print(item)