#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT11.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 21:45
# @Site    : 
# @version : V1.0

from Day10_UnitTest.init import *

def add(a,b):
    return a+b

class BaiduLink(Init):
    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    @unittest.skip('忽略该用例执行')
    def test_02(self):
        pass

    @unittest.expectedFailure
    def test_03(self):
        self.assertEqual(add(2,3),4)

    @staticmethod
    def suite(self):
        suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())