#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_param_one.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-04 21:01
# @Site    : 
# @version : V1.0

import pytest

def add(a,b):
    return a+b

@pytest.mark.parametrize('a,b,expect',[
    pytest.param(1,1,2,id='one plus'),
    pytest.param(2,2,4,id='two plus'),
    pytest.param(3,3,6,id='three plus'),
    pytest.param(4,4,8,id='four plus'),
    pytest.param(5,5,10,id='five plus' ),
])
def test_add(a,b,expect):
    assert add(a,b)==expect

if __name__ == '__main__':
    pytest.main(["-s","-v","test_param_one.py"])