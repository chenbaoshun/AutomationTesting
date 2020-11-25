#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : pop_windows.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 10:19
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os

driver = webdriver.Chrome()

# 打开本地文件
path = os.getcwd() + '\\alert.html'

# 打开网页
driver.get(path)

# 关于等待
# ①sleep：死等-阻塞代码执行若干秒
# ②implicatitly_wait：隐式等待
# from selenium.webdriver.support.wait import WebDriverWait
# driver.implicitly_wait(10)
# 2-1 隐式等待对浏览器对象生效
# 2-2 元素会持续查找，直到设置的时间到达
# 2-3 一旦超出设置的时间，会抛出异常
# ③显式等待：针对一个元素
element = WebDriverWait(driver, 30, 0.5).until(lambda e:e.find_element_by_xpath('//*[@value="alert弹出框"]'))
# 3-1 显式等待，最终返回一个“元素对象”
# 3-2 需要设置等待的“浏览器对象”，时间上限，查找元素的间隔时间
# 3-3 可以等待元素的“出现”或“消失”
# 3-4 until/not until的参数，要求是一个函数
element.click()
sleep(2)

# # 点击元素，触发alert弹窗
# driver.find_element_by_xpath('//*[@value="alert弹出框"]').click()
# sleep(5)
#
# # 点击当前alert弹窗的“同意”按钮
# driver.switch_to.alert.accept()
#
# # 点击元素，触发alert弹窗
# driver.find_element_by_xpath('//*[@value="confirm确认框"]').click()
# sleep(5)
#
# # 点击当前alert弹窗的“同意”按钮
# driver.switch_to.alert.accept()
#
# # 点击元素，触发alert弹窗
# driver.find_element_by_xpath('//*[@value="confirm确认框"]').click()
# sleep(5)
#
# # 点击当前alert弹窗的“取消”按钮
# driver.switch_to.alert.dismiss()
#
# # 点击元素，触发alert弹窗
# driver.find_element_by_xpath('//*[@value="prompt"]').click()
# sleep(5)
#
# # 点击当前alert弹窗的“同意”按钮
# driver.switch_to.alert.send_keys('123456')
# sleep(3)
# driver.switch_to.alert.accept()