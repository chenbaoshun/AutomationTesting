#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_one.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-04 20:23
# @Site    : 
# @version : V1.0

import pytest

def add(a,b):
    return a+b

'''
是对列表中的对象循环，然后一一的赋值
对象：列表，元组，字典
'''

# @pytest.mark.parametrize('a,b,expect',[
#     [1,1,2],
#     [2,2,4],
#     [3,3,6],
#     [4,4,8],
#     [5,5,10]
# ])
# def test_add(a,b,expect):
#     assert add(a,b)==expect

# @pytest.mark.parametrize('a,b,expect',[
#     (1,1,2),
#     (2,2,4),
#     (3,3,6),
#     (4,4,8),
#     (5,5,10)
# ])
# def test_add(a,b,expect):
#     assert add(a,b)==expect

@pytest.mark.parametrize('data',[
    {'a':1,'b':1,'expect':2},
    {'a':5,'b':5,'expect':10}
])
def test_add(data):
    assert add(data['a'],data['b'])==data['expect']

if __name__ == '__main__':
    pytest.main(["-s","-v","test_one.py"])

