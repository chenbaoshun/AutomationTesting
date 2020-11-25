#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : cookie_login.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-24 22:28

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://121.42.15.146:9090/mtx/")
sleep(1)

# 第二步
driver.add_cookie({'name':'PHPSESSID', 'value':'pgafnfj1vnq4qbe9b1jfulsf03'})

sleep(2)

driver.refresh()