#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : cmd_dos.py
# @Author  : CHIN
# @Time    : 2020-12-20 11:39

import os
import multiprocessing

def cmd_server():
    print(os.system('python -V'))

cmd_server()
print('执行测试脚本')

# def main():
#     p = multiprocessing.Process(target=cmd_server)
