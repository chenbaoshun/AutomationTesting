#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_fixture_01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-06 21:02
# @Site    : 
# @version : V1.0

import pytest

@pytest.fixture()
def data():
    return 'hello'

def test_data(data):
    assert data=='hello'

if __name__ == '__main__':
    pytest.main(["-v","-s","test_fixture_01.py"])