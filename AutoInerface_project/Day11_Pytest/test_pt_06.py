#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_pt_06.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 22:51
# @Site    : 
# @version : V1.0

import pytest
import requests
import json

def test_login():
    dict1 = {

    }
    r = requests.post(
        url='',
        json=dict1
    )
    assert '用户名' is r.json()