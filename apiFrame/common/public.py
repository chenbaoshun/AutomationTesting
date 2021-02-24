#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : public.py
# @Author  : CHIN
# @Time    : 2021-01-16

import os

# base_dir = os.path.dirname(os.path.dirname(__file__))
# print(os.path.dirname(base_dir, 'data', 'login.yaml'))

def filePath(fileDir, fileName):
    '''
    :param fileDir: 文件目录
    :param fileName: 文件名称
    :return:
    '''
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)), fileDir, fileName
    )

def writeContent(content):
    with open(filePath(fileDir='data',fileName='content'),'w') as f:
        f.write(str(content))

def readContent():
    with open(filePath(fileDir='data',fileName='content'),'r') as f:
        return f.read()

# print(filePath('data', 'login.yaml'))
print(readContent())