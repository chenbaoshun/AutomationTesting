#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_ui.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-06 21:22
# @Site    : 
# @version : V1.0

import pytest
from selenium import webdriver

@pytest.fixture()
def driver01():
    driver01 = webdriver.Chrome()
    return driver01

driver01 = webdriver.Chrome()
driver01.maximize_window()
driver01.implicitly_wait(30)
driver01.get('http://www.baidu.com/')
driver01.find_element_by_id('kw')

@pytest.fixture()
def init(driver01):
    driver01.maximize_window()
    driver01.implicitly_wait(30)
    driver01.get('http://www.baidu.com/')
    yield
    driver01.quit()

def test_baidu_title(init,driver01):
    assert driver01.title=='百度一下，你就知道'