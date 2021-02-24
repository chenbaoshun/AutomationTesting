#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT05.py
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

class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')
        # now_handle = cls.driver.current_window_handle
        # cls.driver.switch_to_window(now_handle)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    '''百度首页链接测试'''
    def test_baidu_001(self):
        '''百度首页测试：验证新闻的链接'''
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.forward()

    def test_baidu_002(self):
        '''百度首页测试：验证地图的链接'''
        self.driver.find_element_by_partial_link_text('图').click()
        self.driver.forward()

    '''百度首页搜索的测试'''
    def test_baidu_003(self):
        '''百度首页搜的测试：验证搜索'''
        self.driver.find_element_by_id('kw').send_keys('webdriver')
        self.driver.forward()

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest('test_baidu_001'))
    suite.addTest(BaiduTest('test_baidu_002'))
    suite.addTest(BaiduTest('test_baidu_003'))
    unittest.TextTestRunner(verbosity=2).run(suite)