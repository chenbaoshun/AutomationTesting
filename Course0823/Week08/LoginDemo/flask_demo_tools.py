#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : flask_demo_tools.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-25 16:24
# @Site    : 
# @version : V1.0

import csv

def reg_write_csv(name, password):
    path = 'data.csv'
    with open(path, 'a+', newline='', encoding='utf-8') as file:
        reg_write_csv = csv.writer(file)
        data_row = [name, password]
        reg_write_csv.writerow(data_row)

def login_read_csv(name, password):
    path = 'data.csv'
    with open(path, 'r', encoding='utf-8') as file:
        login_read_csv = csv.reader(file)
        for data_row in login_read_csv:
            print(data_row)
            if name in data_row and password in data_row:
                return True
            return False