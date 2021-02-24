#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_plugin_06.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-07 22:04
# @Site    : 
# @version : V1.0

import pytest

@pytest.mark.dependency()
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    assert True

@pytest.mark.dependency(depends=['test_a'])
def test_c():
    pass

@pytest.mark.dependency(depends=['test_b'])
def test_d():
    pass