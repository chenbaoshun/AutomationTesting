#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : baidu.py
# @Author  : CHIN
# @Time    : 2020-12-27 12:27

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver1 = webdriver.Chrome()
driver1.maximize_window()
driver1.implicitly_wait(30)
driver1.get('http://www.baidu.com/')

element = driver1.find_element_by_id('s-usersetting-top')
sleep(3)
ActionChains(driver1).move_to_element(element).perform()
sleep(3)

driver1.find_element_by_class_name('setpref').click()
sleep(2)

# driver1.switch_to_default_content()
# sleep(2)
driver1.find_element_by_xpath('//*[@class="item"]/following-sibling::*[@data-tabid="advanced"]').click()
sleep(2)

# print('alert 弹窗:{0}'.format(driver1.switch_to_alert().text))
# driver1.switch_to_alert().accept()

driver1.close()