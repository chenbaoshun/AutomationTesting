#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_baidu_so.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 23:41
# @Site    : 
# @version : V1.0

from selenium import webdriver
import unittest

class BaiduLink(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_so_enabled(self):
        '''首页：百度搜索输入框可编辑'''
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_baidu_so(self):
        '''首页：测试百度的搜索功能'''
        so = self.driver.find_element_by_id('kw')
        so.send_keys('webdriver')
        self.driver.find_element_by_id('su').click()
        self.assertEqual(so.get_attribute('value'),'webdriver')

if __name__ == '__main__':
    unittest.main(verbosity=2)