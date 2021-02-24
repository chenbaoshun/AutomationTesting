#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : touch_action.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-13 10:23

from appium.webdriver.common.touch_action import TouchAction

TouchAction().press(x=120, y=650).wait(10).move_to(x=360, y=410).release().perform()