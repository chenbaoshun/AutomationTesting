#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-23 22:39
# @Site    : 
# @version : V1.0

class Test():
     #初始化函数
     def __init__(self,a,b):
         self.a = a
         self.b = b

     #两个数相加
     def add(self):
         x = self.a+self.b
         return x

     #两个数相减
     def dele(self):
         y = self.a-self.b
         return y