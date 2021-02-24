#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT09.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 21:45
# @Site    : 
# @version : V1.0

import unittest
from selenium import webdriver

class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test02(self):
        pass

    @staticmethod
    def suite(self):
        suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())