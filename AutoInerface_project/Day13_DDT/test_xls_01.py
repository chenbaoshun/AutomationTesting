#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_xls_01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-10 23:33
# @Site    : 
# @version : V1.0

import xlrd
import os

def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)

work = xlrd.open_workbook(base_dir("data.xls"))
sheet = work.sheet_by_index(0)
# 查看文件有多少行(有内容)
print(sheet.nrows)
# 获取单元格的内容
print(sheet.cell_value[11][1])