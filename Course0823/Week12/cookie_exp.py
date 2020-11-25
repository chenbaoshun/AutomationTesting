#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : cookie_exp.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 12:02
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(1)

# 第二步
driver.add_cookie()

sleep(2)

driver.refresh()