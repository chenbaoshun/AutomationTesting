#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT02.py
# @Author  : Baoshun.Chin
# @Time    : 2020-12-31 22:07
# @Site    : 
# @version : V1.0

'''
unittest
pytest
mock
'''

import unittest
from selenium import webdriver

class F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_news_01(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_baidu_map_02(self):
        self.driver.find_element_by_partial_link_text('图').click()

if __name__ == '__main__':
    unittest.main(verbosity=2)