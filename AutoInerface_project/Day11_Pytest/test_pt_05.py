#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_pt_05.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 22:34
# @Site    : 
# @version : V1.0

import pytest
import requests

def test_baidu():
    r = requests.get(url='http://www.baidu.com')
    assert r.status_code==200

def test_taobao():
    r = requests.get(url='http://www.taobao.com')
    assert r.status_code==200

def test_jd():
    r = requests.get(url='http://www.jd.com')
    assert r.status_code==200

def test_sina():
    r = requests.get(url='http://www.sina.com')
    assert r.status_code==200