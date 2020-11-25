#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : element_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 14:40
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)

# 定位一个元素
# 第一优先级：id-如果一个元素有id属性，那么应该用id去定位
# text_input = driver.find_element_by_id('kw')
# text_input.send_keys('hello selenium')
# sleep(5)
#
# submit_button = driver.find_element_by_id('su')
# submit_button.click()

# 对于a标签
# news = driver.find_element_by_link_text('新闻')
# sleep(3)
# news.click()

# 复合型CSS