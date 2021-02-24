#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : cases.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-09 21:12

import unittest
from selenium import webdriver

from POM20201209.page_object.login_page import LoginPage
from ddt import ddt, file_data

# 测试用例集管理
@ddt()
class Cases(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data("../data/user_data.yml")

    # 测试用例，实现登录+添加购物车流程
    def test_01(self):
        driver = webdriver.Chrome()
        user = ""
        pwd = ""

        # 登录操作


if __name__ == '__main__':
    unittest.main()