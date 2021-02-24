#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : login_page.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-09 20:56


from POM20201209.base.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    # url
    url = ""

    # 页面元素
    user = (By.NAME, "accounts")
    pwd = (By.NAME, "pwd")

    button = (By.XPATH, "")

    # 元素的操作流
    def login(self):
        self.open(self.url)
        self.input_(self.user)


if __name__ == '__main__':
    driver = webdriver.Chrome()
