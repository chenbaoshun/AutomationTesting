#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : cutscreen_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 11:34
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver
import os
import time, random

driver = webdriver.Chrome()

# 打开本地文件\
t = int(time.time())
name = str(t) + '_' + str(random.randint(0,100))
path = os.getcwd() + f'\\截图\\{name}.png'
print(path)

# 打开网页
driver.get("https://www.baidu.com")
sleep(3)

# 全屏截图
# driver.get_screenshot_as_file(path)
# sleep(3)

# 元素截图
driver.find_element_by_xpath('').screenshot(path)
sleep(3)

driver.quit()