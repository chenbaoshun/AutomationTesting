#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mixh5_test.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-13 16:36

from appium import webdriver
from time import sleep

caps = {}
caps['platformName'] = 'Android'    # 指定测试平台
caps['deviceName'] = 'Phone'    # 安卓中可以随意填一个，但是必传

# 一般来说，在脚本的启动项中需要指定包名和界面名（启动）

caps['appPackage'] = 'com.testfan.ask'
caps['appActivity'] = 'com.testfan.ask.MainActivity'

caps['noReset'] = False
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
caps['skipDeviceInitialization'] = False
caps['skipServerInstallation'] = False
caps['adbPort'] = '5037'
caps['uuid'] = '127.0.0.1:62001'

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# 进入APP后，有一个5s的广告
driver.implicitly_wait(10)

print('当前上下文', driver.contexts)
print('当前操作的上下文', driver.current_context)
driver.switch_to.context('WEBVIEW_com.testfan.ask')
driver.find_element_by_xpath("//*[text()='立即注册']").click()

sleep(3)

driver.quit()