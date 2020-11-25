#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : virkeybd_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 11:47
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(3)
input = driver.find_element_by_id('kw')
input.send_keys('selenium')
sleep(2)

input.send_keys(Keys.DOWN)
sleep(1)

input.send_keys(Keys.DOWN)
sleep(1)