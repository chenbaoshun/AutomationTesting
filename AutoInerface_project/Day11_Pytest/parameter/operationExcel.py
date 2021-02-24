#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : operationExcel.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-06 20:54
# @Site    : 
# @version : V1.0

import xlrd

def readExcel():
    data = list()
    book = xlrd.open_workbook('login.xls')
    sheet =