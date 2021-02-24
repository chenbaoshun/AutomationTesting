#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func02.py
# @Author  : CHIN
# @Time    : 2020-12-21 14:21

'''
需求：
1.对请求参数进行ASCII排序
2.排序后，对请求参数进行MD5的加密

    1.写一个函数，获取请求参数，对请求参数进行加密
'''

# DDT data
def f1(*args,**kwargs):     # *args:元组，**kwargs:字典
    print(args,kwargs)

f1([1,2,3])
f1('a')
f1(name='coco')
f1(dict1={'name':'coco'})

'''
应用场景：
1.请求参数不确定
2.请求数据类型不确定
'''

# dict1 = {'name':'coco','age':18,'datas':{'name':'coco','age':18}}

def data(**kwargs):
    return dict(sorted(kwargs.items(),key=lambda item:item[0]))
dict1 = {'name':'coco','age':18,'address':'chengdu','work':'tester'}
print(data(**dict1))