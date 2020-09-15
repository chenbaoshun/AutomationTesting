#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : testscript_addstudents.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 00:20
# @Site    : 
# @version : V1.0

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import csv

driver = webdriver.Chrome()

url = "http://boweifeng.xueqingyun.com/schadmin/user/add-stu"
driver.get(url)

driver.find_element_by_id('loginform-identity').send_keys('xzmadmin')
driver.find_element_by_id('loginform-password').send_keys('51testing')
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

time.sleep(2)

driver.find_element_by_id('studentform-username').send_keys('student1')
driver.find_element_by_id('studentform-fullname').send_keys('studentname')
driver.find_element_by_id('studentform-gender')
Select(sex).select_by_index(2)
driver.find_element_by_id('studentform-password').send_keys('111111')
