#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mtx_register.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-23 22:30

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


reg_url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/reginfo.html'
driver = webdriver.Chrome()
driver.get(reg_url)

name_input_xpath =  '//*[@placeholder="请使用字母、数字、下划线 2~18 个字符"]'
name_input = driver.find_element_by_xpath(name_input_xpath)

pwd_input_xpath =  '//*[@placeholder="请使用字母、数字、下划线 2~18 个字符"]/parent::*/following-sibling::*//input[@name="pwd"]'
pwd_input = driver.find_element_by_xpath(pwd_input_xpath)

agreement_choice_xpath = '//input[@data-validation-message="请同意注册协议"]/following-sibling::span/i[@class="am-icon-checked"]'
choice_button = driver.find_elements_by_xpath(agreement_choice_xpath)[0]

reg_button_xpath = '//button[text()="注册"]'
reg_button = driver.find_elements_by_xpath(reg_button_xpath)[0]

assert_reg = "//*[text()='test_yoyo，欢迎来到']"

sleep(2)
name_input.send_keys('test_yoyo')
sleep(2)
pwd_input.send_keys('test_yoyo')
sleep(2)
choice_button.click()
sleep(2)
reg_button.click()

element = WebDriverWait(driver, 30, 0.5).until(lambda e:e.find_element_by_xpath(assert_reg))
