#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_pt_04.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 22:21
# @Site    : 
# @version : V1.0

import pytest

@pytest.mark.exit
def test_exit_01():
    assert 1==1

@pytest.mark.exit
def test_exit_02():
    assert 1==1

@pytest.mark.register
def test_register_01():
    assert 1==1

@pytest.mark.login
def test_login_01():
    assert 1==1