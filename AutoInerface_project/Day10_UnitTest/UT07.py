#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : UT07.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-02 21:45
# @Site    : 
# @version : V1.0

import unittest

class F7(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        pass

    def test02(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(F7))
    unittest.TextTestRunner(verbosity=2).run(suite)