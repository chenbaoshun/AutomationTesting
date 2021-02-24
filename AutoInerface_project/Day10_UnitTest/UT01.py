#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT01.py
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

class F1(unittest.TestCase):
    def setUp(self):
        print('我已经做好准备工作')

    def tearDown(self):
        print('我已经处理完成')

    def test_001(self):
        print('test01')

    def test_002(self):
        print('test02')

    def test_003(self):
        self.assertEqual(1,'1')
        # print('test03')

if __name__ == '__main__':
    unittest.main(verbosity=2)