#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : readfile.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 23:07
# @Site    : 
# @version : V1.0

import csv

file = open('教师信息测试数据文件.csv','r')
rows = csv.reader(file)
for row in rows:
    print(row[0],row[1])