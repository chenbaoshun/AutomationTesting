#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : selenium_test.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 11:40
# @Site    : 
# @version : V1.0

from selenium import webdriver

# 方案1：
# dev = webdriver.Chrome()
# url = "https://www.baidu.com/"
# dev.get(url)

# 方案2：指定driver路径来实例化一个driver对象
url = 'https://www.baidu.com/'
path = 'C:\\Program Files\\Python37\\chromedriver.exe'
dev = webdriver.Chrome(executable_path=path)
dev.get(url)