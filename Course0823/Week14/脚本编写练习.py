#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 脚本编写练习.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-06 15:21

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps['platformName'] = 'Android'    # 指定测试平台
caps['deviceName'] = 'Phone'    # 安卓中可以随意填一个，但是必传

# 一般来说，在脚本的启动项中需要指定包名和界面名（启动）

caps['appPackage'] = 'com.ss.android.ugc.aweme'
caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'

caps['noReset'] = "true"

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# 编写动作

def swipe_test(x1=0.6, x2=0.6, y1=0.75, y2=0.1):
    size = driver.get_window_size()
    print(size)
    x1 = x1 * size['width']
    x2 = x2 * size['width']
    y1 = y1 * size['height']
    y2 = y2 * size['height']
    driver.swipe(x1, x)

# driver.quit()

