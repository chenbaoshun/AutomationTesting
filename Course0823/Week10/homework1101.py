#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : homework1101.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-08 09:47
# @Site    : 
# @version : V1.0

# 3. httprunner3.x参数化函数parameterize的文件路径是否可以是变量或带路径的文件地址？
# httprunner3.x:是新重构的版本，

# A：文件路径最好用相对路径。如果使用脚手架生成的文件结构，那么相对路径的起点是脚手架文件夹。

# 4. 先注册后登陆的这种场景，使用httprunner的csv文件参数化时，该如何操作？
# A-1:csv数据文件可以有多份，相应的可以有注册.csv、登录.csv
# A-2:参数化的数据，也可以分次取用
# 引申：这里httprunner里边的参数化