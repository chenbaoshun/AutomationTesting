#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : init.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 22:23
# @Site    : 
# @version : V1.0

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()