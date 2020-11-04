#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : add_dele.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-23 22:40
# @Site    : 
# @version : V1.0

from test import Test
import unittest

class Test_test(unittest.TestCase):
    #下面三引号对类的注释会显示在报告的表格中
    '''数字计算'''
    def test_shuzi(self):

       #下面三引号对方法的注释会显示在报告的表格中
       '''两个数字相加以及两个数字相减'''
        # 对test文件中的Test类初始化
       shuzi = Test(7, 3)
       self.assertEqual(shuzi.add(),10)
       self.assertEqual(shuzi.dele(),4)
    def test_liangmethod(self):

       '''两数字相加的2倍 加上 两个数字相减的2倍'''
       #对test文件中的Test类初始化
       liangshuzi = Test(6, 5)
       t = liangshuzi.add()*2 + liangshuzi.dele()*2
       self.assertEqual(t,24)