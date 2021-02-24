#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_demo.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-17 19:44

'''
pytest --
pytest
test_*  *_test.py   模块
    pytest  --写用例 --？ 写用例
class -- TestDemo()
方法 -- def
'''

class TestDemo:
    def test_01(self):
        assert 2==2

def demo():
    print()