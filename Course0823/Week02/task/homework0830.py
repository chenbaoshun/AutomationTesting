#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : homework0830.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 09:46
# @Site    : 
# @version : V1.0


# 1.善于百度，查看文档
# 2.容易混淆
#     2.1 同名方法在不同的数据类型：本质是认为编写了两个方法
#         len()
#     2.2 同质方法
#         str(字符串)里index()和find()
# var = 'string'
# print(len(var))
#
# var = ['swd','tib','ring']
# print(len(var))

# 一句话需求：统计一段英文短语的单词出现的次数
'''
编写一段代码
1.接收键盘输入的英文短语
2.使用空格、逗号、句号分割短语中的单词
3.统计短语中每个单词，出现的次数(忽略大小写)
4.将结果存储为“字典”
范例：
输入:hello python.Learning Python
输出：{'hello':1,'python':2,'learning':1}
'''

# 考点：
# 1.基本数据类型的熟悉程度
# 2.流程控制
# 3.程序设计

# 1.接收键盘输入的英文短语
input_str = input("请输入英文短语：")
input_str = str(input_str)

# 2.使用空格、逗号、句号分割短语中的单词
# replace()
input_str = input_str.replace(',',' ')
mark_list = [',','.','，','，','。']   # 需要统一的分隔符列表
for i in mark_list:
    input_str = input_str.replace(i,' ')
print(input_str)

input_str = input_str.lower()   # 处理“忽略大小写”
word_list = input_str.split()   # 利用split()方法进行分割
# 3.统计短语中每个单词，出现的次数(忽略大小写)
dict_word = {}
dict_word['hello'] = word_list.count('hello')
# 把单词的项目 和 词频统计
# 针对单词项目，本质上是一个“去重”操作
# 去重方式1：
# word_keys = set(word_list)
# 去重方式2：
word_keys = []
for i in word_list:
    if i not in word_keys:
        word_keys.append(i)

# word_keys # 是一个去重的keys列表
# 4.将结果存储为“字典”
for i in word_keys:
    dict_word[i] = word_list.count(i)

print(dict_word)