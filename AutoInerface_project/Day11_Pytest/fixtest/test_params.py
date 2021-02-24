#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_params.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-06 22:41
# @Site    : 
# @version : V1.0

import pytest

def add(a,b):
    return a+b

@pytest.fixture()
def data():
    data = [
        [1,1,2],
        [2,2,4],
        [3,3,6]
        ]
    return data

@pytest.fixture()
def getData(data):
    return data.param

def test_one(getData):
    assert add(getData[0],getData[1])==getData[2]
