#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : pop_windows.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 10:19
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver
import os

driver = webdriver.Chrome()

# 打开本地文件
path = os.getcwd() + '\\alert.html'

# 打开网页
driver.get(path)

# 点击元素，触发alert弹窗
driver.find_element_by_xpath('//*[@value="alert弹出框"]').click()
sleep(5)

# 点击当前alert弹窗的“同意”按钮
driver.switch_to.alert.accept()

# 点击元素，触发alert弹窗
driver.find_element_by_xpath('//*[@value="confirm确认框"]').click()
sleep(5)

# 点击当前alert弹窗的“同意”按钮
driver.switch_to.alert.accept()

# 点击元素，触发alert弹窗
driver.find_element_by_xpath('//*[@value="confirm确认框"]').click()
sleep(5)

# 点击当前alert弹窗的“取消”按钮
driver.switch_to.alert.dismiss()

# 点击元素，触发alert弹窗
driver.find_element_by_xpath('//*[@value="prompt"]').click()
sleep(5)

# 点击当前alert弹窗的“同意”按钮
driver.switch_to.alert.send_keys('123456')
sleep(3)
driver.switch_to.alert.accept()