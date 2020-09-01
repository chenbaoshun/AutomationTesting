#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 练习.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 14:27
# @Site    : 
# @version : V1.0

name = "hello haha\t world\t hi\tnihao beautiful\t haha\nok"
# print(name.count('\t'))
# print(name.count('\n'))

name1 = name.replace('\t',' ')
# print(name1)
name2 = name1.replace('\n',' ')
# print(name2)

name3 = name2.split()
# del name3[' ']

print(name3)
