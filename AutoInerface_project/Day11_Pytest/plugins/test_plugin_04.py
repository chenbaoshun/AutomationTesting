#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_plugin_04.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-07 22:01
# @Site    : 
# @version : V1.0

import pytest
import requests

def test_baidu_001():
    r = requests.get(url='http://www.baidu.com/')
    assert r.status_code==200

def test_baidu_002():
    r = requests.get(url='http://www.baidu.com/',timeout=0.01)