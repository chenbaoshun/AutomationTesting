#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : testscript_addteachers.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 00:21
# @Site    : 
# @version : V1.0

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import csv

driver = webdriver.Chrome()
url = "http://boweifeng.xueqingyun.com/schadmin/user/add-thr"
driver.get(url)

driver.find_element_by_id('loginform-identity').send_keys('xzmadmin')
driver.find_element_by_id('loginform-password').send_keys('51testing')
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

time.sleep(2)

file = open('教师信息测试数据文件.csv','r')
rows = csv.reader(file)
for row in rows:
    TeacherId = row[0]
    TeacherName = row[1]

    driver.find_element_by_id('teacherform-username').send_keys(TeacherId)
    driver.find_element_by_id('teacherform-fullname').send_keys(TeacherName)
    sex = driver.find_element_by_id('teacherform-gender')
    Select(sex).select_by_index(2)
    driver.find_element_by_id('teacherform-password').send_keys('111111')
    driver.find_element_by_id('grp_sel_cmn-tree-input').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="grp_sel_cmn-tree"]/ul/li/div/div[2]/span[3]').click()
    driver.find_element_by_id('sel_role_id').click()
    time.sleep(3)
    role = driver.find_element_by_name('TeacherForm[role_id]')
    Select(role).select_by_value('733632240457777360')
    time.sleep(2)
    driver.find_element_by_id('teacherform-start_date').send_keys('2019-9-5')
    driver.find_element_by_id('teacherform-end_date').send_keys('2020-9-5')
    time.sleep(1)
    driver.find_element_by_class_name('btn-primary').click()

    time.sleep(1)


driver.close()