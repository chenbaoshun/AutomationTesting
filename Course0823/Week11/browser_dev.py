#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : browser_dev.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 13:38
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

# 实例化“浏览器”对象
dev = webdriver.Chrome()
url = "https://www.baidu.com/"

# 使用get方法打开一个页面
dev.get(url)

size = dev.get_window_size()
print(size)
dev.set_window_size(800,600)
sleep(2)
dev.fullscreen_window()
sleep(2)
dev.quit()