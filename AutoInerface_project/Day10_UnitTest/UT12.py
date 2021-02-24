#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT12.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 21:45
# @Site    : 
# @version : V1.0

from Day10_UnitTest.init import *

class BaiduLink(Init):
    # def test_baidu_news(self):
    #     print(self.driver.title,type(str(self.driver.title).encode('gbk')))
    #     self.assertEqual(str(self.driver.title).encode('gbk'),'百度一下，你就知道')    # 相等必须是类型和内容相等
    #     self.driver.find_element_by_link_text('新闻').click()

    # def test_baidu_search(self):
    #     so = self.driver.find_element_by_id('kw')
    #     self.assertTrue(so.is_enabled())    # 是否可用

    def test_baidu_title(self):
        self.assertIn('百度',self.driver.title)   # 是否包含

if __name__ == '__main__':
    unittest.main(verbosity=2)