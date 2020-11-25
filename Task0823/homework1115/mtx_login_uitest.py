#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mtx_login_uitest.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-16 22:38
# @Site    : 
# @version : V1.0

from selenium import webdriver
import time

# 实例化
driver = webdriver.Chrome()
mtx_url = "http://121.42.15.146:9090/mtx/"

accounts = 'chin_mtx'
pwd = '123456'

# 打开浏览器
driver.get(mtx_url)
driver.maximize_window()
time.sleep(5)

# 第1种：商品轮播区右侧登录
login_button = driver.find_element_by_xpath("//div[@class='member-login']//a[1]")
login_button.is_enabled()
login_button.click()
time.sleep(3)

text_accounts_input = driver.find_element_by_name('accounts')
text_accounts_input.send_keys(accounts)
time.sleep(3)
text_pwd_input = driver.find_element_by_name('pwd')
text_pwd_input.send_keys(pwd)
time.sleep(3)

login_submit_button = driver.find_element_by_xpath("//div[@class='user-form-container']/descendant::div[3]/button")
login_submit_button.is_enabled()
login_submit_button.click()
time.sleep(3)

# 判断登录用户名
xpath = "//*[text()='chin_mtx']"
element = driver.find_element_by_xpath(xpath)

# 退出登录，换第2种登录
logout_button = driver.find_element_by_xpath("//div[@class='m-baseinfo']/descendant::a[text()='退出']")
logout_button.is_enabled()
logout_button.click()
time.sleep(10)

# 第2种：顶部导航栏左上角登录
login_button = driver.find_element_by_xpath("//div[@class='header-top']/descendant::a[text()='登录']")
login_button.click()
time.sleep(5)

text_accounts_input = driver.find_element_by_name('accounts')
text_accounts_input.send_keys(accounts)
time.sleep(3)
text_pwd_input = driver.find_element_by_name('pwd')
text_pwd_input.send_keys(pwd)
time.sleep(3)

login_submit_button = driver.find_element_by_xpath("//div[@class='user-form-container']/descendant::div[3]/button")
login_submit_button.is_enabled()
login_submit_button.click()
time.sleep(3)

# 判断登录用户名
xpath = "//div[@class='header-top']/descendant::em[text()='chin_mtx，欢迎来到']"
element = driver.find_element_by_xpath(xpath)
time.sleep(3)

# 退出登录
logout_button = driver.find_element_by_xpath("//div[@class='header-top']/descendant::a[text()='退出']")
logout_button.is_enabled()
logout_button.click()
time.sleep(5)

# 关闭浏览器
driver.quit()