#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : appium连接测试.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-06 15:21

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps['platformName'] = 'Android'    # 指定测试平台
caps['deviceName'] = 'Phone'    # 安卓中可以随意填一个，但是必传

# 一般来说，在脚本的启动项中需要指定

caps['appPackage'] = 'com.youdao.calculator'
caps['appActivity'] = '.activities.MainActivity'

caps['noReset'] = "true"

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.quit()

