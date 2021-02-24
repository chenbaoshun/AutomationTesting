#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : base_page.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-09 20:51

from time import sleep
from selenium import webdriver

class BasePage:
    driver = webdriver.Chrome()

    # 访问 url
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入框
    def input_(self, loc, text):
        self.locator(loc).send_keys(text)

    # 点击
    def button(self):
        self.locator().click()

    # 退出
    def close(self):
        self.driver.quit()