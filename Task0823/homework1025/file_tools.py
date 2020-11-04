#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : file_tools.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-10-26 23:39
# @Site    : 
# @version : V1.0

import csv

path = 'userData.csv'

def write_user_csv(username, password):
    with open(path, 'a+', newline='', encoding='utf-8') as file:
        write_user_csv = csv.writer(file)
        data_row = [username, password]
        return write_user_csv.writerow(data_row)

def read_user_csv(username, password):
    with open(path, 'r') as file:
        read_user_csv = csv.reader(file)
        for data_row in read_user_csv:
            print(data_row)
            if username in data_row and password in data_row:
                return True
            else:
                return False


def read_username(name):
    with open(path, 'r', encoding='utf-8') as file:
        read = csv.reader(file)
        names = [row[0] for row in read]
        print(names)
        if name in names:
            return False
        else:
            return True


def create_user_csv():
    return None