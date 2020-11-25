#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : selector_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 11:20
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/selectTest.htm")

# select = driver.find_element_by_xpath('//*[@id="s1Id"]')
# Select(select).select_by_index(1)
# sleep(5)
#
# Select(select).select_by_visible_text('o2')
# sleep(5)
#
# Select(select).select_by_value('o3')

# select = driver.find_element_by_xpath('//*[@id="s4Id"]/option[5]')

for i in range(4):
