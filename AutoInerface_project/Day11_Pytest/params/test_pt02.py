#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_pt01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 21:39
# @Site    : 
# @version : V1.0

import pytest
import unittest

def test_001():
    assert 1==1

class TestLogin(object):
    def test_login(self):
        assert 1==1

class LoginTest(unittest.TestCase):
    def test_login_01(self):
        assert 1==1

    def test_login_02(self):
        pass

def add():
    assert 1==1