#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT04.py
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
import time as t

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

    '''百度首页链接测试'''
    def test_baidu_001(self):
        '''百度首页测试：验证新闻的链接'''
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()

    def test_baidu_002(self):
        '''百度首页测试：验证地图的链接'''
        self.driver.find_element_by_partial_link_text('图').click()
        self.driver.back()

    '''百度首页搜索的测试'''
    def test_baidu_003(self):
        '''百度首页搜的测试：验证搜索'''
        self.driver.find_element_by_id('kw').send_keys('webdriver')
        self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)