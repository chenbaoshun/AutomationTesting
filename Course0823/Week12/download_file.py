#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : download_file.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 13:45
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/saveAs.htm")
sleep(2)
