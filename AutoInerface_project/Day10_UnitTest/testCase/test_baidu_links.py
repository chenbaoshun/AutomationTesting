#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_baidu_links.py
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

    def test_baidu_news(self):
        '''首页：点击新闻是否正常跳转到对应页面'''
        self.driver.find_element_by_link_text('新闻').click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[1])
        self.assertEqual(self.driver.current_url,'http://news.baidu.com/')

    def test_baidu_map(self):
        '''首页：点击新闻是否正常跳转到对应页面'''
        self.driver.find_element_by_link_text('地图').click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[1])
        self.assertEqual(self.driver.current_url, 'https://map.baidu.com/@11585280.82,3555907.48,12z')


if __name__ == '__main__':
    unittest.main(verbosity=2)