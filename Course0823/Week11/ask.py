#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : ask.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 16:39
# @Site    : 
# @version : V1.0

# 联系ask社区qq关联登录

from time import sleep
from selenium import webdriver

# 实例化driver
driver = webdriver.Chrome()
url = "http://ask.testfan.cn/"

# 打开网页
driver.get(url)

# 点击登录按钮
element = driver.find_element_by_link_text('登录')
element.click()

# 点击QQ图标
element = driver.find_element_by_class_name('icon-sn-bg-qq')
element.click()
sleep(5)

# 点击关联的QQ头像
# 这里QQ头像图标在一个iframe标签里。
# iframe是一个特殊的标签，查找其下辖的元素时需要进行一个切换操作
driver.switch_to.frame('ptlogin_iframe')

element = driver.find_element_by_xpath('//*[@id="img_out_2213183307"]')
element.click()
sleep(5)

# input_email = driver.find_element_by_name('email')
# input_email.send_keys('baoshunchin@qq.com')
# sleep(3)
#
# submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/button')
# submit_button.click()
# sleep(3)


# 检查登录标签，显示预期用户名
